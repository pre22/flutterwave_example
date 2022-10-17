from django.views.generic import CreateView
from django.urls import reverse_lazy
from payments.models import Salary

class PaymentView(CreateView):
    models = CreateView
    template_name = "payments/payment.html"
    success_url = reverse_lazy("home")