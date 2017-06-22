from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from django.core.urlresolvers import reverse

class Book(models.Model):
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="book_adder")
    last_edited_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="book_editor")
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField()
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('profiles:book_detail', kwargs={'slug': self.slug})
    
    class Meta:
        ordering = ["-timestamp", "-updated"]
    
    
def pre_save_book(sender, instance, *args, **kwargs):
    slug = slugify(instance.title)
    instance.slug = slug
    
pre_save.connect(pre_save_book, sender=Book)
    