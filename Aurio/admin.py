from django.contrib import admin
from .models import TSong,Song, OldSong,Watchlater,Channel,USong

# Register your models here.
admin.site.register(USong)
admin.site.register(TSong)
admin.site.register(Song)
admin.site.register(OldSong)
admin.site.register(Watchlater)
admin.site.register(Channel)

