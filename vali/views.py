from django.shortcuts import render,HttpResponse,redirect
from .models import Productmodel,Category
from .forms import Mform
# Create your views here.
def home(request):
    return render(request,'index.html')
def test(request):
    return render(request,'test.html')


def web(request,category=None):
    if category:
        products=Productmodel.objects.filter(category__id= category)
    else:
        products = Productmodel.objects.all()
    categories = Category.objects.all()
    context={
        'products': products,
        'categories':categories
    }
    return render(request,'table_display.html',context)

def create_prodect(request):
    if request.method == 'POST':
        form=Mform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            if obj.price>1000:
                obj.price=obj.price-100
            obj.save()  
            return redirect('/')
        else:
            return render(request,'create_form.html',{'form':form})
    else:
        form = Mform()
        return render(request,'create_form.html',{'form':form})

def update_prodect(request,id):
    productt = Productmodel.objects.get(id=id)
    if request.method == 'POST':
        form=Mform(request.POST, instance=productt)
        if form.is_valid():
            obj=form.save(commit=False)
            if obj.price>1000:
                obj.price=obj.price-100
            obj.save()  
            return redirect('/vali/web/')
        else:
            return render(request,'update_form.html',{'form':form})
    else:
        form = Mform(instance=productt)
        return render(request,'update_form.html',{'form':form})

def delete_product(request,id):
    product=Productmodel.objects.get(id=id)
    product.delete()
    return redirect('/vali/web/')