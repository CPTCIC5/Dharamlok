from django.contrib import admin
from .models import Broker,Sauda


admin.site.index_title='Natraj Industries Admin'
admin.site.site_header='Natraj Control Panel'
admin.site.site_title='Natraj Control Panel'


@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display = ['name','contact_number']  #shows on the page
    class Meta:
        fields = ['__all__']


@admin.register(Sauda)
class SaudaAdmin(admin.ModelAdmin):
    list_display = ['broker_name','rate']