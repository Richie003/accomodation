from django.db import models
from django.conf import settings
from django.utils.timezone import now

class Accommodation(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    capacity = models.PositiveIntegerField()
    description = models.TextField()
    price_per_month = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
    @property
    def getimage(self):
        imgs = roomImages.objects.filter(room_id=self.id).first()
        if imgs:
            return imgs.images.url
        else:
            return None
    
    @property
    def capacity(self):
        counter = roomCount.objects.get(Accommodation_id=self.id)
        return counter

class roomImages(models.Model):
    room = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="ROOMS/")

class Booking(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    check_in_date = models.DateField(default=now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking by {self.student} for {self.accommodation}"


class roomCount(models.Model):
    Accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    count = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return str(self.count)
