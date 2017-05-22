
# the above video at the 10:42 mark has foreign key example
# https://docs.djangoproject.com/en/1.10/topics/migrations/#migration-serializing
 # .schema at the client command line
 # sqlmigrate at the command line just prints it to the screen so that you can see what SQL Django thinks is required - doesn't actually do a migration
 #  python manage.py check; this checks for any problems in your project without making migrations or touching the database
 # to filter: Hop.objects.filter(hop_name__startswith='C')


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
