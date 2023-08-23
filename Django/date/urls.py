from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.MainPage.as_view(), name="main_page"),
    path("review_list/", views.ReviewList.as_view(), name="review_list"),
    path("main_area/<str:q>/",views.SelectPage.as_view(), name="select_page"),
    path("place/",views.PlaceList.as_view(),name="place_list"),
    path("place/cafe/",views.PlaceCafe.as_view(),name = "place_cafe"),
    path("place/rest/",views.PlaceRest.as_view(),name = "place_rest"),
    path("place/place/",views.PlacePlace.as_view(),name = "place_place"),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    # django.contrib.auth앱의 LoginView 클래스를 활용했으므로 별도의 views.py 파일 수정이 필요 없음


]