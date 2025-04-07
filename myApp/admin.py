from django.contrib import admin

# Register your models here.
from .models import testimonie
from .models import product
from .models import contacts



# Register your models here.
admin.site.register(testimonie)
admin.site.register(product)
admin.site.register(contacts)

