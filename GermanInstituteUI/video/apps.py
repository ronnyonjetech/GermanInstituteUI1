from django.apps import AppConfig


class VideoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'video'
    verbose_name = 'Video Files and Documents'  # This is the human-readable name for the admin.

