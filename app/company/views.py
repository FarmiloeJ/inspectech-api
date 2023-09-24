"""
Generate company views.
"""
from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework.decorators import action
from rest_framework.response import Response
from company.serializers import (
    OwnerAuthTokenSerializer,
    CompanySerializer,
    Company,
)

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import (
    ObtainAuthToken
)


class CompanyView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        """Upload an image to recipe."""
        company = self.get_object()
        serializer = self.get_serializer(company, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateOwnerTokenView(ObtainAuthToken):
    """Create a new auth token for owner."""
    serializer_class = OwnerAuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageCompanyView(generics.RetrieveUpdateAPIView):
    """Manage the company details."""
    serializer_class = CompanySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated owner."""
        return self.request.user
