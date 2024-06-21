from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home_view, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.update_profile_view, name='update_profile'),
    path('', views.learning_path_list_view, name='learning_path_list'),
    path('learning_path/<int:pk>/', views.learning_path_detail_view, name='learning_path_detail'),
    path('course/<int:pk>/', views.course_detail_view, name='course_detail'),
    path('course/<int:pk>/update_progress/', views.update_progress_view, name='update_progress'),
    
]


