import requests
from django import forms


class AddCarForm(forms.Form):
    brand = forms.CharField(label='Марка',
                            widget=forms.TextInput(attrs={'placeholder': 'модель', 'class': 'form-control'}))
    model = forms.CharField(label='Модель',
                            widget=forms.TextInput(attrs={'placeholder': 'модель', 'class': 'form-control'}))
    price = forms.CharField(label='Цена',
                            widget=forms.NumberInput(attrs={'placeholder': 'text', 'class': 'form-control'}))
    count = forms.IntegerField(label='Количество',
                               widget=forms.NumberInput(attrs={'placeholder': 'text', 'class': 'form-control'}))


class ConverterForm(forms.Form):
    # url = 'https://api.exchangerate.host/latest'
    # response = requests.get(url)
    # data = response.json()
    # data = [*data['rates']]
    # currencies = [(i, i) for i in data]

    url = 'https://api.exchangerate.host/symbols'
    response = requests.get(url)
    data = response.json()
    data = data['symbols']
    currencies = [(i, f'{j["description"]} ({i})') for i, j in data.items()]

    input_currency_combobox = forms.ChoiceField(label='Валюта 1', choices=currencies,
                                                widget=forms.Select(attrs={'class': "form-control"}))
    input_currency_entry = forms.IntegerField(label='Сколько перевести',
                                              widget=forms.NumberInput(
                                                  attrs={'placeholder': 'сколько?', 'class': 'form-control'}))
    output_currency_combobox = forms.ChoiceField(label='Валюта 2', choices=currencies,
                                                 widget=forms.Select(attrs={'class': "form-control"}))

    output_currency_entry = forms.IntegerField(label='Результат', disabled=True, required=False,
                                               widget=forms.NumberInput(
                                                   attrs={'placeholder': 'ответ будет тут', 'class': 'form-control'}))
