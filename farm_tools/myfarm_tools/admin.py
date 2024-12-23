from django.contrib import admin
from .models import Tool, Farmer, Loan, Maintenance

admin.site.register(Tool)
admin.site.register(Farmer)
admin.site.register(Loan)
admin.site.register(Maintenance)
