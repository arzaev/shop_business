from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.ProductListView.as_view(), name='home'),
    path('filter/', views.FilterProductListView.as_view(), name='filter'),
    path('<int:pk>/', views.ProductDetailView.as_view()),
    path('add_product/', views.add_product_to_cart, name="add_product_to_cart"),
    path('remove_product/', views.remove_product_from_cart, name="remove_product_from_cart"),
]