from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Built-in login/logout views
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    
    # App pages
    path('courses/', views.courses_list, name='courses_list'),
    path('courses/<slug:slug>/', views.course_detail, name='course_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
