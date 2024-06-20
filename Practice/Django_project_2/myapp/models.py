from django.db import models
from django.utils  import timezone
# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    mobile=models.PositiveBigIntegerField()
    address=models.TextField()
    password=models.CharField(max_length=100)
    profile_picture=models.ImageField(upload_to='profile_picture/')
    usertype=models.CharField(max_length=100,default="buyer")
    
    
    def __str__(self) :
        return self.fname+''+self.lname
    
class Product(models.Model):

    category=(
        ('men','men'),
        ('women','women'),
        ('kids','kids')


        )
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    product_category=models.CharField(max_length=100,choices=category)
    product_name=models.CharField(max_length=100)
    product_price=models.PositiveBigIntegerField()
    product_desc=models.TextField()
    product_image=models.ImageField(upload_to='product_image/')

    def __str__(self):
        return self.seller.fname+"-"+self.product_name


class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.fname+" - "+self.product.product_name

