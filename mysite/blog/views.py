from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

posts =[
    {
        'author' : 'blogger',
        'title' : 'first blog 1',
        'content' : "first blog's first content",
        'datetime' : "27 august, 2019"
    },
    {
        'author' : 'blogger800',
        'title' : 'first blog 2',
        'content' : "first blog's seecond content",
        'datetime' : "29 august, 2019"
    },
    {
        'author' : 'blogger',
        'title' : 'first blog 1',
        'content' : "first blog's first content",
        'datetime' : "27 august, 2019"
    },
    {
        'author' : 'blogger800',
        'title' : 'first blog 2',
        'content' : "first blog's seecond content",
        'datetime' : "29 august, 2019"
    },
    {
        'author' : 'blogger',
        'title' : 'first blog 1',
        'content' : "first blog's first content",
        'datetime' : "27 august, 2019"
    },
    {
        'author' : 'blogger800',
        'title' : 'first blog 2',
        'content' : "first blog's seecond content",
        'datetime' : "29 august, 2019"
    },
    {
        'author' : 'blogger',
        'title' : 'first blog 1',
        'content' : "first blog's first content",
        'datetime' : "27 august, 2019"
    },
    {
        'author' : 'blogger800',
        'title' : 'first blog 2',
        'content' : "first blog's seecond content",
        'datetime' : "29 august, 2019"
    },
    {
        'author' : 'blogger',
        'title' : 'first blog 1',
        'content' : "first blog's first content",
        'datetime' : "27 august, 2019"
    },
    {
        'author' : 'blogger800',
        'title' : 'first blog 2',
        'content' : "first blog's seecond content",
        'datetime' : "29 august, 2019"
    },
    {
        'author' : 'blogger',
        'title' : 'first blog 1',
        'content' : "first blog's first content",
        'datetime' : "27 august, 2019"
    },
    {
        'author' : 'blogger800',
        'title' : 'first blog 2',
        'content' : "first blog's seecond content",
        'datetime' : "29 august, 2019"
    },
    {
        'author' : 'blogger',
        'title' : 'first blog 1',
        'content' : "first blog's first content",
        'datetime' : "27 august, 2019"
    },
    {
        'author' : 'blogger800',
        'title' : 'first blog 2',
        'content' : "first blog's seecond content",
        'datetime' : "29 august, 2019"
    },
]


def home(request):
    context = {
        'posts' : posts,
        'title' : "home"
    }
    return render(request,'blog/home.html',context)


def about(request):
    return render(request,'blog/about.html',{'title' : 'about'})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.success(request, f"New account created: {username}")
            return redirect("main:home")


        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "blog/register.html",
                          context={"form":form})
    form = UserCreationForm
    return render(request,'blog/register.html',{'form':form })

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:home")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "blog/login.html",
                  context={"form":form})
