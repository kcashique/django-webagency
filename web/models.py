from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.urls import reverse


class Contact(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=128)
    project_details = models.TextField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)

    def __str__(self):
        return str(self.name)

class About(models.Model):
    phone = models.CharField(max_length=128)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=128)

    def __str__(self):
        return str(self.phone)


class Blog(models.Model):
    CATEGORY_CHOICES = (('agency', 'Agency'), ('digital',
                        'Digital'), ('creative', 'Creative'), )

    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.CharField(max_length=128, choices=CATEGORY_CHOICES, default="creative")
    featured_image = VersatileImageField()
    description = models.TextField()
    content = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)


class Author(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True, null=True)
    photo = VersatileImageField()
    about = models.TextField()

    def __str__(self):
        return str(self.name)


class Slider(models.Model):
    title = models.CharField(max_length=128)
    sub_title = models.CharField(max_length=128)
    slider_img = VersatileImageField()
    btn_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return str(self.title)


class Project(models.Model):
    CATEGORY_CHOICES = (('advertising', 'Advertising'),
                        ('branding', 'Branding'), ('creative', 'Creative'), )

    title = models.CharField(max_length=128)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = VersatileImageField()
    slug = models.SlugField(unique=True)
    details = models.TextField()

    def get_absolute_url(self):
        return reverse('web:project-details', kwargs={'slug': self.slug})

    def __str__(self):
        return str(self.title)


class Testimonial(models.Model):
    name = models.CharField(max_length=30)
    profile_photo = VersatileImageField()
    feedback = models.TextField()
    designation = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name)


class Service(models.Model):

    title = models.CharField(max_length=128)
    icon = models.FileField()
    description = models.TextField()
    content = models.TextField()
    slug = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('web:services-details', kwargs={'slug': self.slug})

    def __str__(self):
        return str(self.title)


class Category(models.Model):
    name = models.CharField(max_length=128, null=True,)

    def __str__(self):
        return str(self.name)


class SocialMedia(models.Model):
    name = models.CharField(max_length=128, null=True,)
    url = models.URLField(max_length=200)
    random = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return str(self.name)
