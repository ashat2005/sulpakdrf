from rest_framework.generics import ListAPIView

from apps.settings.models import Setting
from apps.settings.serializers import SettingsSerializer

class SettingAPI(ListAPIView):
    queryset = Setting.objects.all()
    serializer_class = SettingsSerializer