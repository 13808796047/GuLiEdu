from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .models import UserProfile
from django.db.models import Q


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        user_register_form = UserRegisterForm(request.POST)
        if user_register_form.is_valid():
            email = user_register_form.cleaned_data['email']
            password = user_register_form.cleaned_data['password']
            user_list = UserProfile.objects.filter(Q(username=email) | Q(email=email))
            if user_list:
                return render(request, 'register.html', {
                    'msg': '用户已经存在！'
                })
            else:
                user = UserProfile()
                user.username = email
                user.set_password(password)
                user.email = email
                user.save()
                return redirect('index')
        else:
            return render(request, 'register.html', {'user_register_form': user_register_form})

# def login(request):
#     pass