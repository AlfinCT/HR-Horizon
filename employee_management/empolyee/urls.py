from django.urls import path, include

from empolyee import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('add_employee',views.add,name='add'),
    path('view',views.view,name='view'),
    path('home', views.home, name='home'),
    path('logout', views.logout, name='logout'),
    path('employee/<int:emp_id>/update/', views.update, name='update'),
    path('employee/<int:emp_id>/delete/', views.delete, name='delete'),

]