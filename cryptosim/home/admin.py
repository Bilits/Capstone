from django.contrib import admin
from home.models import *

admin.site.site_header = "Admin Panel"
admin.site.site_title = "CryptoSim"
admin.site.index_title = "CryptoSim"


admin.site.register(Profile)
