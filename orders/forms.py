import re

from django import forms


# ---------КАСТОМНЫЕ ФОРМЫ ( ПОПЫТКА 2) -----------#
class CreateOrderForm(forms.Form):
    
    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
            ],
        )
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(
        choices=[
            ("0", False),
            ("1", True),
            ],
            required=False,
        )

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']

        if not data.isdigit(): # Если не из цифр состоит введеное пользователем
            raise forms.ValidationError("Номер телефона должен содержать только цифры!")
        
        pattern = re.compile(r'^\d{10}$') # А вот тут регулярные выражение идет в ход (ПРЕПОДГОТОВИТЬ ШАБЛОН (НОМЕР ТЕЛЕФОНА ДОЛЖЕН СОСТОЯТЬ ИЗ 10-ТИ ЦИФР))
        if not pattern.match(data): # Если не подходит под шаблон
            raise forms.ValidationError("Неверный формат номера!")
        
        return data




    #-------------КАСТОМНЫЕ ФОРМЫ (ПОПЫТКА 1) -----------#
    #-------------ЧТОБЫ НЕ ХРАНИТЬ ФРОНТЭНД В БЭКЭНД ЧАСТИ------------# !!!!!САМ СЕБЕ ВСЕ УСЛОЖНИЛ!!!!
    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form_control",
    #             "placeholder": "Введите ваше имя",
    #         }
    #     )
    # )

    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Введите вашу фамилию",
    #         }
    #     )
    # )

    # phone_number = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control",
    #             "placeholder": "Номер телефона",
    #         }
    #     )
    # )

    # requires_delivery = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #     choices=[
    #         ("0", False),
    #         ("1", True),
    #     ],
    #     initial=0,
    # )

    # delivery_address = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={
    #             "class": "form-control",
    #             "id": "delivery_address",
    #             "rows": 2,
    #             "placeholder": "Введите адрес доставки",
    #         }
    #     ),
    #     required=False,
    # )

    # payment_on_get = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #     choices=[
    #         ("0", False),
    #         ("1", True),
    #     ],
    #     initial="card",
    # )