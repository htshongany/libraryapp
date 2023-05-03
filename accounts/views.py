from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):

    if request.method =='POST': 
        # Get the username and password from the request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Try to authenticate the user
        user = authenticate(username=username, password=password)

        # If the user is authenticated, log them in and redirect to the home page
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('library:index')

        else:
            messages.error(request, 'The username or password is incorrect.')
            return redirect('accounts:login')

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('accounts:login')

def register_view(request):
    if request.method == 'POST':
        # Get the username, email, and password from the request
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate the username, email, and password
        if not username or not email or not password1 or not password2:
            messages.error(request, 'Please enter a username, email, and password.')
            return redirect('accounts:register')

        # Check if the username is already taken
        try:
            User.objects.get(username=username)
            messages.error(request, 'The username is already taken.')
            return redirect('accounts:register')
        except User.DoesNotExist:
            pass

        # Check if the email is already taken
        try:
            User.objects.get(email=email)
            messages.error(request, 'The email is already taken.')
            return redirect('accounts:register')
        except User.DoesNotExist:
            pass

        # Check if the passwords match
        if password1 != password2:
            messages.error(request, 'The passwords do not match.')
            return redirect('accounts:register')

        # Create a new user and Log the user in
        user = User.objects.create_user(username, email, password1)
        login(request, user)
        messages.success(request, 'You have successfully registered.')
        return redirect('library:index')
        
    return render(request, 'accounts/register.html')