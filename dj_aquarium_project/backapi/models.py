from django.db import models


SERVICE_VALUES = (
    ("l1", "Л/1Э"),
    ("l2", "Л/1У"),
    ("l3", "Л/1Л"),
    ("k1", "К/2К "),
    ("k2", "К/2У"),
    ("p1", "П/3Б"),
    ("p2", "П/3Э")
)

class TicketOrder(models.Model):
    serviceClass = models.CharField(max_length=16)
    departureDate = models.DateField(null=True, blank=True, default=None)
    departureStation = models.CharField(max_length=64)
    arrivalStation = models.CharField(max_length=64)
    totalDistance = models.PositiveIntegerField()
    seatNumber = models.PositiveIntegerField()
    trainNumber = models.CharField(max_length=64)
    costTicket = models.FloatField()
    costPlatzcard = models.FloatField()
    costService = models.FloatField()
