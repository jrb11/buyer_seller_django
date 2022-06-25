from enum import Flag
from django.db import models

# Create your models here.
class User_Role(models.Model):
    Role_ID = models.AutoField(primary_key=True)
    Role_Name = models.CharField(max_length=20, null=True)
    Role = models.ManyToOneRel(field = "Role", field_name = "Role", to = "Users_Role")
    #Role_Description = models.CharField(max_length=200, null=True)

    def __str__(self):      
        return self.Role_Name


class User_Details(models.Model):
    User_ID = models.AutoField(primary_key=True)
    First_Name = models.CharField(max_length=20, null=True)
    Last_Name = models.CharField(max_length=20, null=True)
    #Date_of_Birth = models.DateField(null=True)
    Email_ID = models.EmailField(null=True)
    #Mobile_No = models.CharField(max_length=10, null=True)
    #Balance = models.PositiveIntegerField(null=True)
    Password = models.CharField(max_length=20, null=True)
    #Address = models.CharField(max_length=20, null=True)
    Users_Role = models.ForeignKey(User_Role, on_delete=models.CASCADE)
    User_Product = models.ManyToOneRel(field = "User_Product", field_name = "User_Product", to = "Created_By_User")
    

    def __str__(self):      
        return self.First_Name


class Product(models.Model):
    Product_ID = models.AutoField(primary_key=True)
    Product_Name = models.CharField(max_length=20, null=True)
    Product_Image = models.ImageField(upload_to='products',blank=True, null=True)
    #Product_Sell_Price = models.PositiveIntegerField(null=True)
    #Product_Cost_Price = models.PositiveIntegerField(null=True)
    #Stock_Unit = models.SmallIntegerField(null=True)
    Created_By_User = models.ForeignKey(User_Details, on_delete=models.CASCADE)
    Create_Date = models.DateField(auto_created=True, null=True)
    #IS_Deleted = models.BooleanField()   # True if it has 1 as value, and 0 for False

    def __str__(self):      
        return self.Product_Name


# class User_Purchase(models.Model):
#     Purchase_ID = models.AutoField(primary_key=True)
#     Purchase_Date = models.DateField(auto_created=True, null=True)
#     Product_ID = models.ForeignKey(Product, on_delete=models.CASCADE)
#     Total_Unit = models.SmallIntegerField(null=True)
#     Purchase_By_User = models.ForeignKey(User_details, related_name='Purchase_By_User', on_delete=models.CASCADE)
#     Purchase_From_User = models.ForeignKey(User_details, related_name='Purchase_From_User', on_delete=models.CASCADE)

#     def __str__(self):      
#         return self.Purchase_Date