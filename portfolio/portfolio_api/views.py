from django.shortcuts import render
from rest_framework import generics
from portfolio_app.models import About, Portfolio, Education, Experience
from portfolio_api.serializers import AboutSerializer, PortfolioSerializer, EducationSerializer, ExperienceSerializer

# Create your views here.


class AboutAPI(generics.ListAPIView):
    serializer_class = AboutSerializer
    queryset = About.objects.all()

    def get_queryset(self):
        queryset = super(AboutAPI, self).get_queryset()
        return queryset.all()


class PortfolioAPI(generics.ListAPIView):
    serializer_class = PortfolioSerializer
    queryset = Portfolio.objects.all()

    def get_queryset(self):
        queryset = super(PortfolioAPI, self).get_queryset()
        return queryset.all()


class EducationAPI(generics.ListAPIView):
    serializer_class = EducationSerializer
    queryset = Education.objects.all()

    def get_queryset(self):
        queryset = super(EducationAPI, self).get_queryset()
        return queryset.all()


class ExperienceAPI(generics.ListAPIView):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()

    def get_queryset(self):
        queryset = super(ExperienceAPI, self).get_queryset()
        return queryset.all()
