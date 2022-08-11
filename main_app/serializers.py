import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Messages


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        # fields = ('id', 'form_name', 'message', 'date')
        fields = "__ALL__"

