from django.db import models

class UploadedFile(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly define primary key
    file_name = models.CharField(max_length=255)
    file_url = models.URLField()
    file_type = models.CharField(max_length=10, choices=[("image", "Image"), ("video", "Video")])

    def __str__(self):
        return self.file_name
