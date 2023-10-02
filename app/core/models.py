"""
Database models.
"""
import uuid
import os

from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


# def recipe_image_file_path(instance, filename):
#     """Generate file path for new recipe image."""
#     ext = os.path.splittext(filename)[1]
#     filename = f'{uuid.uuid4()}{ext}'

#     return os.path.join('uploads', 'recipe', filename)


def logo_image_file_path(instance, filename):
    """Generate file path for new recipe image."""
    ext = os.path.splittext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'logo', filename)


def signature_image_file_path(instance, filename):
    """Generate file path for new recipe image."""
    ext = os.path.splittext(filename)[1]
    filename = f'{uuid.uuid4()}{ext}'

    return os.path.join('uploads', 'signature', filename)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    user_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        )
    email = models.EmailField(max_length=255, unique=True)
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    invited_user_count = models.SmallIntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class ReportDetails(models.Model):
    """Report object."""
    report_uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100)
    r_id = models.CharField(max_length=100)
    date = models.DateTimeField('date published')
    customer_fname = models.CharField(max_length=25)
    customer_lname = models.CharField(max_length=25)
    bedroom_count = models.SmallIntegerField(default=0)
    bathroom_count = models.SmallIntegerField(default=0)
    garage_type = models.CharField(max_length=10)
    basement_type = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Overview(models.Model):
    """Overview Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    scope = models.TextField()
    state_of_occupancy = models.CharField(max_length=15)
    weather = models.CharField(max_length=15)
    recent_rain = models.CharField(max_length=10)
    ground_cover = models.CharField(max_length=15)
    approx_age = models.CharField(max_length=10)


class Summary(models.Model):
    """Summary Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    items_not_operating = models.TextField(null=True)
    major_concerns = models.TextField(null=True)
    safety_hazards = models.TextField(null=True)
    further_review = models.TextField(null=True)
    monitor = models.TextField(null=True)
    general_maintenance = models.TextField(null=True)
    needing_repair = models.TextField(null=True)


class Photos(models.Model):
    """Photos Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    grounds_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )
    roof_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )
    exterior_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )
    garage_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )
    kitchen_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )
    laundry_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )
    bathroom_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )
    bedrooms_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )
    interior_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )
    basement_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )
    crawl_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )
    plumbing_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )
    heating_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )
    living_room_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )
    dining_room_photos = models.ImageField(
        null=True,
        upload_to=logo_image_file_path
    )


class ReceiptInvoice(models.Model):
    """Receipt/Invoice Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    company = models.CharField(max_length=75)
    date = models.DateTimeField('date published')
    inspector_fname = models.CharField(max_length=25)
    inspector_lname = models.CharField(max_length=25)
    client_fname = models.CharField(max_length=25)
    client_lname = models.CharField(max_length=25)
    payment_type = models.CharField(max_length=15)
    total_fee = models.DecimalField(max_digits=5, decimal_places=2)


class Grounds(models.Model):
    """Grounds Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    service_walks = models.TextField(null=True)
    drive_parking = models.TextField(null=True)
    stoop_steps = models.TextField(null=True)
    patio = models.TextField(null=True)
    deck_balcony = models.TextField(null=True)
    covers = models.TextField(null=True)
    fence_wall = models.TextField(null=True)
    landscaping = models.TextField(null=True)
    retaining_wall = models.TextField(null=True)
    hose_bibs = models.TextField(null=True)


class Roof(models.Model):
    """Roof Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    general = models.TextField(null=True)
    style = models.TextField(null=True)
    ventilation = models.TextField(null=True)
    flashing = models.TextField(null=True)
    valleys = models.TextField(null=True)
    condition = models.TextField(null=True)
    skylights = models.TextField(null=True)
    plumbing_vents = models.TextField(null=True)


class Exterior(models.Model):
    """Exterior Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    chimney = models.TextField(null=True)
    gutters = models.TextField(null=True)
    siding = models.TextField(null=True)
    trim = models.TextField(null=True)
    soffit = models.TextField(null=True)
    fascia = models.TextField(null=True)
    flashing = models.TextField(null=True)
    caulking = models.TextField(null=True)
    windows = models.TextField(null=True)
    storm_windows = models.TextField(null=True)
    slab_on_foundation = models.TextField(null=True)
    service_entry = models.TextField(null=True)
    wall_construction = models.TextField(null=True)
    exterior_doors = models.TextField(null=True)


class ExteriorACUnit(Exterior):
    """AC Sub-Class"""
    exterior_ac = models.TextField(null=True)


class GarageCarport(models.Model):
    """Garage Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    type = models.TextField(null=True)
    automatic_opener = models.TextField(null=True)
    safety_reverse = models.TextField(null=True)
    roofing = models.TextField(null=True)
    gutters = models.TextField(null=True)
    siding = models.TextField(null=True)
    trim = models.TextField(null=True)
    floor = models.TextField(null=True)
    sillplate = models.TextField(null=True)
    overhead_doors = models.TextField(null=True)
    service_door = models.TextField(null=True)
    electrical = models.TextField(null=True)
    walls_ceiling = models.TextField(null=True)


class Kitchen(models.Model):
    """Kitchen Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    countertops = models.TextField(null=True)
    cabinets = models.TextField(null=True)
    plumbing = models.TextField(null=True)
    walls_ceiling = models.TextField(null=True)
    heating_cooling = models.TextField(null=True)
    floor = models.TextField(null=True)
    appliances = models.TextField(null=True)


class Laundry(models.Model):
    """Laundry Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    laundry = models.TextField(null=True)


