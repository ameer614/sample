from django.db import models

class  Category(models.Model):
    name=models.CharField(max_length=60,unique=True)
    def __str__(self):
        return(self.name)
class Productmodel(models.Model):
    name=models.CharField(max_length=60,unique=True,null=False,blank=True)
    price=models.PositiveIntegerField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.TextField(null=True)
    image= models.ImageField(upload_to='product_photos', default='base.jpg')
    created_at=models.DateTimeField(auto_now_add=True)
    

    class Meta():
        db_table='product_table'

    def __str__(self):
        return(self.name)


