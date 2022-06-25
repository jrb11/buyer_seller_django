# from urllib.request import Request
# from django.shortcuts import render,redirect,HttpResponse
# from .models import *
# from django.contrib.auth import login, logout, authenticate
# from django.contrib.auth.models import User
# from django.contrib import auth
# from datetime import datetime
# from django.contrib import messages


# # Create your views here.
# def index(request):
#     return render(request, 'index.html')


# #---------------------------------- User Details Registration -----------------------------------------
# def user_details_registration(request):
#     print("----- In User Details ------")
    
#     if request.method == 'POST':

#         #Users Details
#         First_Name = request.POST['First_Name']
#         Last_Name = request.POST['Last_Name']
#         #Date_of_Birth = request.POST['Date_of_Birth']
#         Email_ID = request.POST['Email_ID']
#         #Mobile_No = request.POST['Mobile_No']
#         #Balance = request.POST['Balance']
#         Password = request.POST['Password']
#         #Address = request.POST['Address']


#         #Users Role
#         Users_Role = request.POST['Users_Role']
#         print('------- Users_Role From HTML---------', Users_Role)

#         print("Data Enter")

#         #db_email_id = User_Details.objects.filter(Email_ID=Email_ID).exists()
#         #print('Received Email ID---------', db_email_id)

#         if User_Details.objects.filter(Email_ID=Email_ID).exists():
#             messages.error(request,'Email ID already exists')
#             print('Email ID already exists')
#             return redirect('user_details_registration')


  
#         # Buyer
#         user_role_get = User_Role.objects.get(Role_Name=Users_Role) 
#         print(user_role_get)

#         # Seller
#         # user_role_get_seller = User_Role.objects.get(Role_ID=2) 
#         # print(user_role_get_seller)

#         # qs_1= User_Role.objects.values_list('Role_ID', 'Role_Name')
#         # print(qs_1)
#         # #print(qs_1.query)
#         # print(qs_1[0]) ------ (1, 'Buyer')
#         # print(qs_1[1]) ------ (2, 'Seller')


#         #print(user_role_get)
#         #print("----- user_role_Data ------", user_role_get)




#         # for i in user_role_get:
#         #     print(i.Role_Name)
#         #     #print(user_role_get.Roll_Name)

#         # if user_role_get.Roll_Name == 'Buyer':
#         #     print('User Role : Buyer ............')
#         # if user_role_get.Roll_Name == 'Seller':
#         #     print('User Role : Seller ............')
#         # else:
#         #     pass

       
#         # user_role_create = User_Role.objects.create(Role_Name=Role_Name)
#         # user_role_create.save()
#         # print("----------- user_role_create ------------")


#         user_details = User_Details.objects.create(First_Name=First_Name, Last_Name=Last_Name, Email_ID=Email_ID, Password=Password, Users_Role=user_role_get)

#         ## ---------- Note ----------- ##
#         ##Users_Role is Foreign KEY from User_Role, So pass object in this field for Users_Role not a value


#         #print("blog image: ",user.image)
#         user_details.save()
      

#         print(user_details)
		       
		
#         print('----------------------------------- User Details Created --------------------------------')
		
#         return redirect('user_details_view')
        
#     else:
#         return render(request, 'user_details_registration.html')


# #---------------------------------- User Detaisl View  -----------------------------------------

# def user_details_view(request):

#     if 'email' in request.session:
#         email = request.session['email']
#         user_obj = User_Details.objects.filter(Email_ID=email).first()

        
#         return render(request, 'user_details_view.html',{'user_data':user_obj})

#     else:
#         return redirect('login')

#     # return render(request, 'login.html')

#     # print("----- In User View ------")
#     # user_data = User_Details.objects.all()
    
#     # print("----------------------------- User Details View ------------------------------",user_data)
#     # return render(request,'user_details_view.html',{'user_data':user_data})



# #---------------------------------- User Login --------------------------------------------------

# def user_login(request):
    
#     if request.method == 'POST':
#         Email_ID = request.POST['Email_ID']
#         Password = request.POST['Password']

#         user = User_Details.objects.filter(Email_ID=Email_ID, Password=Password).first()
#         print('----------user object ----------------------------------------------------', user)
#         request.session['email'] = Email_ID

#         if user is not None:

#             messages.success(request,'Successfully Login')
#             print('Successfully Login')

#             #print(user.values())
#             a = User_Role.objects.filter(Role_ID=user.Users_Role_id).first()
#             #print(a.Role_Name)

#             if a.Role_Name == 'Seller':
#                 print("--------------------------- Your are Seller -----------------")
#                 print('----------user object ----------------------------------------', user)
#                 #return render(request, 'product_registration.html', {'user_obj':user_obj})
#                 return redirect('product_registration')

#             else:
#                 print("--------------------------- Your are Buyer ----------------")


#         else:
#             messages.error(request, 'Wrong Email or Password')
#             print('Wrong Email or Password')
#             return render(request, 'user_login.html')
    
#     else:
#         return render(request, 'user_login.html')
        



       

#             # #Retrieve Users_Role Data from User_Details ..............
#             # users_role_data = User_Details.objects.all()
            
#             # for s in users_role_data:
#             #     print('-------------- User Role Data-----------',s.Users_Role_id)

#             # #Retrieve only 'seller' Data from User_Details ..............
#             # for s in users_role_data:
#             #     if s.Users_Role_id == 2:
#             #         print('-------------- Only Seller Data---------------', s.Users_Role)
            
# # Get only 'Seller' Data from User_Details from DB --------------------------------------



#             # seller_obj = User_Details.objects.get(Users_Role_id=2)
#             # print(seller_obj.Users_Role)

#             # buyer_obj = User_Details.objects.filter(Users_Role='Buyer')
#             # print(buyer_obj)
            
#             #return redirect('user_details_view')
        
# #---------------------------------- User Login --------------------------------------------------

# def user_logout(request):
#     logout(request)
#     print('----------------------------------- User Logout --------------------------------')
#     return redirect('user_login')





# #---------------------------------- Product Details Registration ------------------------------------

# def product_registration(request):

#     #if request.session.has_key('user_obj'):
#         if request.method == 'POST':

#             Product_Name = request.POST['Product_Name']
#             Product_Image = request.FILES['Product_Image']
#             Create_Date = request.POST['Create_Date']
#             Created_By_User = request.POST['Created_By_User']

#             print(Created_By_User)
            


#             product_user_get = User_Details.objects.get(First_Name=Created_By_User) 
#             print(product_user_get)


#             product = Product.objects.create(Product_Name=Product_Name, Product_Image=Product_Image, Create_Date=Create_Date, Created_By_User=product_user_get)
#             product.save()

#             print('----------------------------------- Product Created --------------------------------')
#         else:

#             return render(request, 'product_registration.html' )
#     #else:

#     #    return render(request, 'user_login.html' )


# #---------------------------------- Product Details View ------------------------------------


# def product_view(request):

#     print("----- In User View ------")
#     product_data = Product.objects.all()
    
#     print("----------------------------- Product Details View ------------------------------",product_data)
#     return render(request,'product_view.html',{'product_data':product_data})




