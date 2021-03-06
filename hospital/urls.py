from django.urls import path, include
from django.contrib.auth import views as auth_views

from  .import views
from .views import *

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='service'),
    path('appointment/',views.appointment,name='appointment'),
    #path('signup/',RegistrationView.as_view(),name='signup'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    #path('search/',views.search,name='search'),
    path('signup/',views.signup,name='signup'),
	path('accounts/',include('django.contrib.auth.urls')),
]