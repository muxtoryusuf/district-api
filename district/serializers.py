from rest_framework import serializers
from . models import District


class RegionDistrictSerializer(serializers.ModelSerializer):

    class Meta:
        model = District
        fields = ("id", "name")