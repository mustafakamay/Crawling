from django.db import models

# Create your models here.
class Crawlerr(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    sellingPrice = models.CharField(max_length=50,null=True,blank=True)
    discountedPrice = models.CharField(max_length=50,null=True,blank=True)
    category = models.CharField(max_length=200,null=True,blank=True)
    merchantName = models.CharField(max_length=100,null=True,blank=True)
    merchantCity = models.CharField(max_length=100,null=True,blank=True)
    merchantScore = models.CharField(max_length=100,null=True,blank=True)
    otherMerchantNames = models.TextField(null=True,blank=True)
    otherCityNames = models.TextField(null=True,blank=True)
    otherSellerScores = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name