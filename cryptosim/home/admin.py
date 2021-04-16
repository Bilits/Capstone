from django.contrib import admin
from home.models import *
from django.contrib.auth.models import Permission

admin.site.site_header = "Admin Panel"
admin.site.site_title = "CryptoSim"
admin.site.index_title = "CryptoSim"



admin.site.register(Profile)
admin.site.register(Wallet)
admin.site.register(Coin)
admin.site.register(Transaction)
admin.site.register(Permission)


