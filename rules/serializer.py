from rest_framework import serializers
from .models import Rules

class RulesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'creator', 'game', 'rule_set', 'created_at')
        model = Rules