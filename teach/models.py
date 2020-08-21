from django.db import models

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    context = models.TextField()
    video = models.FileField(upload_to='videos/', null=True, verbose_name="video")
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name
