from django.db import models
from category.models import Category
from django.urls import reverse
from accounts.models import Account
from django.db.models import Avg
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.IntegerField()
    image = models.ImageField(upload_to='photos/products',)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.product_name
    
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    
    # My way of avg rating  
    # def get_average_rating(self):
    #     all_rating = ReviewRating.objects.filter(product__id = self.id)
    #     all_rating_list= list(all_rating)
    #     summed_rating = 0.0
    #     for all_rating in all_rating_list:
    #         summed_rating += all_rating.rating
    #     average_rating = summed_rating / len(all_rating_list)
    #     return average_rating
    
    # Tutors way
    def averageReview(self):
        all_rating = ReviewRating.objects.filter(product = self,status = True).aggregate(average = Avg('rating'))
        avg = 0
        if all_rating['average'] is not None :
            avg = float(all_rating['average'])
        return avg

        # return all_rating['average']



    
class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(vatiation_category = 'color',is_active = True)
    def size(self):
        return super(VariationManager, self).filter(vatiation_category = 'size',is_active = True)
    
    
variation_categories_choice = (
    ('color', 'color'),
    ('size', 'size')
)

class Variation(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    vatiation_category = models.CharField(max_length=100 ,choices=variation_categories_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()


    def __str__(self):
        return self.variation_value

    
class ReviewRating(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    subject = models.CharField(blank=True,max_length=100)
    review = models.TextField(max_length=500,blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=50,blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
    
class ProductGallery(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default=None)
    image = models.ImageField(upload_to='store/products',max_length=245)

    def __str__(self):
        return self.product.product_name
    
    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'product gallery'
    
        


