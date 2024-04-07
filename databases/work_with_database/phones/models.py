from django.db import models

class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    image = models.URLField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f'{self.id}|{self.name}|{self.price}|{self.lte_exists}|{self.slug}'