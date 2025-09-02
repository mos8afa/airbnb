from django.shortcuts import redirect, render
from .models import Profile 
from .forms import UserForm , ProfileForm , UserCreateForm
from property.models import Property ,PropertyBook
from django.urls import reverse
from django.contrib import messages
from .forms import AddList ,AddCategory, AddPlace
from django.http import JsonResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        signup_form = UserCreateForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.is_active = False  
            user.save()

            current_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            activation_link = f"http://127.0.0.1:8000/accounts/activate/{uid}/{token}/"

            subject = 'Activate your account'
            message = f"Hi {user.username},\n\nPlease click the link below to activate your account:\n{activation_link}\n\nIf this email isn't yours, please ignore this message."
            send_mail(subject, message, None, [user.email], fail_silently=False)

            return render(request, 'registration/activation_sent.html', {'email': user.email})
    
    else:
        signup_form = UserCreateForm()

    return render(request,'registration/signup.html',{'signup_form':signup_form})

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user) 
        return render(request, 'registration/activation_success.html', {'user': user})
    else:
        return render(request, 'registration/activation_invalid.html')



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



