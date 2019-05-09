from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('home2/',views.home_view),
    path('',views.home2_view),
    path('admin2/',views.admin_dashboard),
    path('manageem/',views.admin_manage),
    path('treeview/',views.treeview_test),
    path('adminbase/',views.adminbase),
    path('manages/',views.manage),
    path('view/',views.tableview),
    url(r'^(?P<category>[\w|\W]+)/(?P<level>[\w|\W]+)/(?P<exam>[\w|\W]+)/(?P<module>[\w|\W]+)/(?P<sub_module>[\w|\W]+)/(?P<type>[\w|\W]+)/$',views.sub_module_view),

]
