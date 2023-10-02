"""
Serializers for reports API.
"""
from rest_framework import serializers


from core.models import (
    ReportDetails, Overview, Summary,
    ReceiptInvoice, Grounds, Roof,
    GarageCarport, Exterior, ExteriorACUnit,
    Kitchen, Laundry, Basement, CrawlSpace,
    Bathroom, Bedrooms, Interior, Plumbing,
    WaterHeater, ElectricalCoolingSystems, MainPanel,
    SubPanel, EvaporatorCoil, Boiler, Furnace,
    HeatingSystem, DiningRoom, LivingRoom,
    InspectionReport, models
)

import uuid


class ReportDetailsSerializer(serializers.ModelSerializer):
    """Report Detail Serializer"""
    class Meta:
        model = ReportDetails
        fields = ['report_uuid', 'title', 'r_id',
                  'date', 'customer_fname', 'customer_lname',
                  'bedroom_count', 'bathroom_count', 'garage_type',
                  'basement_type']
        read_only_fields = ['report_uuid']


class OverviewSerializer(serializers.ModelSerializer):
    """Serializer for overview model"""

    class Meta:
        model = Overview
        fields = ['report_uuid', 'scope', 'state_of_occupancy',
                  'weather', 'recent_rain', 'ground_cover',
                  'approx_age']
        read_only_fields = ['report_uuid']


class SummarySerializer(serializers.ModelSerializer):
    """Serializer for summary model"""

    class Meta:
        model = Summary
        fields = ['report_uuid', 'items_not_operating', 'major_concerns',
                  'safety_hazards', 'further_review', 'monitor',
                  'general_maintenance', 'needing_repair']
        read_only_fields = ['report_uuid']


# class PhotosSerializer(serializers.ModelSerializer):
#     """Serializer for photos model"""

#     class Meta:
#         model = Photos
#         fields = ['report_uuid', 'grounds_photos',
# 'roof_photos',
#                   'exterior_photos', 'garage_photos',
# 'kitchen_photos', 'laundry_photos',
#                   'bathroom_photos', 'bedroom_photos',
# 'interior_photos',
#                   'basement_photos', 'crawl_photos',
# 'plumbing_photos',
#                   'heating_photos', 'living_room_photos',
# 'dining_room_photos']
#         read_only_fields = ['report_uuid']


class ReceiptInvoiceSerializer(serializers.ModelSerializer):
    """Serializer for receipt invoice model"""

    class Meta:
        model = ReceiptInvoice
        fields = ['report_uuid', 'company', 'date',
                  'inspector_fname', 'inspector_lname', 'client_fname',
                  'client_lname', 'payment_type', 'total_fee']
        read_only_fields = ['report_uuid']


class GroundsSerializer(serializers.ModelSerializer):
    """Serializer for grounds model"""

    class Meta:
        model = Grounds
        fields = ['report_uuid', 'service_walks', 'drive_parking',
                  'stoop_steps', 'patio', 'deck_balcony',
                  'covers', 'fence_wall', 'landscaping',
                  'retaining_wall', 'hose_bibs']
        read_only_fields = ['report_uuid']


class RoofSerializer(serializers.ModelSerializer):
    """Serializer for roof model"""

    class Meta:
        model = Roof
        fields = ['report_uuid', 'general', 'style',
                  'ventilation', 'flashing', 'valleys',
                  'condition', 'skylights', 'plumbing_vents']
        read_only_fields = ['report_uuid']


class ExteriorSerializer(serializers.ModelSerializer):
    """Serializer for Exterior model"""

    class Meta:
        model = Exterior
        fields = ['report_uuid', 'chimney', 'gutters',
                  'siding', 'trim', 'soffit',
                  'fascia', 'flashing', 'caulking',
                  'windows', 'storm_windows', 'slab_on_foundation',
                  'service_entry', 'wall_construction', 'exterior_doors']
        read_only_fields = ['report_uuid']


class ExteriorACUnitSerializer(serializers.ModelSerializer):
    """Serializer for AC unit model"""

    class Meta:
        model = ExteriorACUnit
        fields = ['report_uuid', 'exterior_ac']


class GarageCarportSerializer(serializers.ModelSerializer):
    """Garage carport serializer"""

    class Meta:
        model = GarageCarport
        fields = ['report_uuid', 'type', 'automatic_opener',
                  'safety_reverse', 'roofing', 'gutters',
                  'siding', 'trim', 'floor', 'sillplate',
                  'overhead_doors', 'service_door', 'electrical',
                  'walls_ceiling']
        read_only_fields = ['report_uuid']


class KitchenSerializer(serializers.ModelSerializer):
    """Kitchen Serializer"""

    class Meta:
        model = Kitchen
        fields = ['report_uuid', 'countertops', 'cabinets',
                  'plumbing', 'walls_ceiling', 'heating_cooling',
                  'floor', 'appliances']
        read_only_fields = ['report_uuid']


class LaundrySerializer(serializers.ModelSerializer):
    """Laundry Serializer"""

    class Meta:
        model = Laundry
        fields = ['report_uuid', 'laundry']
        read_only_fields = ['report_uuid']


class BathroomSerializer(serializers.ModelSerializer):
    """Bathroom serializer"""

    class Meta:
        model = Bathroom
        fields = ['report_uuid', 'bathroom']
        read_only_field = ['report_uuid']


class BedroomSerializer(serializers.ModelSerializer):
    """Bedroom serializer"""

    class Meta:
        model = Bedrooms
        fields = ['report_uuid', 'bedroom']
        read_only_fields = ['report_uuid']


