from django.contrib import admin

# Register your models here.
from .models import ExternalLinks, UserProfile, PdfResource
from .models import ContactMessage
from .models import Announcement


admin.site.register(UserProfile)
admin.site.register(ExternalLinks)
admin.site.register(PdfResource)
admin.site.register(ContactMessage)
admin.site.register(Announcement)
