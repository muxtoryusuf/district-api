from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"
        ordering = ['-id']

    @classmethod
    def create_country_uz(cls):
        obj, _ = Country.objects.get_or_create(name="Uzbekistan")
        return obj


class Region(models.Model):
    name = models.CharField(max_length=256)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Regions"
        ordering = ['-id']

    def __str__(self):
        return self.name


class District(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=500)
    latitude = models.DecimalField(max_digits=10, decimal_places=8, default=41.000000)
    longitude = models.DecimalField(max_digits=10, decimal_places=8, default=71.000000)

    class Meta:
        verbose_name_plural = "TBRegions"
        ordering = ['-id']

    def __str__(self):
        return f"{self.region.name.upper()}: {self.name}"
