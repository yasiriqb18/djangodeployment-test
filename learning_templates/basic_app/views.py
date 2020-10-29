from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

#
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse 
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("you are logged in Nice" )

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        profile_form = UserProfileInfoForm(data = request.POST)

        if user_form.is_valid and profile_form.is_valid():
            #save user to the database
            user = user_form.save()
            # using set_password to hash the password
            user.set_password(user.password)
            #update the with the hashed password
            user.save()

            profile = profile_form.save(commit = False)

            profile.user = user

            if 'profile_pic' in request.FILES: #  the file through FILES object 
                
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/register.html', { 'user_form':user_form,
                            'profile_form': profile_form, 
                            'register':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user: #check for user
            if user.is_active: #if account is active
                #log the user in
                login(request,user)

                return HttpResponseRedirect(reverse('index')) #semd the user back to main page.

            else: #if account is not active
                return HttpResponseRedirect("account not active")
        else: 
            print("someone tried to login and failded!")
            #print("username: {} and password ".format(username,password))
            return HttpResponse("invalid login detial")
    else:
        #nothing has been provided. 
        return render(request,'basic_app/login.html', {})
