from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('company-information', views.about, name="about_us"),
    path('catalog-of-product/', views.catalog, name="catalog_of_products"),
    path('some-extra-information', views.make_order, name="information"),
    path('payment-and-delivery', views.pay, name="pay_and_delivery"),
    path('discounts-and-promotions', views.promo, name="promotion"),
    path('catalog-of-product/<int:id>', views.product, name="product_page"),
    path('make-order/', views.make_order, name="order"),
    path('cart/', views.cart, name="cart_edit"),
    path('catalog-of-product/', views.add_to_cart, name="add_to_cart"),   #????
    path('catalog-of-product/add/', views.add_product, name="add_product"),
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += [path('accounts/', include('django.contrib.auth.urls'))]