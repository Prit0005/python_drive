from django.shortcuts import render,redirect
from .models import User,Product,Wishlist
import requests
import random

# Create your views here.
def index(request):
    try:
        user=User.objects.get(email=request.session['email'])
        if user.usertype=='buyer':
            return render(request,'index.html')
        else:
            return render(request,'seller-index.html')
    except:
        return render(request,'index.html')
    


def contact(request):
    return render(request,'contact.html')

def product(request):
    products=Product.objects.all()
    return render(request,'product.html',{'products':products})

def shoping_cart(request):
    return render(request,'shoping-cart.html')

def blog(request):
    return render(request,'blog.html')

def about(request):
    return render(request,'about.html')

def signup(request):
    if request.method=="POST":
        try:
            User.objects.get(email=request.POST['email'])
            msg='email already registered'  
            return render(request,'login.html',{'msg':msg})
        except:
            if request.POST['password']==request.POST['cpassword']:
                User.objects.create(
                    fname=request.POST['fname'],
                    lname=request.POST['lname'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address'],
                    password=request.POST['password'],
                    profile_picture=request.FILES['profile_picture'],
                    usertype=request.POST['usertype']
                )
                msg='user registered sucessfully'
                return render(request,'login.html',{'msg':msg})
            else:
                msg='password and confirm password not matched'
                return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')
        
def login(request):
    if request.method=="POST":
        try:
            user=User.objects.get(email=request.POST['email'])
            if user.password==request.POST['password']:
                request.session['email']=user.email
                request.session['fname']=user.fname
                request.session['profile_picture']=user.profile_picture.url
                wishlists=Wishlist.objects.filter(user=user)
                request.session['wishlist_count']=len(wishlists)    
                if user.usertype=="buyer":
                    return render(request,'index.html')
                else:
                    return render(request,'seller-index.html')
            else:
                msg="Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        except Exception as e:
            print(e)
            msg="Email Not Registered"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')
    
def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        del request.session['profile_picture']
        msg='user logout sucessfull'
        return render(request,'login.html',{'msg':msg})
    except:
        msg='user logout sucessfull'
        return render(request,'login.html',{'msg':msg})
        
def profile(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.mobile=request.POST['mobile']
        user.address=request.POST['address']
        try:
            user.profile_picture=request.FILES['profile_picture']
        except:
            pass
        user.save()
        request.session['profile_picture']=user.profile_picture.url
        msg='profile update sucessfully'
        if user.usertype=="buyer":
            return render(request,'profile.html',{'user':user})
        else:
            return render(request,'seller-profile.html',{'user':user})
    else:
        if user.usertype=="buyer":
            return render(request,'profile.html',{'user':user})
        else:
            return render(request,'seller-profile.html',{'user':user})
    
def change_password(request):
    user=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        if user.password==request.POST['old_password']:
            if request.POST['new_password']==request.POST['cnew_password']:
                if request.POST['old_password']!=request.POST['new_password']:
                    user.password=request.POST['new_password']
                    user.save()
                    del request.session['email']
                    del request.session['fname']
                    del request.session['profile_picture']
                    msg="Password Changed Successfully"
                    return render(request,'login.html',{'msg':msg})
                else:
                    msg="Old Password & New Password Can't Be Same"
                    if user.usertype=="buyer":
                        return render(request,'change-password.html',{'msg':msg})
                    else:
                        return render(request,'seller-change-password.html',{'msg':msg})
            else:
                msg="New Password & Confirm New Password Does Not Matched"
                if user.usertype=="buyer":
                    return render(request,'change-password.html',{'msg':msg})
                else:
                    return render(request,'seller-change-password.html',{'msg':msg})
        else:
            msg="Old Password Does Not Matched"
            if user.usertype=="buyer":
                return render(request,'change-password.html',{'msg':msg})
            else:
                return render(request,'seller-change-password.html',{'msg':msg})
    else:
        if user.usertype=="buyer":
            return render(request,'change-password.html')
        else:
            return render(request,'seller-change-password.html')


def forgot_password(request):
    if request.method=="POST":
        try:
            user=User.objects.get(mobile=request.POST['mobile'])
            mobile=request.POST['mobile']
            otp=str(random.randint(1000,9999))
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {"authorization":"l7r1fEQqshvmyiMg3AtDPNZ8XKpVuUaB6HRdCxbI4G95zcJTekqYj43mlJTgieZ9HUNy27XMK5cob6Lr","message":"OTP "+otp,"language":"english","route":"q","numbers":mobile}
            headers = {'cache-control': "no-cache"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
            print("OTP:",otp)
            request.session['otp']=otp
            request.session['mobile']=mobile
            return render(request,'otp.html')           
        except:
            msg="Mobile Number Not Registered"
            return render(request,'forgot_password.html',{'msg':msg})
    else:
        return render(request,'forgot_password.html')

def verify_otp(request):
    otp1=str(request.POST['otp'])
    otp2=str(request.session['otp'])

    if otp1==otp2:
        del request.session['otp']
        return render(request,'new_password.html')
    else:
        msg='invalid otp'
        return render(request,'otp.html',{'msg':msg}) 


def new_password(request):
    if request.POST['new_password']==request.POST['cnew_password']:
        user=User.objects.get(mobile=request.session['mobile'])
        user.password=request.POST['new_password']
        del request.session['mobile']
        user.save()
        msg='password Updated Successfully'
        return render(request,'login.html',{'msg':msg})
    else:
        msg="new password and confirm password doesn't Matched"
        return render(request,'new-password.html',{'msg':msg})

def seller_add_product(request):
    seller=User.objects.get(email=request.session['email'])
    if request.method=="POST":
        Product.objects.create(
            seller=seller,
            product_category=request.POST['product_category'],
            product_price=request.POST['product_price'],
            product_name=request.POST['product_name'],
            product_desc=request.POST['product_desc'],
            product_image=request.FILES['product_image'],
            )
        msg='Product add sucessfull'
        return render(request,'seller-add-product.html',{'msg':msg})
    else:
        return render(request,'seller-add-product.html')

def seller_view_product(request):
    seller = User.objects.get(email=request.session['email'])
    products = Product.objects.filter(seller=seller)
    
    return render(request, 'seller-view-product.html', {'products': products})


def seller_product_detail(request,pk):
    product=Product.objects.get(pk=pk)

    return render(request,'seller-product-detail.html',{'product':product})

def product_details(request,pk):
    wishlist_flag=False
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    try:
        Wishlist.objects.get(user=user,product=product)
        wishlist_flag=True
    except:
        pass
    return render(request,'product-detail.html',{'product':product,'wishlist_flag':wishlist_flag})

def seller_edit_product(request,pk):
    product=Product.objects.get(pk=pk)
    if request.method=='POST':
        product.product_category=request.POST['product_category']
        product.product_name=request.POST['product_name']
        product.product_price=request.POST['product_price']
        product.product_desc=request.POST['product_desc']
        try:
            product.product_image=request.FILES['product_image'] 
        except:
            pass
        product.save()
        msg='Product update sucessfully'           
        return render(request,'seller_edit_product.html',{'product':product ,'msg':msg})
    else:
        return render(request,'seller_edit_product.html',{'product':product})

def seller_delete_product(request,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    return redirect('seller-view-product')

  
def add_to_wishlist(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    Wishlist.objects.create(user=user,product=product)
    return redirect('wishlist')

def wishlist(request):
    user = User.objects.get(email=request.session['email'])
    wishlists = Wishlist.objects.filter(user=user)
    request.session['wishlist_count']=len(wishlists)
    return render(request, 'wishlist.html', {'wishlists': wishlists})

def remove_wishlist(request,pk):
    product=Product.objects.get(pk=pk)
    user=User.objects.get(email=request.session['email'])
    wishlist=Wishlist.objects.get(user=user,product=product)
    wishlist.delete()
    return redirect('wishlist')

