from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from Api.models import Customerlist
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def getter(request):
    if request.method=='GET':
        print(request.method)
        list_object=Customerlist.objects.all().values()
        print("your list_object of Customerlist is :",list_object)
        lists=list(list_object)
        dicts={'Customerlist':lists}
        return JsonResponse(dicts)

    elif request.method=='POST':
        print("Request body contents => ",request.body)
        print("Request body type =>",type(request.body))
        python_obj =json.loads(request.body)
        print("Request type=>",type(python_obj))
        print(python_obj)
        print(python_obj['name'])
        print(python_obj['address'])
        print(python_obj['title'])
        objj=Customerlist.objects.create(name=python_obj['name'],title=python_obj['title'],address=python_obj['address'],date='2020-12-1')
        obj_saver=objj.save()
        return JsonResponse({
            "message":"POST successfully!!"
        })
    else:
        return HttpResponse("Object is in another method,please type another method")


@csrf_exempt
def getter_by_id(request,ID):
    objj=Customerlist.objects.get(Postid=ID)

    if request.method=='GET':
        print(request.method)
        dicts= {'your name is':objj.name,
                'your title':objj.title,
                'your address is ':objj.address,
                'your date is ':objj.date
                }     
        return JsonResponse(dicts)

    elif request.method=='DELETE':
        objj.delete()
        return JsonResponse({'Deleted':'Message'})

    elif request.method=='PUT':
        # updatee=Customerlist.objects.put(Postid=ID)
        obb= json.loads(request.body)
        objj.name=obb['name']
        objj.title=obb['title']
        objj.address=obb['address']
        objj.save()
        return JsonResponse({'Updated':'Message'})

    else:
        return HttpResponse("object is on another format, please try again")

def Api_CarCustomization_pagination(request, PAGENO):
	SIZE = 2
	skip = SIZE * (PAGENO-1)
	page_Post = Customerlist.objects.all()[skip: PAGENO*SIZE]
	dict = {
		"Posts":list(page_Post.values("title","address"))}
	return JsonResponse(dict)
	