class Bathroom(models.Model):
    """Bathroom Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    bathroom = models.TextField(null=True)


class Bedrooms(models.Model):
    """Bedrooms Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    bedroom = models.TextField(null=True)


class Interior(models.Model):
    """Interior Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    fireplace = models.TextField(null=True)
    stairs_steps = models.TextField(null=True)
    smoke_carbon_det = models.TextField(null=True)
    attic = models.TextField(null=True)


class Basement(models.Model):
    """Basement Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    stairs = models.TextField(null=True)
    foundation = models.TextField(null=True)
    floor = models.TextField(null=True)
    seismic_bolts = models.TextField(null=True)
    drainage = models.TextField(null=True)
    girders_beams = models.TextField(null=True)
    columns = models.TextField(null=True)
    joists = models.TextField(null=True)
    subfloor = models.TextField(null=True)


class CrawlSpace(models.Model):
    """Crawlspace Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    crawlspace = models.TextField(null=True)
    access = models.TextField(null=True)
    foundation = models.TextField(null=True)
    floor = models.TextField(null=True)
    seismic_bolts = models.TextField(null=True)
    drainage = models.TextField(null=True)
    ventilation = models.TextField(null=True)
    girders_beams = models.TextField(null=True)
    joists = models.TextField(null=True)
    subfloor = models.TextField(null=True)
    insulation = models.TextField(null=True)
    vapor_barriers = models.TextField(null=True)


class Plumbing(models.Model):
    """Plumbing Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    water_service = models.TextField(null=True)
    fuel_shutoff = models.TextField(null=True)
    well_pump = models.TextField(null=True)
    sanitary_pump = models.TextField(null=True)


class WaterHeater(Plumbing):
    """Water Heater Sub-Class"""
    water_heater = models.TextField(null=True)


class HeatingSystem(models.Model):
    """Heating System Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    other_systems = models.TextField(null=True)


class Furnace(HeatingSystem):
    """Furnace Model Sub-Class"""
    furnace_unit = models.TextField(null=True)


class Boiler(HeatingSystem):
    """Boiler Model Sub-Class"""
    boiler_unit = models.TextField(null=True)


class ElectricalCoolingSystems(models.Model):
    """Electrical and Cooling Systems Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )


class MainPanel(ElectricalCoolingSystems):
    """Main Panel Sub-Class"""
    main_panel = models.TextField(null=True)


class SubPanel(ElectricalCoolingSystems):
    """Sub-Panel Sub-Class"""
    sub_panel = models.TextField(null=True)


class EvaporatorCoil(ElectricalCoolingSystems):
    """Evaporator Coil Sub-Class"""
    evap_coil = models.TextField(null=True)


class LivingRoom(models.Model):
    """Living Room Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    living_room = models.TextField(null=True)


class DiningRoom(models.Model):
    """Dining Room Model"""
    report_uuid = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    dining_room = models.TextField(null=True)


class InspectionReport(models.Model):
    """Inspection Report Model"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    report_details = models.ForeignKey(
        ReportDetails,
        on_delete=models.CASCADE,
        null=True
    )
    overview = models.ForeignKey(
        Overview,
        on_delete=models.CASCADE,
        null=True
    )
    summary = models.ForeignKey(
        Summary,
        on_delete=models.CASCADE,
        null=True
    )
    photos = models.ForeignKey(
        Photos,
        on_delete=models.CASCADE,
        null=True
    )
    receipt_invoice = models.ForeignKey(
        ReceiptInvoice,
        on_delete=models.CASCADE,
        null=True
    )
    grounds = models.ForeignKey(
        Grounds,
        on_delete=models.CASCADE,
        null=True
    )
    roof = models.ForeignKey(
        Roof,
        on_delete=models.CASCADE,
        null=True
    )
    exterior = models.ForeignKey(
        Exterior,
        on_delete=models.CASCADE,
        null=True
    )
    garage = models.ForeignKey(
        GarageCarport,
        on_delete=models.CASCADE,
        null=True
    )
    kitchen = models.ForeignKey(
        Kitchen,
        on_delete=models.CASCADE,
        null=True
    )
    laundry = models.ForeignKey(
        Laundry,
        on_delete=models.CASCADE,
        null=True
    )
    bathroom = models.ForeignKey(
        Bathroom,
        on_delete=models.CASCADE,
        null=True
    )
    basement = models.ForeignKey(
        Basement,
        on_delete=models.CASCADE,
        null=True
    )
    crawlspace = models.ForeignKey(
        CrawlSpace,
        on_delete=models.CASCADE,
        null=True
    )
    plumbing = models.ForeignKey(
        Plumbing,
        on_delete=models.CASCADE,
        null=True
    )
    heatingsystem = models.ForeignKey(
        HeatingSystem,
        on_delete=models.CASCADE,
        null=True
    )
    electrical_cooling = models.ForeignKey(
        ElectricalCoolingSystems,
        on_delete=models.CASCADE,
        null=True
    )
    living_room = models.ForeignKey(
        LivingRoom,
        on_delete=models.CASCADE,
        null=True
    )
    dining_room = models.ForeignKey(
        DiningRoom,
        on_delete=models.CASCADE,
        null=True
    )

    def create(self, report_details, **validated_data):
        """Helper function to create inspection report"""
        report_details(**validated_data)
        return InspectionReport
