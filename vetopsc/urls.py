from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view),
    path('home2/',views.home2_view),
    path('admin2/',views.admin_dashboard),
    path('manageem/',views.admin_manage)

]
