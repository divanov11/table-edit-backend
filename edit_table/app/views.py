from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import *

def index(request):
	return render(request, 'app/backend_table.html')

#API data
def testsDataAPI(request):
	data = Test.objects.all()
	dataList = []

	for i in data:
		dataList.append({'name':i.name, 'result':i.result, 'id':i.id})

	return JsonResponse(dataList, safe=False)

@csrf_exempt
def createTest(request):
	name = request.POST.get('name')
	result = request.POST.get('result') 

	Test.objects.create(
		name=name,
		result=result,
		)
	return JsonResponse('Test Created!', safe=False)

@csrf_exempt
def updateTest(request):
	objId = request.POST.get('id')
	result = request.POST.get('result')
	
	test = Test.objects.get(id=objId)
	test.result = result
	test.save()

	return JsonResponse('Test Updated!', safe=False)

@csrf_exempt
def deleteTest(request):
	print('Delete called!')
	objId = request.POST.get('id')
	test = Test.objects.get(id=objId)
	test.delete()

	return JsonResponse('Test Deleted!', safe=False)

