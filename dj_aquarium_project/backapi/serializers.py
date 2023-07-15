from pyexpat import model
from rest_framework import serializers
from .models import *

class TicketOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketOrder
        fields = '__all__'


class TicketOrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketOrder
        fields = '__all__'


