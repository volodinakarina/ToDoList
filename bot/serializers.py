# from rest_framework import serializers
#
#
# class VerificationSerializer(serializers.Serializer):
#     verification_code = serializers.CharField(max_length=16)
from rest_framework import serializers

from bot.models import TgUser


class TgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TgUser
        fields = ('verification_code',)
