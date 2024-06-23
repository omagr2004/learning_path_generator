from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,ProfileForm
from .models import LearningPath, Course, UserProgress



def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'core/login.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'core/profile.html')




@login_required
def update_profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'core/update_profile.html', {'form': form})



def home_view(request):
    return render(request, 'core/home.html')

# core/views.py
# core/views.py


# class CustomLogoutView(View):
#     def get(self, request):
#         logout(request)s
#         return redirect('home')

def learning_path_list_view(request):
    learning_paths = LearningPath.objects.all()
    return render(request, 'core/learning_path_list.html', {'learning_paths': learning_paths})

def learning_path_detail_view(request, pk):
    learning_path = get_object_or_404(LearningPath, pk=pk)
    return render(request, 'core/learning_path_detail.html', {'learning_path': learning_path})

def course_detail_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'core/course_detail.html', {'course': course})

@login_required
def update_progress_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    user_progress, created = UserProgress.objects.get_or_create(user=request.user, course=course)
    user_progress.completed = not user_progress.completed
    user_progress.save()
    return redirect('learning_path_detail', pk=course.learningpath_set.first().pk)
