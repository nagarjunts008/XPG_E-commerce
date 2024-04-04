from django.contrib import admin
from . models import ecmodel,csmodel,memodel,eemodel,tcmodel,melmodel,xprojectmodel,othermodel,developermodel,cartmodel,buyer
# Register your models here.

admin.site.register(xprojectmodel)
admin.site.register(ecmodel)
admin.site.register(csmodel)
admin.site.register(memodel)
admin.site.register(eemodel)
admin.site.register(tcmodel)
admin.site.register(melmodel)
admin.site.register(othermodel)
admin.site.register(cartmodel)
admin.site.register(buyer)
admin.site.register(developermodel)