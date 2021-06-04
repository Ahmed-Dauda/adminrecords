from django.contrib import admin
from studentreg.models import Salat, Dining, Lightout, Prep, Hygiene
# Register your models here.
admin.site.register(Salat)


admin.site.register(Prep)



admin.site.site_header = "Esteem Hostel Administration Site"
admin.site.site_title = 'Student Registration'
admin.site.index_title = 'Welcome to Esteem Platform'
