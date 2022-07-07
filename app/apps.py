from django.apps import AppConfig
from django.core.signals import request_finished

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    
    # def ready(self):
    #     from .signals import create_carvan_status
    #     request_finished.connect(create_carvan_status)