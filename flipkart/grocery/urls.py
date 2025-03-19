from django.urls import path
from grocery import views

urlpatterns = [
    path('product/', views.product_detail, name = "product_detail")
]