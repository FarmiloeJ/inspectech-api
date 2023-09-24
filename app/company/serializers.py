"""
Serializers for company API.
"""
from rest_framework import serializers

from core.models import (
    Company,
    User,
)

from django.contrib.auth import authenticate
from django.utils.translation import gettext as _


class CompanySerializer(serializers.ModelSerializer):

    owner = serializers.CharField(required=True)
    owner_email = serializers.EmailField(required=True)
    company_name = serializers.CharField(required=True)
    company_addr = serializers.CharField(required=True)
    phone_number = serializers.IntegerField(required=True)
    logo = serializers.ImageField(required=False)
    owner = User

    class Meta:
        model = Company
        fields = (
            'owner',
            'owner_email',
            'company_name',
            'company_addr',
            'phone_number',
            'logo',
        )

    def _get_or_create_company(self, owner, company):
        """Handle getting or creating a company as needed."""
        auth_user = self.context['request'].user
        for obj in company:
            company_obj = Company.objects.get_or_create(
                owner=auth_user,
                **company,
            )
            owner.company.add(company_obj)

    def create(self, validated_data):
        """Create a company."""
        company = validated_data.pop('company', [])
        company = Company.objects.create(**validated_data)
        self._get_or_create_company(company, User)

        return company

    def update(self, instance, validated_data):
        """Update company."""
        company_addr = validated_data.pop('company_addr', None)
        phone_number = validated_data.pop('company_addr', None)
        logo = validated_data.pop('company_addr', None)
        if company_addr is not None:
            instance.company_addr.clear()
            self._get_or_create_company(company_addr, instance)
        if phone_number is not None:
            instance.company_addr.clear()
            self._get_or_create_company(phone_number, instance)

        if logo is not None:
            instance.logo.clear()
            self._get_or_create_company(logo, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class CompanyLogoSerializer(serializers.ModelSerializer):
    """Serializer for uploading logos to companies."""

    class Meta:
        model = Company
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}


class OwnerAuthTokenSerializer(serializers.Serializer):
    """Serializer for the owner auth token."""
    owner_email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the owner."""
        owner_email = attrs.get('owner_email')
        password = attrs.get('password')
        owner = authenticate(
            request=self.context.get('request'),
            username=owner_email,
            password=password,
        )
        if not owner:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['owner'] = owner
        return attrs
