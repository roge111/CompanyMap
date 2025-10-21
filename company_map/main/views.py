from django.shortcuts import render

from integration_utils.bitrix24.bitrix_user_auth.main_auth import main_auth

# Create your views here.
@main_auth(on_cookies=True)
def company_map(request):
    token = request.bitrix_user_token
    
    companies = token.call_list_method('crm.company.list')
    companies_info = []
    for company in companies:
        context = {
            'name': company.get('TITLE'),
            'address': company.get('ADDRESS'),
            'city': company.get('ADDRESS_CITY'),
            'country': company.get('ADDRESS_COUNTRY'),
            'region': company.get('ADDRESS_REGION')
        }
        companies_info.append(context)
    
    # Передаем данные в шаблон
    return render(request, 'main/company_map.html', {
        'companies_info': companies_info
    })

@main_auth(on_start=True, set_cookie=True)
def start(request):
    return render(request, 'main/start.html')