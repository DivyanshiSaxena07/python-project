from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from api.models import Student
from api.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
# from api.serializtions import 
import io

# Create your views here.

def student_detail(request,val):
    stu=Student.objects.get(id=val)
    serializer=StudentSerializer(stu)
    # print(serializer.data)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)

def student_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many='True')
    # print(serializer.data)
    # json_data=JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)

@csrf_exempt
def student_info(request):
    if request.method == 'POST':
     j_data= request.body
     stream=io.BytesIO(j_data)
     pydata = JSONParser().parse(stream)
     serializer = StudentSerializer(data=pydata)
     if serializer.is_valid():
         serializer.save()
         res={'msg':'Data is created!'}
         return JsonResponse(res, safe=False) 
     return JsonResponse(serializer.errors) 
 
    if request.method == 'GET':
        j_data = request.body
        stream = io.BytesIO(j_data)
        pydata = JSONParser().parse(stream)
        id = pydata.get('id',None)
        
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return JsonResponse(serializer.data)    
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if request.method == 'PUT':
        j_data = request.body
        stream = io.BytesIO(j_data)
        pydata = JSONParser().parse(stream)
        id = pydata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=pydata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data is Updated!'}
            return JsonResponse(res, safe=False) 
        return JsonResponse(serializer.errors) 
    
    if request.method == 'DELETE':
        j_data = request.body
        stream=io.BytesIO(j_data)
        pydata = JSONParser().parse(stream)
        id = pydata.get('id')
        stu = Student.objects.get(id = id)
        stu.delete()
        res={'msg':'Data Deleted Successful!'}
        return JsonResponse(res) 
    
                
                                                                                                                                                                          
    