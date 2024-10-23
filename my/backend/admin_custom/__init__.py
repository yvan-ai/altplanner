# apps.py or __init__.py
from django.apps import AppConfig

class AdminCustomConfig(AppConfig):
    name = 'admin_custom'

    def ready(self):
        import admin_custom.signals  # Assure-toi que les signaux sont chargés
