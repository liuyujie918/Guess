from rest_framework import serializers


class SingleRecSerializer(serializers.Serializer):
    uid = serializers.CharField()
    pid = serializers.CharField()