class InteriorSerializer(serializers.ModelSerializer):
    """Interior Serializer"""

    class Meta:
        model = Interior
        fields = ['report_uuid', 'fireplace', 'stairs_steps',
                  'smoke_carbon_det', 'attic']
        read_only_fields = ['report_uuid']


class BasementSerializer(serializers.ModelSerializer):
    """Basement Serializer"""

    class Meta:
        model = Basement
        fields = ['report_uuid', 'stairs', 'foundation',
                  'floor', 'seismic_bolts', 'drainage',
                  'girders_beams', 'columns', 'joists',
                  'subfloor']
        read_only_fields = ['report_uuid']


class CrawlSpaceSerializer(serializers.ModelSerializer):
    """Crawl Space Serializer"""

    class Meta:
        model = CrawlSpace
        fields = ['report_uuid', 'crawlspace', 'access',
                  'foundation', 'floor', 'seismic_bolts',
                  'drainage', 'ventilation', 'girders_beams',
                  'joists', 'subfloor', 'insulation',
                  'vapor_barriers']
        read_only_fields = ['report_uuid']


class PlumbingSerializer(serializers.ModelSerializer):
    """Plumbing Serializer"""

    class Meta:
        model = Plumbing
        fields = ['report_uuid', 'water_service', 'fuel_shutoff',
                  'well_pump', 'sanitary_pump']
        read_only_fields = ['report_uuid']


class WaterHeaterSerializer(serializers.ModelSerializer):
    """Water Heater Serializer"""

    class Meta:
        model = WaterHeater
        fields = ['report_uuid', 'water_heater']
        read_only_fields = ['report_uuid']


class HeatingSystemSerializer(serializers.ModelSerializer):
    """Heating System Serializer"""

    class Meta:
        model = HeatingSystem
        fields = ['report_uuid', 'other_systems']
        read_only_fields = ['report_uuid']


class FurnaceSerializer(serializers.ModelSerializer):
    """Furnace Serializer"""

    class Meta:
        model = Furnace
        fields = ['report_uuid', 'furnace_unit']
        read_only_fields = ['report_uuid']


class BoilerSerializer(serializers.ModelSerializer):
    """Boiler Serializer"""

    class Meta:
        model = Boiler
        fields = ['report_uuid', 'boiler_unit']
        read_only_fields = ['report_uuid']


class ElectricalCoolingSystemsSerializer(serializers.ModelSerializer):
    """Electrical and cooling systems serializer"""

    class Meta:
        model = ElectricalCoolingSystems
        fields = ['report_uuid']
        read_only_fields = ['report_uuid']


class MainPanelSerializer(serializers.ModelSerializer):
    """Main Panel Serializer"""

    class Meta:
        model = MainPanel
        fields = ['report_uuid', 'main_panel']
        read_only_fields = ['report_uuid']


class SubPanelSerializer(serializers.ModelSerializer):
    """Sub Panel Serializer"""

    class Meta:
        model = SubPanel
        fields = ['report_uuid', 'sub_panel']
        read_only_fields = ['report_uuid']


class EvaporatorCoilSerializer(serializers.ModelSerializer):
    """Evaporator Coil Serializer"""

    class Meta:
        model = EvaporatorCoil
        fields = ['report_uuid', 'evap_coil']
        read_only_fields = ['report_uuid']


class LivingRoomSerializer(serializers.ModelSerializer):
    """Living Room Serializer"""

    class Meta:
        model = LivingRoom
        fields = ['report_uuid', 'living_room']
        read_only_fields = ['report_uuid']


class DiningRoomSerializer(serializers.ModelSerializer):
    """Dining Room Serializer"""

    class Meta:
        model = DiningRoom
        fields = ['report_uuid', 'dining_room']
        read_only_fields = ['report_uuid']


class InspectionReportSerializer(serializers.ModelSerializer):
    """Serializer for report details model."""
    report_details = ReportDetailsSerializer(
        many=False, required=True)
    overview = OverviewSerializer(many=False, required=True)
    summary = SummarySerializer(many=False, required=True)
    receipt_invoice = ReceiptInvoiceSerializer(
        many=False, required=True)
    grounds = GroundsSerializer(many=False, required=True)
    roof = RoofSerializer(many=False, required=True)
    exterior = ExteriorSerializer(many=False, required=True)
    garage = GarageCarportSerializer(many=False, required=False)
    kitchen = KitchenSerializer(many=False, required=True)
    laundry = LaundrySerializer(many=False, required=True)
    bathroom = BathroomSerializer(many=False, required=True)
    bedrooms = BedroomSerializer(many=True, required=True)
    interior = InteriorSerializer(many=False, required=True)
    basement = BasementSerializer(many=False, required=False)
    crawlspace = CrawlSpaceSerializer(many=False, required=False)
    plumbing = PlumbingSerializer(many=False, required=True)
    waterheater = WaterHeaterSerializer(many=False, required=True)
    heatingsystem = HeatingSystemSerializer(many=False, required=True)
    furnace = FurnaceSerializer(many=True, required=True)
    boiler = BoilerSerializer(many=False, required=True)
    electricalcoolingsystems = ElectricalCoolingSystemsSerializer(
        many=False, required=True)
    main_panel = MainPanelSerializer(many=True, required=True)
    sub_panel = SubPanelSerializer(many=True, required=True)
    evap_coil = EvaporatorCoilSerializer(many=True, required=True)
    living_room = LivingRoomSerializer(many=True, required=True)
    dining_room = DiningRoomSerializer(many=True, required=True)

    class Meta:
        model = InspectionReport
        fields = '__all__'
        read_only_fields = ['report_uuid']

    def create(self, validated_data):
        """Create a report."""
        models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        report = InspectionReport.objects.create(**validated_data)

        return report

    def update(self, instance, validated_data):
        """Update report."""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
