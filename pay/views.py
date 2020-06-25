from django.shortcuts import render
from django.http import HttpResponse


def payjp(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == "POST":
        item_name = "うまい！おせんべい" # 本当は Database から
        item_price = "100" # 本当は Database から
        user_name = request.POST['input_name']
        user_email = request.POST['input_mail']
        user_address = request.POST['input_address']
        card_number = request.POST['card_number']
        card_cvc = request.POST['card_cvc']
        card_month = request.POST['card_month']
        card_year = request.POST['card_year']

        print(user_name)
        print(user_email)
        print(user_address)
        print(card_number)
        print(card_cvc)
        print(card_month)
        print(card_year)
        context = {'item_name':item_name, 'item_price':item_price ,'name':user_name, 'email':user_email, 'address':user_address}
        return render(request, 'pay/thanks.html', context)
        #return HttpResponse("Hello, world. You're at the polls index.")

    return render(request, 'pay/payjp.html')