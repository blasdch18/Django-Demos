from django.contrib import admin
from profiles_api import models

# Register your models here.
"""acceso al admin para editar y crear profile """
admin.site.register(models.UserProfile)