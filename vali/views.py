from django.shortcuts import render, HttpResponse, redirect
from .models import Productmodel, Category
from .forms import Mform, Create_user
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
from django.contrib.auth import login, authenticate, logout


def home(request):
    return render(request, "index.html")


def test(request):
    return render(request, "test.html")


def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            return render(request, "create_form.html", {"form": form})
    else:
        form = UserCreationForm()
        return render(request, "create_form.html", {"form": form})


def web(request, category=None):
    if category:
        products = Productmodel.objects.filter(category__id=category)
    else:
        products = Productmodel.objects.all()
    categories = Category.objects.all()
    context = {"products": products, "categories": categories}
    return render(request, "table_display.html", context)


def create_prodect(request):
    if request.method == "POST":
        form = Mform(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            if obj.price > 1000:
                obj.price = obj.price - 100
            obj.save()
            return redirect("/")
        else:
            return render(request, "create_form.html", {"form": form})
    else:
        form = Mform()
        return render(request, "create_form.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("/vali/login/")


def User_login(request):
    # form = Mform(instance=productt)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        obj = authenticate(username=username, password=password)
        if obj:
            login(request, obj)
            return redirect("/")
        else:
            return render(request, "user_login.html")
    return render(request, "user_login.html")


def update_prodect(request, id):
    productt = Productmodel.objects.get(id=id)
    if request.method == "POST":
        form = Mform(request.POST, instance=productt)
        if form.is_valid():
            obj = form.save(commit=False)
            if obj.price > 1000:
                obj.price = obj.price - 100
            obj.save()
            return redirect("/vali/web/")
        else:
            return render(request, "update_form.html", {"form": form})
    else:
        form = Mform(instance=productt)
        return render(request, "update_form.html", {"form": form})


def delete_product(request, id):
    product = Productmodel.objects.get(id=id)
    product.delete()
    return redirect("/vali/web/")
