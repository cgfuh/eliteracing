from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from cmdrs.models import Commander


class Course(models.Model):
    COURSE_ZEROGRAVITY = 'zerogravity'
    COURSE_SURFACE = 'surface'
    COURSE_SRVRALLY = 'srvrally'
    COURSE_SRVCROSS = 'srvcross'
    COURSE_STADIUM = 'stadium'
    COURSE_TYPES = [
        (COURSE_ZEROGRAVITY, 'Zero Gravity'),
        (COURSE_SURFACE, 'Surface'),
        (COURSE_SRVRALLY, 'SRV Rally'),
        (COURSE_SRVCROSS, 'SRV Cross'),
        (COURSE_STADIUM, 'Stadium'),
    ]

    title = models.CharField(max_length=255)
    system = models.CharField(max_length=255)
    course_type = models.CharField(max_length=16, choices=COURSE_TYPES)
    nearby_outfitting = models.CharField(max_length=128, blank=True, default='')
    distance_from_primary = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        default='0.0'
    )
    distance_from_sol = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        default='0.0'
    )
    notes = models.TextField(blank=True, default='')
    created_by = models.ForeignKey(Commander)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u"{} ({}) in {}".format(
            self.title, 
            self.course_type, 
            self.system
        )

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        return super(Course, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return ''
        # FIXME: Implement the detail views!
        return reverse(
            'course_detail',
            kwargs={
                'pk': self.pk,
            }
        )


class BaseCourseInfo(models.Model):
    VEHICLE_SHIP = 'ship'
    VEHICLE_SRV = 'srv'
    VEHICLE_TYPES = [
        (VEHICLE_SHIP, 'Ship'),
        (VEHICLE_SRV, 'SRV'),
    ]

    course = models.OneToOneField(Course)
    vehicle_type = models.CharField(
        max_length=8, 
        blank=True,
        choices=VEHICLE_TYPES, 
        default=VEHICLE_SHIP
    )
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True
        ordering = ('-created',)

    def __unicode__(self):
        return u"{} for {}".format(self.__class__.__name__, self.course.name)

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        return super(CourseInfo, self).save(*args, **kwargs)


class ZeroGravityCourse(BaseCourseInfo):
    """
    The traditional/original race type around a station.
    """
    station_name = models.CharField(max_length=255)
    number_of_rings = models.PositiveIntegerField(default=1)
    length = models.PositiveIntegerField(help_text='In Kilometers')

    def save(self, *args, **kwargs):
        if not self.vehicle_type:
            self.vehicle_type = self.VEHICLE_SHIP

        return super(ZeroGravityCourse, self).save(*args, **kwargs)


class SurfaceCourse(BaseCourseInfo):
    """
    A ship-based surface race, such as canyon loops.
    """
    planet_name = models.CharField(max_length=255)
    coordinates = models.CharField(max_length=64)
    gravity = models.DecimalField(max_digits=5, decimal_places=2, default='1.0')

    def save(self, *args, **kwargs):
        if not self.vehicle_type:
            self.vehicle_type = self.VEHICLE_SHIP

        return super(SurfaceCourse, self).save(*args, **kwargs)


class SRVRallyCourse(BaseCourseInfo):
    """
    An SRV point-to-point race, raced across a planetary surface from one
    port to another.
    """
    PLANET_ROCK = 'rock'
    PLANET_ICE = 'ice'
    PLANET_LAVA = 'lava'
    PLANET_METALLIC = 'metallic'
    PLANET_WATER = 'water'
    PLANET_EARTH = 'earth-like'
    PLANET_AMMONIA = 'ammonia'
    PLANET_GAS = 'gas'
    PLANET_TYPES = [
        (PLANET_ROCK, 'rock'),
        (PLANET_ICE, 'ice'),
        (PLANET_LAVA, 'lava'),
        (PLANET_METALLIC, 'metallic'),
        (PLANET_WATER, 'water'),
        (PLANET_EARTH, 'earth-like'),
        (PLANET_AMMONIA, 'ammonia'),
        (PLANET_GAS, 'gas'),
    ]

    planet_name = models.CharField(max_length=255)
    length = models.PositiveIntegerField(help_text='In Kilometers')
    start_port_name = models.CharField(max_length=255)
    end_port_name = models.CharField(max_length=255)
    starting_line = models.CharField(max_length=255, blank=True, default='')
    finish_line = models.CharField(max_length=255, blank=True, default='')
    gravity = models.DecimalField(max_digits=5, decimal_places=2, default='1.0')
    planet_type = models.CharField(
        max_length=32, 
        choices=PLANET_TYPES, 
        default=PLANET_ROCK
    )

    def save(self, *args, **kwargs):
        if not self.vehicle_type:
            self.vehicle_type = self.VEHICLE_SRV

        return super(SRVRallyCourse, self).save(*args, **kwargs)


class SRVCrossCourse(BaseCourseInfo):
    """
    An SRV-based port race, involving using the port as a racetrack, usually
    in a loop.
    """
    planet_name = models.CharField(max_length=255)
    port_name = models.CharField(max_length=255)
    gravity = models.DecimalField(max_digits=5, decimal_places=2, default='1.0')
    tidally_locked = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.vehicle_type:
            self.vehicle_type = self.VEHICLE_SRV

        return super(SRVRallyCourse, self).save(*args, **kwargs)


class StadiumCourse(BaseCourseInfo):
    """
    A ship-based port race, involving flying in/around/through man-made
    structures within the port.
    """
    planet_name = models.CharField(max_length=255)
    port_name = models.CharField(max_length=255)
    gravity = models.DecimalField(max_digits=5, decimal_places=2, default='1.0')

    def save(self, *args, **kwargs):
        if not self.vehicle_type:
            self.vehicle_type = self.VEHICLE_SRV

        return super(SRVRallyCourse, self).save(*args, **kwargs)


class CourseScreenshot(models.Model):
    course = models.ForeignKey(Course, related_name="screenshots")
    shot = models.ImageField(max_length=255)
    is_primary = models.BooleanField(
        default=False, 
        help_text="Is this the main/best image the user should see?"
    )
    is_annotated = models.BooleanField(
        default=False, 
        help_text="Does this image have a course drawn on top of it?"
    )
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("created", "is_primary")

    def __unicode__(self):
        return u"{} for {}".format(self.shot.get_filename(), self.course.title)

    def save(self, *args, **kwargs):
        self.updated = timezone.now()
        return super(CourseScreenshot, self).save(*args, **kwargs)
