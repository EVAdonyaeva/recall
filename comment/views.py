from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from comment.models import Post
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib.auth.models import User


def auth_decorator(fn):
    def wrapper(request):
        if request.user.is_authenticated:
            return fn(request)
        else:
            return redirect('main_page')
    return wrapper


def main_page(request):
    return render(request, 'comment/signin_form_main_page.html', {})


def signup_page(request):
    return render(request, 'comment/signup_form_main_page.html', {})



def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)
    else:
        return HttpResponse(status=405)


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return HttpResponse(status=401)
        user = User.objects.create_user(username=username, email=email, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)
    else:
        return HttpResponse(status=405)


def signout(request):
    logout(request)
    return redirect('main_page')


@auth_decorator
def post_comment_form(request):
    return render(request, 'comment/comment_form.html', {})


@auth_decorator
def post_send(request):
    message = request.POST.get('message', '')
    email = request.POST.get('email', '')
    if message and email:
        try:
            send_mail('Recall', message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER, email])
            status = 'Email has been sent successfully.'
        except BadHeaderError:
            status = HttpResponse('Invalid header found.')
    else:
        status = 'Make sure all fields are entered and valid.'
    user = request.user
    post = Post.objects.create(email=email, text=message, author=user, send_status=status)
    return render(request, 'comment/comment_form.html', {'status': status})


