from django.forms import ModelForm
from django import forms
from djangit.models import Hop
from djangit.models import Country
from djangit.models import Aroma

# ===== CREATE A HOPFORM CLASS =====
class HopForm(ModelForm):
    

    class Meta:
        model = Hop
        fields = ['hop_name', 'alpha_acid_low', 'alpha_acid_high', 'beta_acid_low', 'beta_acid_high', 'total_oil_low', 'total_oil_high', 'cohumulone_low', 'cohumulone_high']
        widgets = {
            "alpha_acid_low": forms.NumberInput(attrs={
                'class':"form-control",
                'placeholder':"Alpha Acid Low"
                })
        }

# ===== CREATE A FORM TO ADD A HOP
form = HopForm()

# ===== CREATE A COUNTRYFORM CLASS =====
class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = ['country_name']

# ===== CREATE A FORM TO ADD A COUNTRY
form = CountryForm()

# ===== CREATE AN AROMAFORM CLASS =====
class AromaForm(ModelForm):
    class Meta:
        model = Aroma
        fields = ['aroma_type']

# ===== CREATE A FORM TO ADD AN AROMA
form = AromaForm()
