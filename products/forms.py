from django import forms


class PaymentForm(forms.Form):
    name = forms.CharField(label="Full Name", max_length=100)
    email =  forms.EmailField()
    phone = forms.CharField(max_length=15)
    amount = forms.FloatField()