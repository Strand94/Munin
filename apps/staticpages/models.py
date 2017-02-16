from django.db import models

#Model for school, to keep track of schools and their info.
class School(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='schools', default='placeholder-school-logo.jpg')
    telephone = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=70, blank=True)
    webpage = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name