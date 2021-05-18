from django.db import models
import os

#https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.FileField.upload_to
#instance = the instance of the model/class being called
#filename = original filename given
def get_upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return os.path.join("%s" % instance.unit_name, filename)

# Create your models here.
class Unit(models.Model):
    number = models.CharField(max_length = 250)
    unit_name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = get_upload_path, default= "default.png")

    def __str__(self):
        return self.unit_name
    

class Word(models.Model):
    unit_name = models.ForeignKey(Unit, on_delete=models.CASCADE, blank = True)
    english = models.CharField(max_length = 250)
    thai = models.CharField(max_length = 250)
    transliteration = models.CharField(max_length = 250, default = "none")
    audio = models.FileField(upload_to = get_upload_path)
    image = models.ImageField(upload_to = get_upload_path, default= "default.png")

    def __str__(self):
        return self.english + ' - ' + self.thai