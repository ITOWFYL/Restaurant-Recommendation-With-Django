# RestaurantRecommendation 의 urls.py 에서 넘어옴 

from django.urls.conf import path
from . import views    # 현재 위치에서 views.py 파일(모듈) 불러오기

urlpatterns = [
    path('Send/', views.sendEmail),
]