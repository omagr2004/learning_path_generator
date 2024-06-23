from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home_view, name='home'),  # This should be the only path with the empty string
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),# Using built-in LogoutView
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.update_profile_view, name='update_profile'),
    path('learning_paths/', views.learning_path_list_view, name='learning_path_list'),  # Changed path to avoid conflict
    path('learning_path/<int:pk>/', views.learning_path_detail_view, name='learning_path_detail'),
    path('course/<int:pk>/', views.course_detail_view, name='course_detail'),
    path('course/<int:pk>/update_progress/', views.update_progress_view, name='update_progress'),
]
