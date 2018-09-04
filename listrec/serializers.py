from rest_framework import serializers


class ListRecSerializer(serializers.Serializer):
    uid = serializers.CharField()
    lid = serializers.CharField()
