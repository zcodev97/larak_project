from django.apps import AppConfig


class LarakAppConfig(AppConfig):
    name = 'larak_app'

    def ready(self):
        import larak_app.signals
