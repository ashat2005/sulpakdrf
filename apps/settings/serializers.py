from rest_framework  import serializers

from apps.settings.models import Setting

class SettingsSerializer(serializers.ModelSerializer):
     class Meta:
          model = Setting
          fields = "__all__"