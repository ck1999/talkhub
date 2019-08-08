from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from admin_module.models import UserApplication
from django.core import serializers
import json

def getApplications(request):
    result = map(lambda x: {'email': x.email, 'phone': x.phone, 'name': x.name, 'id': x.id }, list(UserApplication.objects.all()))
    return JsonResponse({"status":"ok", "result": list(result)})
    
@csrf_exempt
def submit_application(request):
    if request.method != 'POST':
        return JsonResponse({"status":'bad', "error": request.method + ' is not allowed'}, status=405)
    body = request.body.decode('utf-8')
    try:
        body = json.loads(body)
    except ValueError:
        return JsonResponse({"status":'bad', "error": 'data should be a valid JSON'}, status=400)

    print(body)
   
    
    def getDataFromDict(d, key):
        if key in d:
            return d[key]
        return None

    name = getDataFromDict(body, 'name')
    email = getDataFromDict(body, 'email')
    phone = getDataFromDict(body, 'phone')

    print(name)
    print(email)
    print(phone)  

    
    def is_empty_string(val):
        return type(val) is not str or len(val) == 0

    if is_empty_string(name):
        return JsonResponse({"status":'bad', "error": 'name is required!'}, status=400)

    if is_empty_string(email) and is_empty_string(phone):
        return JsonResponse({"status":'bad', "error": 'email or phone is required!'}, status=400)
    
    #create here
    result = UserApplication.objects.create(email=email, name=name, phone=phone)
    print(result)
    return JsonResponse({"status": 'ok'})
    
def hello(request):
    return JsonResponse({"status":'ok', "result": 'TEST'}, status=200)
