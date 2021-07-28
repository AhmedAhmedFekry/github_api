from django.urls import path
from api import views 
urlpatterns = [

    path("", views.home, name="api"),
    path('all/', views.Home.as_view()),

]
