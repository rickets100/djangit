# admin here is a package that contains the class ModelAdmin
from django.contrib import admin

# these are classes that are being imported
from .models import Country
from .models import Aroma
from .models import Hop

class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name',)

class AromaAdmin(admin.ModelAdmin):
    list_display = ('aroma_type',)

class HopAdmin(admin.ModelAdmin):
    list_display = ('hop_name', 'alpha_acid_low', 'alpha_acid_high', 'beta_acid_low', 'beta_acid_high', 'total_oil_low', 'total_oil_high', 'cohumulone_low', 'cohumulone_high')

admin.site.register(Hop, HopAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Aroma, AromaAdmin)
