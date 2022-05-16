from django.contrib import admin
from boredbuttonapp.models import Contact
from .models import Games

# Register your models here.
admin.site.register(Contact)
admin.site.register(Games)
