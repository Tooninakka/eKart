from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

# Creating Superuser
class MyAccountManager(BaseUserManager):
    def create_user(self, firstname, lastname, username, email, password=None):
        if not email:
            raise ValueError('User must have an email Address')
        if not username:
            raise ValueError('User must have Username')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            firstname = firstname,
            lastname = lastname,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, firstname, lastname, email, username, password, **extra_fileds):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            firstname=firstname,
            lastname=lastname,
            password=password,
            **extra_fileds,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user
    

# Creating Normal User            

class Account(AbstractBaseUser):
    firstname = models.CharField(max_length=100)
    lastname =models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50 , unique=True)
    phone_number = models.IntegerField(blank=True)
    
    # required fileds
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'lastname']
    
    objects = MyAccountManager()
    
    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
