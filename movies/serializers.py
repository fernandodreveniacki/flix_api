from rest_framework import serializers
from movies.models import Movie

"""
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
    )
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True,
    )
    resume = serializers.CharField()
"""

class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1900!.')
        return value
    
    def validate_resume(self, value):
        if len(value) > 300:
            raise serializers.ValidationError('Resumo não deve ser maior do que 300 caracteres!.')
        return value