from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.ProductListView.as_view(), name='home'),
    path('filter/', views.FilterProductListView.as_view(), name='filter'),
    path('cart/', views.CartListView.as_view(), name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    path('question/', views.question, name='question'),
    path('<int:pk>/', views.ProductDetailView.as_view()),
    path('add_product/', views.add_product_to_cart, name="add_product_to_cart"),
    path('remove_product/', views.remove_product_from_cart, name="remove_product_from_cart"),
    path('update_product/', views.update_product_in_cart, name="update_product_in_cart"),
]