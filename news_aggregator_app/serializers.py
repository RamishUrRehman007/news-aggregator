from rest_framework import serializers

from .models import ( News,
    NewsQuery,
    Favourite
    )

class NewsQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsQuery
        fields = '__all__'
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('__all__')

class GetNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('headline', 'source')

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ('__all__')
