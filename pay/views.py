from django.shortcuts import render
from django.http import HttpResponse
import payjp
payjp.api_key = 'sk_test_9e835c1a09250c18e4891c1d'

user_id = 100


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

        #try:
            # create token
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
        print('+++++ token')
        print(token_id)
        # create user
        user_id = str(user_id + 1)
        user =payjp.Customer.create(
            description= item_name,
            id = user_id,
            email = user_email,
            card = token_id
        )
        user_id = user["id"]
        print('---- create user')
        print(user_id)
        ## pay
        item_price = int(item_price)
        charge = payjp.Charge.create(
            amount= item_price,
            customer=user_id,
            currency="jpy",
        )
        print('$$$$ charge')
        print(charge)
        #except Exception as e:
        #    print("例外args:", e.args)

        context = {'item_name':item_name, 'item_price':item_price ,'name':user_name, 'email':user_email, 'address':user_address}
        return render(request, 'pay/thanks.html', context)
        #return HttpResponse("Hello, world. You're at the polls index.")

    return render(request, 'pay/payjp.html')