from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from projects.models import Review, Project

def home_page(request):
    profiles = Profile.objects.all()
    return render(request, 'users/index.html', {'profiles': profiles})


def profile_detail(request, pk):
    profile = get_object_or_404(Profile, pk=pk)
    return render(request, 'users/profile.html', {'profile': profile})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            print('Login failed')

    return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            login(request, user)
            messages.success(request, "Ro‘yxatdan muvaffaqiyatli o‘tdingiz!")

            return redirect('home_page')
        else:
            messages.error(request, "Xatolik yuz berdi. Ma'lumotlarni tekshiring.")
    else:
        form = UserCreationForm()

    context = {'form': form}
    print(form.errors)
    return render(request, 'users/signup.html', context)


def signin(request):
    return render(request, 'users/login.html')


def forget_password(request):
    return render(request, 'users/forgetpassword.html')


@login_required(login_url='login')
def account(request):
    return render(request, 'users/account.html')


def single_project(request):
    return render(request, 'users/single-project.html')


def find_students(request):
    query = request.GET.get('text', '')
    profiles = Profile.objects.filter(name__icontains=query)
    return render(request, 'users/index.html', {'profiles': profiles, 'query': query})