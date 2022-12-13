from django.contrib import admin
from .models import TransitType,Transits,Profiles,PredefinedRoutes
# Register your models here.

admin.site.register(TransitType)
admin.site.register(Profiles)
admin.site.register(Transits)
admin.site.register(PredefinedRoutes)