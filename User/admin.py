from django.contrib import admin
from .models import user
@admin.register(user)
class userAdmin(admin.ModelAdmin):
    model=user
    Fields='__all__'
