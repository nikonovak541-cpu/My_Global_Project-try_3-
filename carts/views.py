from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from carts.models import Cart
from carts.utils import get_user_carts
from goods.models import Products

def cart_add(request):
    
    product_id = request.POST.get("product_id")

    product = Products.objects.get(id=product_id) # Объект продукта , который нужно добавить в корзину

    if request.user.is_authenticated: # Если он авторизованный
        carts = Cart.objects.filter(user=request.user, product=product) # Запрос на все корзины которые есть по конкретному продукту.

        if carts.exists(): # Если у пользователя уже есть добавленный товар к корзину
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1) # Если карт нет, то мы создаем их


    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": user_cart}, request=request)

    response_data = {
        "message": "Товар добавлен в корзину",
        "cart_items_html": cart_items_html,
    }
    return JsonResponse(response_data)


def cart_change(request):
    cart_id = request.POST.get("cart_id")
    quantity = request.POST.get("quantity")

    cart = Cart.objects.get(id=cart_id)

    cart.quantity = quantity
    cart.save()
    updated_quantity = cart.quantity

    cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html", {"carts": cart}, request=request)
    
    
    response_data = {
        "message": "Количество изменено",
        "cart_items_html": cart_items_html,
        "quantity_delete": updated_quantity,
    }
    
    return JsonResponse(response_data)


def cart_remove(request):

    cart_id = request.POST.get("cart_id")
    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    user_cart = get_user_carts(request)

    # Вычисляем итоги здесь, чтобы быть уверенными
    total_price = sum(item.product.sell_price() * item.quantity for item in user_cart)
    total_quantity = sum(item.quantity for item in user_cart)

    # Передаём их в контекст отдельно
    context = {
        "carts": user_cart,
        "total_price": total_price,
        "total_quantity": total_quantity,
    }
    cart_items_html = render_to_string(
        "carts/includes/included_cart.html",
        context,
        request=request
    )

    response_data = {
        "message": "Товар удален",
        "cart_items_html": cart_items_html,
        "quantity_deleted": cart.quantity,
        "total_price": float(total_price),
        "total_quantity": total_quantity,
    }
    return JsonResponse(response_data)

# -----------------------------
    # УБИЛ ЗДЕСЬ ПОЧТИ 5 ДНЕЙ. НО МОДАЛЬНОЕ ОКНО ПЕРЕСТАЛО ПОКАЗЫВАТЬ (NAN) ТОЛЬКО КОГДА НАЧАЛ ИСПОЛЬЗОВАТЬ (CONTEXT) - РАБОЧИЙ СПОСОБ НАВЕРХУ!!!!!!!
    # СПАСИБО ВЕЛИКОМУ GOOGLE И PYTHON DOCUMENTATION!! 
# -----------------------------
