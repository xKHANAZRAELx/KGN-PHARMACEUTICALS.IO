from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Product
from store.models.category import Category
from django.views import View
from django.contrib.auth import login as auth_login,logout as auth_logout,authenticate 
from store.forms import LoginForm 
from django.contrib import messages

# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')



    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    
    return render(request, 'index.html')

def htl1(request):
    products=Product.get_all_products1().order_by('-price')
    d={'products':products}
    return render(request,'CovidEssentials.html',d)

def lth1(request):
    products=Product.get_all_products1().order_by('price')
    d={'products':products}
    return render(request,'CovidEssentials.html',d)


def htl2(request):
    products=Product.get_all_products2().order_by('-price')
    d={'products':products}
    return render(request,'healthCproducts.html',d)

def lth2(request):
    products=Product.get_all_products2().order_by('price')
    d={'products':products}
    return render(request,'healthCproducts.html',d)

def htl3(request):
    products=Product.get_all_products3().order_by('-price')
    d={'products':products}
    return render(request,'personalcare.html',d)

def lth3(request):
    products=Product.get_all_products3().order_by('price')
    d={'products':products}
    return render(request,'personalcare.html',d)

def htl4(request):
    products=Product.get_all_products4().order_by('-price')
    d={'products':products}
    return render(request,'MensGrooming.html',d)

def lth4(request):
    products=Product.get_all_products4().order_by('price')
    d={'products':products}
    return render(request,'MensGrooming.html',d)

def htl5(request):
    products=Product.get_all_products5().order_by('-price')
    d={'products':products}
    return render(request,'makeup.html',d)

def lth5(request):
    products=Product.get_all_products5().order_by('price')
    d={'products':products}
    return render(request,'makeup.html',d)

class alogin(View):
    def get(self,request):
        form=LoginForm()
        d={'form':form}
        return render(request,'alogin.html',d)
    def post(self,request):
        fm=LoginForm(request.POST)
        if fm.is_valid():
            username=fm.cleaned_data['username']
            password=fm.cleaned_data['password']
        myuser=authenticate(username=username,password=password)
        if myuser is not None:
            auth_login(request,myuser)
            return redirect('users')
        else:
            messages.error(request,'Invalid Username or Password')
            return redirect('alogin')
        
def users(request):
    return render(request,'users.html')