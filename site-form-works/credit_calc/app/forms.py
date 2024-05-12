from django import forms


class CalcForm(forms.Form):
    initial_fee = forms.IntegerField(label="Стоимость товара", min_value=1)
    rate = forms.FloatField(label="Процентная ставка", min_value=1, max_value=100)
    months_count = forms.IntegerField(label="Срок кредита в месяцах", min_value=1, max_value=360)
    #
    # def clean_initial_fee(self):
    #     # валидация одного поля, функция начинающаяся на `clean_` + имя поля
    #     initial_fee = self.cleaned_data.get('initial_fee')
    #     if not initial_fee or initial_fee < 0:
    #         raise forms.ValidationError("Стоимость товара не может быть отрицательной")
    #     return initial_fee

    def clean(self):
        # общая функция валидации
        return self.cleaned_data
