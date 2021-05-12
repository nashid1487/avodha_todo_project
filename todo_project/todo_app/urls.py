from django.urls import path

from . import views

urlpatterns = [
    path('',views.task_view,name='task_view'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:task_id>/',views.update,name='update'),
    path('conobtask/',views.Task_lv.as_view(),name='conobtask'),
    path('conobdetail/<int:pk>',views.Task_dv.as_view(),name='conobdetail'),
    path('conobupdate/<int:pk>', views.Task_uv.as_view(), name='conobupdate'),
    path('conobdelete/<int:pk>', views.Task_delv.as_view(), name='conobdelete'),

]