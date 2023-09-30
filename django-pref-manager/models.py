from django.db import models


class AppPreference(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=False)
    value = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "App Preference"
        verbose_name_plural = "App Preferences"
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["created_at"]),
            models.Index(fields=["updated_at"]),
        ]
