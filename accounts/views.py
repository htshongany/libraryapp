from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

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