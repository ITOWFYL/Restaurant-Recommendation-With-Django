# RestaurantRecommendation 의 urls.py 에서 넘어옴 

from . import views
from django.urls.conf import path

# urlpatterns 오타로 인한 에러
urlpatterns = [
    path('', views.index, name='index'),
    path('restaurantDetail/', views.restaurantDetail),
    path('restaurantCreate/', views.restaurantCreate),
    path('categoryCreate/', views.categoryCreate),
]
