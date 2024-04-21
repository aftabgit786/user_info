from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserRegistrationForm, EducationalInfoForm


def index(request):
    return render(request, 'userinfo/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user including hashed password
            messages.success(request, f'Account created successfully for {user.email}!')
            return redirect('login')  # Redirect to a login page after successful registration
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()  # Initialize a blank form for GET requests

    return render(request, 'userinfo/register.html', {'form': form})


def user_login(request):
    # Initialize the counter on first access
    request.session.setdefault('failed_attempts', 0)

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['failed_attempts'] = 0  # Reset counter after successful login
                return redirect('profile')
            else:
                messages.error(request, 'Your account is not active.')
        else:
            messages.error(request, 'Invalid login credentials.')
            # Increment the failed login attempts counter
            request.session['failed_attempts'] += 1
            request.session.modified = True  # Ensure the session is saved

    return render(request, 'userinfo/login.html', {
        'failed_attempts': request.session['failed_attempts']
    })


@login_required  # Ensure only authenticated users can access the profile
def profile(request):
    return render(request, 'userinfo/profile.html', {'user': request.user})


@login_required
def add_education(request):
    if request.method == 'POST':
        form = EducationalInfoForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            education.user = request.user
            education.save()
            return redirect('profile')  # Redirect back to the profile page
    else:
        form = EducationalInfoForm()

    return render(request, 'userinfo/add_education.html', {'form': form})


def user_logout(request):
    logout(request)  # This will clear the session of the current request
    return redirect('home')  # Redirect to homepage or login page after logout
