from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=50, null=False, blank=False)
    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.country_name

    def english_speaking_country(self):
        return self.country_name == 'United States' or 'Australia'

class Aroma(models.Model):
    aroma_type = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.aroma_type

class Hop(models.Model):
    hop_name = models.CharField(max_length=50, null=False, blank=False)
    alpha_acid_low = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False, default='0')
    alpha_acid_high = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False, default='0')
    beta_acid_low = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False, default='0')
    beta_acid_high = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False, default='0')
    total_oil_low = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False, default='0')
    total_oil_high = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False, default='0')
    cohumulone_low = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False, default='0')
    cohumulone_high = models.DecimalField(max_digits=4, decimal_places=1, null=False, blank=False, default='0')

    def __str__(self):
        return self.hop_name
