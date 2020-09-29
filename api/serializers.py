from rest_framework import serializers
from api import models


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    marks = serializers.IntegerField()


class Tagserializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tag
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    # returns id of tag it is related to so use tagserializer
    # read_only becz we donot want in json form
    tags = Tagserializer(many=True, read_only=True)

    class Meta:
        model = models.Article
        fields = '__all__'

    def create(self, validated_data):  # add more data to it
        return self.Meta.model.objects.create(**validated_data)
