from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from datetime import datetime
import decimal

'''# Create your views here.
def myself(request):
    if request.method=='GET':    
        return HttpResponse("hi iam shivam")
def index(request):
    return render(request,'index.html')
def about(request):
    return HttpResponse("this is about")'''
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from dataaccess import get_dashboard

'''@csrf_exempt
def register(request):
    if request.method=='GET':
        id_value=request.GET.get('id')
        if id_value is None:
            return JsonResponse({"error not given "},status=400)
        #studentdata=get_studentData(id_value)
        for student in studentdata:
            return [{"id":student[0],"firstname":student[1],"lastname":student[2],"fathername":student[3],"mothername":student[4],"DOB":student[5],"status":student[6] }]'''
         
def dashboard(request):
    if request.method=='GET':
        data,data_list=get_dashboard()
        birthday_array=[]
        for eachbirthday in sorted(data_list):
            
            
            birthday={
                    "firstname":eachbirthday[0],
                    "lastname":eachbirthday[1],
                    "dateOfbirth":eachbirthday[2]
            }
            birthday_array.append(birthday)
            print(data)
        '''def make_take_decimal(value):
            if isinstance(value,decimal.Decimal):
                value=float(value)
            return value[0]        
        expenses_array=[]
        
        for key,value in expenses_dict.items():
           
            expenses_json={
                "horizontalvalue":key,
                "verticalvalue":make_take_decimal(value[0][0])
            }
            expenses_array.append(expenses_json)
        student_data=[]
        for key,value in student_wise_data.items():
           
                studentWisedata={
                    "horizontalvalue":key,
                    "verticalvalue":value
                }
                student_data.append(studentWisedata)
        group_data=[]
        for key,value in group_dict.items():
           
                groupWisedata={
                    "horizontalvalue":key,
                    "verticalvalue":value
                }
                group_data.append(groupWisedata)
                '''
        return JsonResponse({
            "activestudentcount":data["activestudentdata"],
            "upcomingbirthdays":birthday_array,
            "averageStudentAttendence":75,
            
            },safe=False)
    else:
        return JsonResponse("fail")
'''@csrf_exempt
def insert(request):
    if request.method=="POST":
        try:
            data=json.loads(request.body.decode("utf-8"))
            name=data.get("name")
            print(name)
            gender=data.get("gender")
            dob=data.get("dob")
            print(dob)
            insert_student(name,gender,dob)
            return JsonResponse({"message":"data stored successfully"})
        except Exception as e:
            return JsonResponse({"error":"only post allowed"})
            '''