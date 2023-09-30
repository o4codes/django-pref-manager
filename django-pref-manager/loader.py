from typing import Optional

from django.conf import settings
from decouple import config as env_config

from .schema import PreferenceSchema
from .models import AppPreference

app_preferences: list[PreferenceSchema] = getattr(settings, "APP_PREFERENCES", None)


class PreferenceLoader:
    def __init__(self):
        pass

    def __getattribute__(self, name):
        preference: Optional[PreferenceSchema] = next(
            (prop for prop in app_preferences if prop.name == name), None
        )
        if preference:
            if preference.is_env:
                value = env_config(preference.name, default=preference.default)
                return preference.parse_value(value)
            return self._get_create_app_preferences(preference)
        return super(PreferenceLoader, self).__getattribute__(name)

    @classmethod
    def _get_create_app_preferences(cls, preference: PreferenceSchema):
        preference_instance, _ = AppPreference.objects.get_or_create(
            name=preference.name,
            defaults={
                "value": preference.default,
            }
        )
        return preference.parse_value(preference_instance.value)
