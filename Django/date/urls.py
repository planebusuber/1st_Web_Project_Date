from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainPage.as_view(), name="main_page"),
    path("review_list/", views.ReviewList.as_view(), name="review_list"),
    path("main_area/<str:q>/",views.SelectPage.as_view(), name="select_page"),
    path("place/",views.PlaceList.as_view(),name="place_list"),
    path("place/cafe/",views.PlaceCafe.as_view(),name = "place_cafe"),
    path("place/rest/",views.PlaceRest.as_view(),name = "place_rest"),
    path("place/place/",views.PlacePlace.as_view(),name = "place_place"),
    path("write/", views.ReviewCreate.as_view(), name="review_write")
]