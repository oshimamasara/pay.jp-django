from django.shortcuts import render
from django.http import HttpResponse

user_id = 100


def payjp(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == "POST":

        item_name = "うまい！おせんべい" # 本当は Database から
        item_price = 100 # 本当は Database から
        user_name = request.POST['input_name']
        user_email = request.POST['input_mail']
        user_address = request.POST['input_address']
        card_number = request.POST['card_number']
        card_cvc = request.POST['card_cvc']
        card_month = request.POST['card_month']
        card_year = request.POST['card_year']

        # pay.jp token from form method
        print(request.POST['payjp-token'])
        # create token
        import payjp # この位置じゃないとダメ
        payjp.api_key = 'sk_test_9e835c1a09250c18e4891c1d'
        customer = payjp.Customer.create(
            email=user_email,
            card=request.POST['payjp-token']
        )

        payjp.Charge.create(
            amount= item_price,
            currency='jpy',
            customer=customer.id,
            description= item_name
        )

        context = {'item_name':item_name, 'item_price':item_price ,'name':user_name, 'email':user_email, 'address':user_address}
        return render(request, 'pay/thanks.html', context)

    return render(request, 'pay/payjp.html')