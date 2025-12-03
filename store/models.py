
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField


class UserProfile(AbstractUser):
    age = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(70)],
        null=True, blank=True
    )
    phone_number = PhoneNumberField(null=True, blank=True)
    avatar = models.ImageField(upload_to="user_images/", null=True, blank=True)

    StatusChoices = (
        ('gold', 'Gold'),
        ('silver', 'Silver'),
        ('bronze', 'Bronze'),
        ('simple', 'Simple'),
    )
    status = models.CharField(max_length=30, choices=StatusChoices, default='simple')
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    category_image = models.ImageField(upload_to='category_photo')
    category_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    sub_category_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")

    def __str__(self):
        return self.sub_category_name


class Product(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="products")
    product_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    article_number = models.PositiveIntegerField(unique=True, verbose_name='Article')
    description = models.TextField()
    product_type = models.BooleanField()
    video = models.FileField(upload_to='video_photo')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name


class ProductImage(models.Model):
    product_image = models.ImageField(upload_to='product_image/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f'{self.product} — {self.product_image}'


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="reviews")
    stars = models.PositiveSmallIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} — {self.stars}'

class Cart(models.Model):
     user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

class CartItem(models.Model):
     cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     quantity = models.PositiveSmallIntegerField(default=1)
