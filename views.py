from re import A
from urllib.request import Request
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import datetime
from django.contrib import messages


# Create your views here.
#------------------------------------------ Home Page -------------------------------------------------
def index(request):
    return render(request, 'index.html')


#---------------------------------- User Details Registration -----------------------------------------
def user_details_registration(request):
    print("----- In User Details ------")
    
    if request.method == 'POST':

        #Users Details
        First_Name = request.POST['First_Name']
        Last_Name = request.POST['Last_Name']
        #Date_of_Birth = request.POST['Date_of_Birth']
        Email_ID = request.POST['Email_ID']
        #Mobile_No = request.POST['Mobile_No']
        #Balance = request.POST['Balance']
        Password = request.POST['Password']
        #Address = request.POST['Address']


        #Users Role
        Users_Role = request.POST['Users_Role']
        print('------- Users_Role From HTML---------', Users_Role)

        print("Data Enter")

        if User_Details.objects.filter(Email_ID=Email_ID).exists():
            messages.error(request,'Email ID already exists')
            print('Email ID already exists')
            return redirect('user_details_registration')


  
        # Buyer_Seller_Role_Get
        user_role_get = User_Role.objects.get(Role_Name=Users_Role) 
        print(user_role_get)

        user_details = User_Details.objects.create(First_Name=First_Name, Last_Name=Last_Name, Email_ID=Email_ID, Password=Password, Users_Role=user_role_get)
        ## ---------- Note ----------- ##
        ##Users_Role is Foreign KEY from User_Role, So pass object in this field for Users_Role not a value
        user_details.save()
        print(user_details) 
	    
        print('----------------------------------- User Details Created --------------------------------')
		
        return redirect('user_details_view')
        
    else:
        return render(request, 'user_details_registration.html')


#---------------------------------- User Detaisl View  -----------------------------------------

def user_details_view(request):

    if 'email' in request.session:
        email = request.session['email']
        user_obj = User_Details.objects.filter(Email_ID=email).first()

        
        return render(request, 'user_details_view.html',{'user_data':user_obj})

    else:
        return redirect('user_login')


#---------------------------------- User Login --------------------------------------------------

def user_login(request):
    
    if request.method == 'POST':
        Email_ID = request.POST['Email_ID']
        Password = request.POST['Password']

        user_obj = User_Details.objects.filter(Email_ID=Email_ID, Password=Password).first()
        print('-------------------------- user object name :-----------------------', user_obj)
        request.session['email'] = Email_ID

        if user_obj is not None:

            messages.success(request,'Successfully Login')
            print('-------------------------- Successfully Login')

            #print(user.values())
            seller_obj= User_Role.objects.filter(Role_ID=user_obj.Users_Role_id).first()
            #print(a.Role_Name)

            if seller_obj.Role_Name == 'Seller':
                print("--------------------------- Your are Seller ------------------------")
                return redirect('product_view')

            else:
                print("--------------------------- Your are Not Seller --------------------")
                return render(request, 'user_login.html')


        else:
            messages.error(request, 'Wrong Email or Password')
            print('Wrong Email or Password')
            return render(request, 'user_login.html')
    
    else:
        return render(request, 'user_login.html')

        
#---------------------------------- User Login --------------------------------------------------

def user_logout(request):
    try:
        del request.session['email']
    except:
        return redirect('user_login')
    print('-------------------------- Successfully Logout')
    return redirect('user_login')
    

#---------------------------------- Product Details Registration ---------------------------------

def product_registration(request):

    #if request.session.has_key('user_obj'):
        if request.method == 'POST':

            Product_Name = request.POST['Product_Name']
            Product_Image = request.FILES['Product_Image']
            Create_Date = request.POST['Create_Date']
            Created_By_User = request.POST['Created_By_User']

            print(Created_By_User)
            
            product_user_get = User_Details.objects.get(First_Name=Created_By_User) 
            print(product_user_get)

            product = Product.objects.create(Product_Name=Product_Name, Product_Image=Product_Image, Create_Date=Create_Date, Created_By_User=product_user_get)
            product.save()

            print('-------------------------- Product Created ------------------------------')
            return redirect('product_view')

        else:
            return render(request, 'product_registration.html')
    #else:

    #    return render(request, 'user_login.html' )


#---------------------------------- Product Details View ------------------------------------


def product_view(request):

    print("----- In User View ------")
    product_data = Product.objects.all().order_by('Created_By_User')
    #product_data_user = Product.objects.filter(First_Name=request.Created_By_User)
    #print(product_data_user)

    Email = request.session.get('email')
    print('Session Get Data------',Email)
    login_user_obj = User_Details.objects.filter(Email_ID=Email).first()
    print('login_user_obj--------',login_user_obj)
    user_product_obj = Product.objects.filter(Created_By_User_id=login_user_obj.User_ID)
    print('product_obj-----------',user_product_obj)
    
    print("------------------------ Product Details View ----------------------",user_product_obj)
    return render(request,'product_view.html',{'product_data':user_product_obj})




