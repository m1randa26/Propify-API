from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Create your models here.
class User(models.Model):
    
    # Definition of user types
    class UserRoles(models.TextChoices):
        OWNER = 'OWR', 'Owner'
        USER = 'USR', 'User'
    
    class Gender(models.TextChoices):
        MALE = 'MALE', 'Male'
        FEMALE = 'FEMALE', 'Female'
    
    # AutoField -> Auto increment value
    user_id = models.AutoField(primary_key=True)
    role = models.CharField(
        max_length=3,
        choices=UserRoles.choices,
        default=UserRoles.USER,
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=6,
        choices=Gender.choices,
    )
    age = models.IntegerField()
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=128)
    
    # Password Hashing
    def save(self, *args, **kwargs):
        if self._state.adding or self.password != User.objects.get(pk=self.pk).password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
    picture_profile = models.URLField()
    registration_date = models.DateField(auto_now_add=True)
    location = models.CharField(max_length=80)
    
class Property(models.Model):
    
    class Currency(models.TextChoices):
        MXN = 'MXN', 'Mxn'
        USD = 'USD', 'Usd'
        EUR = 'EUR', 'Eur'
    
    property_id = models.AutoField(primary_key=True)
    rooms = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency_type = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.MXN,
    )
    period = models.CharField(max_length=30)
    availability = models.BooleanField(default=True)
    reserved = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='properties')
    
class RentalHistory(models.Model):
    
    rent_id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    
    def clean(self):
        if self.end_date < self.start_date:
            raise ValidationError('End date cannot be before start date')
    
    review = models.CharField(max_length=255)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(5.0)]
    )
    property_rent = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)