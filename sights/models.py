from django.db import models

# Create your models here.
CITY_CHOICES = [('kastoria', 'KASTORIA'), ('serres', 'SERRES')]
CATEGORY_CHOICES = [('nature', 'NATURE'), ('church', 'CHURCH'), ('museum', 'MUSEUM')]


class Sights(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    Title = models.CharField(max_length=100, blank=True, default='')
    Image = models.ImageField(max_length=100, blank=True, default='')
    Information = models.TextField()
    City = models.CharField(choices=CITY_CHOICES, default='kastoria', max_length=100)
    Category = models.CharField(choices=CATEGORY_CHOICES, default='nature', max_length=100)
    owner = models.ForeignKey('auth.User', related_name='sights', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.Title
