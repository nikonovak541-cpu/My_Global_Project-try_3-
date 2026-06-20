from django.contrib import admin

from carts.models import Cart




# admin.site.register(Cart)

class CartTabAdmin(admin.TabularInline): # Табулярный вариант таблицы
    model = Cart # Модель к которой идет привязка
    fields = "product", "quantity", "created_timestamp" # Поля для отображения в инлайне режиме
    search_fields = "product", "quantity", "created_timestamp" # Поля для отображения в инлайне режиме
    readonly_fields = ["created_timestamp"] # Для невозможност] изменять в инлайн режиме
    extra = 1 # Свободные поля для добавления пользователю новых заказов


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ["user_display", "product_display", "quantity", "created_timestamp"] # created_timestamp - ЭТО ПОЛЕ МОДЕЛИ ДЛЯ АВТОМАТИЧЕСКОГО СОХРАНЕНИЯ ДАТЫ И ВРЕМЕНИ СОЗДАНИЯ ОБЪЕКТА (ЗАПИСИ В БД)
    list_filter = ["created_timestamp", "user", "product__name"] #---------- ИСПОЛЬЗУЕТСЯ ДЛЯ ОТСЛЕЖИВАНИЯ ТОГО, КОГДА ИМЕННО БЫЛА ДОБАВЛЕНА ЗАПИСЬ (ЗАКАЗ,ТОВАР В КОРЗИНЕ, ПОЛЬЗОВАТЕЛЬ) КАК ПРИМЕР!!!!


    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"
    
    def product_display(self,obj):
        return str(obj.product.name)


