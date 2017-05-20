# if migrations get all screwy:
# ./manage.py migrate djangit zero
# then delete (manually) everything in the migrations folder EXCEPT __init__.py
# python manage.py showmigrations to show status
# python manage.py makemigrations
# python manage.py migrate
# https://www.youtube.com/watch?v=UpssHYl6bjA&index=7&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK
# the above video at the 10:42 mark has foreign key example

from django.db import models

class Country(models.Model):
    country_name = models.CharField(max_length=50, null=False, blank=False)
    class Meta:
        verbose_name_plural = "countries"

    def __str__(self):
        return self.country_name

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

    # CITRUSY = 'CI'
    # FLORAL = 'FL'
    # FRUITY = 'FR'
    # FUNKY = 'FU'
    # GRASSY = 'GS'
    # HERBAL = 'HE'
    # HOPPY = 'HO'
    # PINEY = 'PI'
    # SPICY = 'SP'
    # AROMA_CHOICES = (
    #     (CITRUSY, 'Citrusy'),
    #     (FLORAL, 'Floral'),
    #     (FRUITY, 'Fruity'),
    #     (FUNKY, 'Funky'),
    #     (GRASSY, 'Grassy'),
    #     (HERBAL, 'Herbal'),
    #     (HOPPY, 'Hoppy'),
    #     (PINEY, 'Piney'),
    #     (SPICY, 'Spicy'),
    # )
    # aroma = models.CharField(
    #     max_length=2,
    #     choices=AROMA_CHOICES,
    #     default=HOPPY,
    # )
