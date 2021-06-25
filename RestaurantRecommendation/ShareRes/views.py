from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

# Create your views here.
def index(request):
    # return HttpResponse('인덱스입니다')
    categoryAll = Category.objects.all()
    restaurantAll = Restaurant.objects.all()
    content = {'categories': categoryAll, 'restaurants': restaurantAll}
    return render(request, 'index.html', content)
    
def restaurantDetail(request):
    # return HttpResponse('레스토랑 디테일입니다')
    return render(request, 'restaurantDetail.html') 
    
def restaurantCreate(request):
    # return HttpResponse('레스토랑 생성!')
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'restaurantCreate.html', content)

def restaurantCreateCreate(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id=category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    
    new_res = Restaurant(
                category=category,
                restaurant_name=name,
                restaurant_link=link,
                restaurant_content=content,
                restaurant_keyword=keyword,
              )
    new_res.save()
    
    return HttpResponseRedirect(reverse('index'))  

def categoryCreate(request):
    # return HttpResponse('카테고리 기본그룹')
    categoriesAll = Category.objects.all()    # 데이터베이스에서 값 가져오기
    content = {'categories': categoriesAll}    # 딕셔너리 생성
    return render(request, 'categoryCreate.html', content)    # 딕셔너리 전달

def categoryCreateCreate(request):
    # return HttpResponse('카테고리 추가할거야')
    categoryNameInput = request.POST['categoryNameName']    # HTML템플레이트 안에 input 태그의 id 값을 POST 방식으로 처리해서 변수에 담는다
    newCategory = Category(categoryName=categoryNameInput)
    newCategory.save()
    return HttpResponseRedirect(reverse('index'))

def categoryCreateDelete(request):
    category_Id = request.POST['categoryId']
    deleteCategory = Category.objects.get(id=category_Id)
    deleteCategory.delete()
    return HttpResponseRedirect(reverse('categoryCreateN'))
    
