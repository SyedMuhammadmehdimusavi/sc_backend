from rest_framework import serializers
from .models import Quote


class QuoteSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'body','author','created_at','updated_at']