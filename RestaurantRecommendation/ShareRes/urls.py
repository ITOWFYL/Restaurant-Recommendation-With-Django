# RestaurantRecommendation 의 urls.py 에서 넘어옴 

from . import views
from django.urls.conf import path

# urlpatterns 오타로 인한 에러
urlpatterns = [
    # 함수 이름 소문자로 시작, html파일도 소문자로 시작, 그렇다면 path(주소경로)도 소문자로 해야한다
    path('', views.index, name='index'),
    path('restaurantDetail/', views.restaurantDetail, name='restaurantDetailN'),
    path('restaurantCreate/', views.restaurantCreate, name='restaurantCreateN'),
    path('restaurantCreate/create', views.restaurantCreateCreate, name='restaurantCreateCreateN'),
   
    path('categoryCreate/', views.categoryCreate, name='categoryCreateN'),
    path('categoryCreate/create', views.categoryCreateCreate, name='categoryCreateCreateN'),
    path('categoryCreate/delete', views.categoryCreateDelete, name='categoryCreateDeleteN'),
]

