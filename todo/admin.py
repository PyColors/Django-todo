from django.contrib import admin

# import todo model
from .models import Todo


# Register Todo model.
admin.site.register(Todo)