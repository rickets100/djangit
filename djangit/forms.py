# https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms
# https://docs.djangoproject.com/en/1.10/ref/validators/

from django.forms import ModelForm
from django import forms
from djangit.models import Hop
from djangit.models import Country
from djangit.models import Aroma

# ===== CREATE A HOPFORM CLASS =====
class HopForm(ModelForm):

    class Meta:
        model = Hop
        fields = ['id', 'hop_name', 'alpha_acid_low', 'alpha_acid_high', 'beta_acid_low', 'beta_acid_high', 'total_oil_low', 'total_oil_high', 'cohumulone_low', 'cohumulone_high']
        widgets = {
            "hop_name": forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':"HOP VARIETY"
                }),
            "alpha_acid_low": forms.NumberInput(attrs={
                'class':"form-control",
                'placeholder':"Alpha Acid Low"
                }),
            "alpha_acid_high": forms.NumberInput(attrs={
                'class':"form-control",
                'placeholder':"Alpha Acid High"
                }),
            "beta_acid_low": forms.NumberInput(attrs={
                'class':"form-control",
                'placeholder':"Beta Acid Low"
                }),
            "beta_acid_high": forms.NumberInput(attrs={
                'class':"form-control",
                'placeholder':"Beta Acid High"
                }),
            "total_oil_low": forms.NumberInput(attrs={
                'class':"form-control",
                'placeholder':"Total Oil Low"
                }),
            "total_oil_high": forms.NumberInput(attrs={
                'class':"form-control",
                'placeholder':"Total Oil High"
                }),
            "cohumulone_low": forms.NumberInput(attrs={
                'class':"form-control",
                'placeholder':"Cohumulone Low"
                }),
            "cohumulone_high": forms.NumberInput(attrs={
                'class':"form-control",
                'placeholder':"Cohumulone High"
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
