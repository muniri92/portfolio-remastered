from portfolio_app.models import About, Portfolio, Education, Experience
from rest_framework import serializers


class AboutSerializer(serializers.ModelSerializer):
	"""Serializer for the About model."""

    class Meta:
        model = About
        fields = ('title', 'description')


class PortfolioSerializer(serializers.ModelSerializer):
	"""Serializer for the Portfolio model."""

    class Meta:
        model = Portfolio
        fields = ('title', 'description', 'site', 'repo')


class EducationSerializer(serializers.ModelSerializer):
	"""Serializer for the Education model."""

    class Meta:
        model = Education
        fields = ('institution', 'dates', 'degree')


class ExperienceSerializer(serializers.ModelSerializer):
	"""Serializer for the Experience model."""

    class Meta:
        model = Experience
        fields = ('company', 'position', 'description', 'dates')
