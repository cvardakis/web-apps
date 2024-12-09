# forms.py

from django import forms
from .models import UserProfile, Announcement, Resources, ResourceURL
from .models import ContactMessage
from .models import Highlight


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'user_email', 'phone_number', 'school', 'role']


class AnnouncementForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Title"}
        ),
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Description"}
        )
    )
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control-file"}, ), required=False

    )

    class Meta:
        model = Announcement
        fields = ['title', 'description', 'file']


class Higlight_form(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Title"}
        ),
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={"class": "form-control", "placeholder": "Description"}
        )
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        required=False,
    )

    class Meta:
        model = Highlight
        fields = ['title', 'description', 'image']


class ResourcesForm(forms.ModelForm):
    title = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Title"}),
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Description"}),
    )
    files = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        required=False,
    )
    urls = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control",
                                     "placeholder": "Enter URLs separated by commas, semicolons, or new lines",
                                     "style": "height: 21px;"}),
        required=False,
    )
    role = forms.ChoiceField(
        choices=Resources.CHOICES.items(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Resources
        fields = ['title', 'description', 'files', 'urls', 'role']

    def clean_urls(self):
        urls_data = self.cleaned_data['urls']
        urls_list = [url.strip() for url in urls_data.split('\n') if url.strip()]
        return [ResourceURL.objects.get_or_create(url=url)[0] for url in urls_list]


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea)
