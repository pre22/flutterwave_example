from django.shortcuts import render
from django.http import request, HttpResponse
from django.views.decorators.http import require_http_methods
from products.forms import PaymentForm

# Create your views here.
def product_detail(request):
    if request.method == "POST":
        form = PaymentForm(request.POST)
        if form.is_valid():
            name =  form.cleaned_data["name"]
            email =  form.cleaned_data["email"]
            amount =  form.cleaned_data["amount"]
            phone =  form.cleaned_data["phone"]
            return redirect(str(process_payment(name, email, amount, phone)))
    else:
        form = PaymentForm()
    return render(request, "payments/payment.html", {"form":form})

def process_payment(name,email,amount,phone):
    auth_token = 
    head = {
        'Authorization': 'Bearer' + auth_token
    }
    data = {
        "tx_ref": '' + str(math.floor(1000000 + random.random()*9000000)),
        "amount": amount,
        "currency": "USD",
        "redirect_url": "http://localhost:8000/callback",
        "payment_options": "card",
        "customer": {
            "email": email,
            "phonenumber": phone,
            "name": name
        },
        "customizations": {
            "title": "My Store",
            "description": "Best Store in Town",
            "logo": "My Lgo"
        }
    }
    url = "https://api.flutterwave.com/v3/payments"
    response = requests.post(url, json=data, headers=head)
    response = response.json()
    link = response["data"]["link"]
    return link

@require_http_methods(["GET", "POST"])
def payment_response(request):
    status = request.GET.get('status', None)
    tx_ref = request.GET.get('tx_ref', None)

    return HttpResponse('Finished')