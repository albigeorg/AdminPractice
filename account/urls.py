from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('admin_reg/',admin_reg,name='admin_reg'),
    path('admin_login/',admin_login,name='admin_login'),
    path('admin_dashboard/',admin_dashboard,name='admin_dashboard'),
    path('admin_logout/',admin_logout,name='admin_logout'),
    path('session/',admin_session,name='admin_session'),
]