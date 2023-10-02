# """
# Tests for report API.
# """

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import ReportDetails
from core.models import InspectionReport

from report.serializers import InspectionReportSerializer

REPORT_URL = reverse('report:report-list')


def create_report(user, **params):
    """Create and return a sample recipe."""
    defaults = {
        'title': 'Sample report title',
        'r_id': 'Sample R_id',
        'date': '2023-09-18',
        'customer_fname': 'Samplefname',
        'customer_lname': 'Samplelname',
        'bedroom_count': 3,
        'bathroom_count': 3,
        'garage_type': 'Detached',
        'basement_type': True,
    }
    defaults.update(params)

    ReportDetails.objects.create(user=user, **defaults)
    return ReportDetails


class PublicRecipeAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(REPORT_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeApiTests(TestCase):
    """Test authenticated API requests."""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'user@example.com',
            'testpass123',
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_report(self):
        """Test retrieving a list of reports."""
        create_report(user=self.user)
        create_report(user=self.user)

        res = self.client.get(REPORT_URL)

        report = InspectionReport.objects.all().order_by('-report_details_id')
        serializer = InspectionReportSerializer(report, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_recipe_list_limited_to_user(self):
        """Test list of reports is limited to company users."""
        other_user = get_user_model().objects.create_user(
             'other@example.com',
             'password123',
        )
        create_report(user=self.user)
        create_report(user=other_user)

        res = self.client.get(REPORT_URL)

        report = InspectionReport.objects.filter(user=self.user)
        serializer = InspectionReportSerializer(report, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
