from django.contrib import admin
from .models import bodypartdb, contact
from .models import DataSet

# Register your models here.
admin.site.register(bodypartdb)
admin.site.register(DataSet)
admin.site.register(contact)
