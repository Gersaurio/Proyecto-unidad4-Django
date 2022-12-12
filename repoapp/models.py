from django.db import models
from django.utils import timezone
from django.forms.widgets import HiddenInput
# Create your models here.





class Project(models.Model):
    photo = models.URLField()
    tittle = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(editable=False) 
    deleted_at = models.DateTimeField(null=True,blank=True)
    tags = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    



    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
                 
        return super(Project,self).save(*args, **kwargs)

    
    class Meta:
        db_table = "Projects"


# Modulo "IPWARE" para guardar direcciones IP
class Ip(models.Model):
    ip = models.GenericIPAddressField()

    class Meta:
        db_table = "ip_visitors"


