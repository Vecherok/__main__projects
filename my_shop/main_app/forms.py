
from django import forms
from .models import Clients, Products


class ClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['name','email','phone','adress']
        widgets = {
                    'name': forms.TextInput(attrs={
                        'placeholder' : 'Имя и фамилия',
                        'class' : 'form-control'
                    }),
                    'email': forms.EmailInput(attrs={
                        'placeholder' : 'Электронная почта',
                        'class' : 'form-control'
                    }),
                    'phone': forms.NumberInput(attrs={
                        'placeholder' : 'Номер телефона',
                        'class' : 'form-control'
                    }),
                    'adress': forms.TextInput(attrs={
                        'placeholder' : 'Адрес',
                        'class' : 'form-control'
                    })
                }

class NewProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ('category','code','title','subtitle','content','image','price','count')
    
    


class OrderForm(forms.Form): pass

    #count = forms.ChoiceField(choices=Products.count)  #добавить %(limit_value)s