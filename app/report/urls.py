"""
Report Urls
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from report import views


router = DefaultRouter()
router.register('reports', views.InspectionReportViewSet, basename='report')
# router.register('tags', views.TagViewSet)
# router.register('ingredients', views.IngredientViewSet)

app_name = 'report'

urlpatterns = [
    path('', include(router.urls)),
]
