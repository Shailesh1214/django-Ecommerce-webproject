from django.db import models

# Product model
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length =50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

# Contact model
class Contact(models.Model):
    msg_id = models.AutoField(primary_key =True)
    name = models.CharField(max_length =70)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.IntegerField(default=0)
    desc = models.CharField(max_length=500,default="")
    

# method overriding
    def __str__(self):
        return self.name

