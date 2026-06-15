from django.shortcuts import redirect, render

from carts.models import Cart
from goods.models import Products

def cart_add(request, product_slug):
    
    product = Products.objects.get(slug=product_slug) # Объект продукта , который нужно добавить в корзину

    if request.user.is_authenticated: # Если он авторизованный
        carts = Cart.objects.filter(user=request.user, product=product) # Запрос на все корзины которые есть по конкретному продукту.

        if carts.exists(): # Если у пользователя уже есть добавленный товар к корзину
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1) # Если карт нет, то мы создаем их

    return redirect(request.META['HTTP_REFERER']) # С какой страницы пользователь попал, туда и возвращается


def cart_change(request, prduct_slug):
    ...


def cart_remove(request, cart_id):
    
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return redirect(request.META['HTTP_REFERER']) # С какой страницы пользователь попал, туда и возвращается