import django
from waffle.models import Flag

# to create cache for the first time
if django.VERSION > (1, 7):
    from django.db.models.signals import post_migrate
else:
    from south.signals import post_migrate



def add_flag(sender, **kwargs):

    flag, created = Flag.objects.get_or_create(name='myflag')
    if created:
        flag.delete()



post_migrate.connect(add_flag)