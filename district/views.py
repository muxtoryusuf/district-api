from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from . models import Region, District
from .serializers import RegionDistrictSerializer
from rest_framework.response import Response


class RegionDistrictsAPIView(generics.GenericAPIView):
    """
     GET http://127.0.0.1:8000/api/addresses/v1/retrieve/get-district/Namangan
    """
    permission_classes = [permissions.AllowAny]
    authentication_classes = [TokenAuthentication]
    schema = None

    def get(self, request, region):
        try:
            region = Region.objects.get(name__icontains=region)
            qs = District.objects.filter(region_id=region.id)
            serializer = RegionDistrictSerializer(qs, many=True)
            return Response({"success": True, "message": "OK", "results": serializer.data})
        except Exception as e:
            return Response({"success": False, "message": e.args, "results": []})
