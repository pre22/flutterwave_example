from django.views.generic import CreateView
from django.urls import reverse_lazy
from payments.models import Salary

class PaymentView(CreateView):
    model = Salary
    fields = "__all__"
    template_name = "payments/payment.html"
    success_url = reverse_lazy("home")

    # def form_valid(self, form):
    #     form.instance.employee = self.request.user.employee
    #     form.instance.company = self.request.user.employee.company
    #     return super().form_valid(form)  