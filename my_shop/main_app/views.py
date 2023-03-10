from datetime import datetime
from email import message
from http.client import NOT_FOUND
from unicodedata import category
from django.shortcuts import render, redirect
from .models import Products, Clients, Category
from .forms import ClientForm, OrderForm, NewProductForm



def index(request):
    categories = Category.objects.all()
    return render(request, 'main_app/index.html', {'title': 'Нью Гарден', 'categories': categories ,})
#____________________________________________________________________

def about(request):
    categories = Category.objects.all()
    return render(request, 'main_app/about.html', {'title': 'Покупателям', 'categories': categories ,})
#____________________________________________________________________

def catalog(request):
    
    try:
        categories = Category.objects.all()
        products = Products.objects.order_by('title').filter(isActive=True)


        return render(request, 'main_app/catalog.html', {
                                                        'title': 'Каталог "Нью Гарден"', 
                                                        'products': products,
                                                        'categories': categories 
                                                        })
    except:
        return NOT_FOUND
#____________________________________________________________________

def info(request):
    categories = Category.objects.all()
    return render(request, 'main_app/info.html', {'title': 'Покупателям', 'categories': categories ,})
#____________________________________________________________________

def pay(request):
    categories = Category.objects.all()
    context = {
        "order_message" : "Благодарим, Ваш заказ успешно оформлен. Детали смотрите на e-mail. Менеджер свяжется с Вами в ближайшее время",
        'title': 'Оплата и доставка', 
        'categories': categories ,
    }                  #подтянуть номер заказа из базы для отображения + отправка информации на E-mail

    return render(request, 'main_app/pay_and_delivery.html', context)
#____________________________________________________________________

def promo(request):
    categories = Category.objects.all()
    return render(request, 'main_app/promo.html',{'title': 'Акции!', 'categories': categories ,})

#____________________________________________________________________

def product(request, id):
    categories = Category.objects.all()
    try:
        product = Products.objects.get(id=id)
        form = OrderForm()

        if request.method == 'POST':
            form = OrderForm(request.POST)

            # if form.is_valid():
            #     new_order = 
            #     form.save()
            #     return redirect('pay_and_delivery')

        return render(request, 'main_app/product_page.html', {'title': 'страница товара',
                                                              'product': product, 
                                                              'form':form,
                                                              'categories': categories ,
                                                              })
    except:
        return NOT_FOUND                                #сделать страницу для NOT_FOUND
    
    
    
    #     #clients = Clients.objects.all("email")
    # # new_client = ClientForm
    # error = ''
    # if request.method == 'POST':
    #     form = ClientForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('pay_and_delivery')
    #     #elif ClientForm.
    #     else:                                              #добавить валидацию на существующего пользователя
    #         error = 'Неверно заполнена форма'

    # form = ClientForm()
    
    # context = {
    #     'title': 'Оформление заказа', 
    #     'form': form,
    #     'error' : error
    # }
    # return render(request, 'main_app/make_order.html', context )
#____________________________________________________________________

def cart(request):
    categories = Category.objects.all()
    return render(request, 'main_app/cart.html', {'title': 'Корзина', 'categories': categories ,})

#____________________________________________________________________

def make_order(request):
    categories = Category.objects.all()
    #clients = Clients.objects.all("email")
    # new_client = ClientForm
    message = ''
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)

        if form.is_valid():
            new_client = form.save(commit=False)
            # new_client.name = form.cleaned_data['name']
            # new_client.email = form.cleaned_data['email']
            # new_client.phone = form.cleaned_data['phone']
            # new_client.adress = form.cleaned_data['adress']
            new_client.save()
            form.save_m2m()
            message = "Новый клиент добавлен в базу данных"
            return redirect('pay_and_delivery')
        #elif ClientForm.
        else:                                              #добавить валидацию на существующего пользователя
            message = 'Неверно заполнена форма'

    context = {
        'title': 'Оформление заказа', 
        'form': form,
        'message' : message,
        'categories': categories ,
    }
    return render(request, 'main_app/make_order.html', context )

#____________________________________________________________________

def add_to_cart(request):                                 #редактировать
    categories = Category.objects.all()
    message = "Товар успешно добавлен в корзину"
    items = {}
        
    context = { 'message':message,
                'categories': categories ,
                }   
                  
    return render(request,'main_app/catalog.html', context )

#____________________________________________________________________

def add_product(request): 
    categories = Category.objects.all()
    form = NewProductForm()
    message = ''
    if request.method == 'POST':
        form = NewProductForm(request.POST, request.FILES)

        if form.is_valid():
            new_product = form.save(commit=False)
            new_product.category = Category.objects.get(Products.category)
            new_product.created = datetime.now
            new_product.updated = datetime.now
            new_product.save()
            form.save_m2m()

            message = "Новый товар добавлен в базу данных"
            return redirect('catalog_of_products')
        # else:                                              
        #     message = 'Неверно заполнена форма'

    return render(request, 'main_app/add_product.html', {
        'title': 'Добавление нового товара', 
        'form': form,
        'message' : message,
        'categories': categories ,
    } )