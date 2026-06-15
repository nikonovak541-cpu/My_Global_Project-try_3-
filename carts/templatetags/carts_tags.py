from django import template

from carts.models import Cart


register = template.Library() # Да с БОЛЬШОЙ БУКВЫ, БОЛЬШИМ РЕГИСТРОМ НАДО ПИСАТЬ ПЕРВУЮ БУКВУ В СЛОВЕ "Library"

@register.simple_tag()
def user_cart(requset):
    if requset.user.is_authenticated:
        return Cart.objects.filter(user=requset.user) # Фильтруем по user, передаем объект пользователя для поиска