from django.urls import path,include
from . import views
urlpatterns =[
    path('', views.HomePageView.as_view(),name= 'home'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/signup/',views.SignUpView.as_view(),name='signup')

]