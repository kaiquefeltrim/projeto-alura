from datetime import datetime
from django.db import models

class Photography(models.Model):

    CATEGORY_OPTIONS = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]

    name = models.CharField(max_length=100, null=False, blank=False)
    legend = models.CharField(max_length=100, null=False, blank=False)
    category = models.CharField(max_length=100, choices=CATEGORY_OPTIONS, default='')
    description = models.TextField(null=False, blank=False)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    published = models.BooleanField(default=False)
    photographys_date = models.DateTimeField(default= datetime.now, blank=False)

    def __str__(self):
        return self.name
    