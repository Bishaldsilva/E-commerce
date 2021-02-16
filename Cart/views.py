from django.shortcuts import render,redirect,get_object_or_404
from .models import Products,Cart
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.
catlist=[]
def home(request):
    allprods=[]
    prods=Products.objects.values('Category','id')
    catg={i['Category'] for i in prods}
    catlist.append(catg)
    for c in catg:
        prod=Products.objects.filter(Category=c)
        allprods.append(prod)
    return render(request,'Cart/index.html',{'allprods':allprods,'catg':catg})
def products(request,id):
    product = Products.objects.filter(id=id)
    return render(request, 'Cart/product.html', {'product': product[0]})
def cart(request):
    if request.user.is_authenticated:
        list=[]
        cart = Cart.objects.filter(user=request.user.first_name)
        for i in cart:
            if i.prod_id not in list:
                list.append(i.prod_id)
        num=int(request.POST['num'])
        if num not in list:
            crt=Cart(prod_id=num,user=request.user.first_name)
            crt.save()
        return redirect('/')
    else:
        messages.info(request,"You aren't logged in")
        return redirect('/')
def viewcart(request):
    if request.user.is_authenticated:
        c=0
        cart=Cart.objects.filter(user=request.user.first_name)
        product=Products.objects.all()
        for i in cart:
            for j in product:
                if j.id == i.prod_id:
                    c+=j.Price
        c=str(c)
        print(c)
        return render(request, 'Cart/cart.html',{'cart':cart,'product':product,'Price':c})
    else:
        messages.info(request, "You aren't logged in")
        return redirect('/')
def delete(request,id):
    obj=get_object_or_404(Cart,id=id)
    obj.delete()
    return redirect('viewcart')
def category(request):
    cat=request.POST['c1']
    prod=Products.objects.filter(Category=cat)
    return render(request,'Cart/category.html',{'prod':prod,'catg':catlist[0]})
def golog(request):
    return render(request, 'Cart/login.html')
def goreg(request):
    return render(request, 'Cart/reg.html')
def reg(request):
    fn=request.POST['fn']
    ln = request.POST['ln']
    un = request.POST['un']
    email = request.POST['em']
    pass1 = request.POST['ps1']
    pass2 = request.POST['ps2']
    if pass1==pass2:
        if User.objects.filter(username=un).exists():  #checking the existence of user
            messages.info(request,'Username taken')
            return redirect('/goreg')
        else:
            user = User.objects.create_user(username=un, password=pass1, email=email, first_name=fn, last_name=ln)
            user.save()
    else:
        messages.info(request, 'Password dismatch')
        return redirect('/goreg')
    return redirect('/')
def login(request):
    un = request.POST['un']
    pass1 = request.POST['pass1']
    user = auth.authenticate(username=un,password=pass1)
    if user is not None:
        auth.login(request,user)
        return redirect('/')
    else:
        messages.info(request,'Invalid username or password')
        return redirect('/golog')
def logout(request):
    auth.logout(request)
    return redirect('/')