from django.db import models
import uuid
# Create your models here.
class Booking(models.Model):
    booking_no = models.CharField(primary_key=True, default=uuid.uuid4().hex[:5].upper(), max_length=50, editable=False)
    user_name = models.CharField(max_length=122)
    location = models.CharField(max_length=122)
    pickup_date = models.DateField()
    return_date = models.DateField()
    car = models.CharField(max_length=122)
    total_amount = models.FloatField(default=0)
    cost = models.IntegerField(null=True)