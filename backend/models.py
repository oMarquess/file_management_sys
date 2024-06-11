from django.db import models

# Create your models here.

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
    #metadata = models.JSONField(default=dict)  # Requires Django 3.1 and above
    #error_message = models.TextField(blank=True, null=True)





    def save(self, *args, **kwargs):
        # Remove any existing files before saving a new one
        self.__class__.objects.all().delete()
        super(UploadedFile, self).save(*args, **kwargs)

    def __str__(self):
        return self.file.name

