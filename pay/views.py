from django.shortcuts import render
from django.http import HttpResponse

def payjp(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    if request.method == "POST":

        item_name = "うまい！おせんべい" # 本当は Database から
        item_price = 100 # 本当は Database から
        user_name = request.POST['input_name']
        user_email = request.POST['input_mail']
        user_address = request.POST['input_address']

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

def payjp_2(request):
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

        if len(card_month) > 2:
            card_month = card_month[-2:] # for Chrome

        # token
        import payjp # この位置じゃないとダメ
        payjp.api_key = 'sk_test_9e835c1a09250c18e4891c1d'
        token = payjp.Token.create(
            card={
                'number' : card_number,
                'cvc' : card_cvc,
                'exp_month' : card_month,
                'exp_year' : card_year
            },
            headers={'X-Payjp-Direct-Token-Generate': 'true'}
        )
        token_id = token['id']
        print('\n+++++ token')
        print(token_id)

        # create user
        user =payjp.Customer.create(
            #name = user_name, # 決済フローの中で name は指定できない様子
            description= "どこから？　" + item_name,
            email = user_email,
            card = token_id
        )
        user_id = user["id"]
        print('\n---- create user')
        print(user_id)

        ## pay
        item_price = int(item_price)
        charge = payjp.Charge.create(
            amount= item_price,
            customer=user_id,
            currency="jpy",
        )
        paied_id = charge['id']
        print('\n$$$$ charge')
        print(charge)

        context = {'item_name':item_name, 'item_price':item_price ,'name':user_name, 'email':user_email, 'address':user_address, 'paied_id':paied_id}
        return render(request, 'pay/thanks2.html', context)
    
    return render(request, 'pay/payjp2.html')