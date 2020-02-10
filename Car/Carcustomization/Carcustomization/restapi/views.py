from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from firstapp.models import CustomerList
import json

@csrf_exempt
def view_get_post_customerlist(request):
    print("What's the request => ",request.method)
    if request.method == "GET":
        Customer = CustomerList.objects.all()
        print("QuerySet objects => ",customer)
        list_of_customer = list(customer.values("name","title"))
        print("List of customer objects => ",list_of_customer)
        dictionary_name = {
        "customer":list_of_customer
    }
        return JsonResponse(dictionary_name)
    elif request.method == "POST":
        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>",python_dictionary_object)
        print("Python dictionary type=>",type(python_dictionary_object))
        print(python_dictionary_object['name'])
        print(python_dictionary_object['title'])
        CustomerList.objects.create(name=python_dictionary_object['name'],title=python_dictionary_object['title'])
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")

@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    print("What's the request =>",request.method)
    if request.method == "GET":
        customer = CustomerList.objects.get(id = Postid)
        print(type(customer. name))
        return JsonResponse({
            "id":customer.Postid,
            " name":customer.name,
            "title":custmoer.title
        })
    else:
        return JsonResponse({
        "message":" Other htpp verbs Testing"
        })
