from django.db import models


class UserProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    school = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ExternalLinks(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    link = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.category} {self.name} {self.level} {self.link}"


class PdfResource(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='documents/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Highlight(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



class ResourceURL(models.Model):
    url = models.URLField(max_length=50)


class Resources(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    files = models.FileField(upload_to='documents/', null=True, blank=True)
    urls = models.ManyToManyField(ResourceURL, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    CHOICES = {
        "Coach": "Coach",
        "Student": "Student",
        "Judge": "Judges",
        "Events": "Events"
    }
    role = models.CharField(max_length=20, choices=CHOICES)

    def __str__(self):
        return self.title
