from django.urls import path 
from payments.views import PaymentView, TransactionSuccessView


urlpatterns = [
    path("", PaymentView.as_view(), name="payment"),
    path("success/", TransactionSuccessView.as_view(), name="success")
]
