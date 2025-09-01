from django.shortcuts import redirect, render
from .models import Profile 
from .forms import UserForm , ProfileForm , UserCreateForm
from property.models import Property ,PropertyBook
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import AddList ,AddCategory, AddPlace
from django.http import JsonResponse

def signup(request):
    if request.method == 'POST':
        signup_form = UserCreateForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            # return redirect(reverse('login'))
            username = signup_form.cleaned_data['username']
            password = signup_form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect(reverse('accounts:profile'))
    
    else:
        signup_form = UserCreateForm()

    return render(request,'registration/signup.html',{'signup_form':signup_form})



def profile(request):
    profile , created = Profile.objects.get_or_create(user = request.user)
    return render(request,'profile/profile.html',{'profile':profile})



def profile_edit(request):
    profile , created = Profile.objects.get_or_create(user = request.user)
    if request.method == 'POST':
        user_form = UserForm(request.POST , instance=request.user)
        profile_form = ProfileForm(request.POST , request.FILES , instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            my_form = profile_form.save(commit=False)
            my_form.user = request.user
            my_form.save()
            messages.success(request, 'Profile details updated.')
            return redirect(reverse('accounts:profile'))
    
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance = profile)       

    return render(request,'profile/profile_edit.html',{
        'user_form' : user_form , 
        'profile_form' : profile_form
    })


def my_reservations(request):
    my_reservations = PropertyBook.objects.filter( user = request.user )
    return render(request,'profile/my_reservations.html',{'my_reservations' : my_reservations})

def my_list(request):
    my_list = Property.objects.filter(owner = request.user)
    return render(request,'profile/my_list.html',{'my_list' : my_list})


def add_list(request):
    if request.method == 'POST':
        form = AddList(request.POST,request.FILES)
        if form.is_valid():
            form.instance.owner = request.user
            form.save()
            return redirect(reverse('accounts:list'))
    
    else:
        form = AddList()

    category_form = AddCategory()
    place_form = AddPlace()

    return render(request, "profile/add_list.html", {
        "form": form,
        "category_form": category_form,
        "place_form": place_form,
    })

def add_category(request):
    if request.method == "POST":
        form = AddCategory(request.POST)
        if form.is_valid():
            category = form.save()
            return JsonResponse({
                "id": category.id,
                "name": category.name
            })
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

def add_place(request):
    if request.method == "POST":
        form = AddPlace(request.POST, request.FILES)
        if form.is_valid():
            place = form.save()
            return JsonResponse({
                "id": place.id,
                "name": place.name
            })
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)



