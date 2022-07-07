# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import CARVANSTATUS, CARVAN


# @receiver(post_save, sender=CARVAN)
# def create_carvan_status(sender, **kwargs):
#     if kwargs.get('created'):
#         CARVANSTATUS.objects.create(carvan=kwargs.get('instance'))
#         print('created')
#     else:
#         print('updated')