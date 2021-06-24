from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse('인덱스입니다')
    return render(request, 'index.html')
    
def restaurantDetail(request):
    # return HttpResponse('레스토랑 디테일입니다')
    return render(request, 'restaurantDetail.html') 
    
def restaurantCreate(request):
    # return HttpResponse('레스토랑 생성!')
    return render(request, 'restaurantCreate.html')

def categoryCreate(request):
    # return HttpResponse('카테고리 생성!')
    return render(request, 'categoryCreate.html')