from django.contrib import admin

# Register your models here.
from .models import Image, Camera, Lens, User

admin.site.register(Image)
admin.site.register(Camera)
admin.site.register(Lens)
admin.site.register(User)

