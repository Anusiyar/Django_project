from django.contrib import admin

# Register your models here.
from .models import slider, whatido, whatidoitem, about, aboutbrief, aboutprojects, aboutskill, work, workimg, experience, experiencelist, contacttitle, contactaddr, contactform

admin.site.register(slider)
admin.site.register(whatido)
admin.site.register(whatidoitem)
admin.site.register(about)
admin.site.register(aboutbrief)
admin.site.register(aboutprojects)
admin.site.register(aboutskill)
admin.site.register(work)
admin.site.register(workimg)
admin.site.register(experience)
admin.site.register(experiencelist)
admin.site.register(contacttitle)
admin.site.register(contactaddr)
admin.site.register(contactform)
