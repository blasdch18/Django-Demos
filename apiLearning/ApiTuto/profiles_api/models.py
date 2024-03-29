from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    """manager para perfiles de usuario """
    def create_user(self,email, name, password=None):
        """"crear nuevo user profile"""
        if not email:
            raise ValueError('Usuario debe tener un email')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        user= self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """"modelo de base de datos para usuario en el sistema"""
    email= models.EmailField(max_length=225, unique=True)
    name= models.CharField(max_length=255)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)

    objects= UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """obtener nombre completo"""
        return self.name

    def get_short_name(self):
        """"obtener nombre corto del usuario"""
        return self.name    

    def __str__(self):
        """representando nuestro usuario """
        return self.email