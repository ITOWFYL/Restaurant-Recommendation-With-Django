from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def sendEmail(request):
   return HttpResponse("이메일 보냈습니다") 