from django.db import models


class Region(models.Model):
    name = models.CharField(max_length=15)
    slug = models.SlugField(max_length=15)

    def __str__(self):
        return self.name


class Salesperson(models.Model):
    region = models.ForeignKey(Region, related_name='region', on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    image = models.ImageField(upload_to='media/', blank=True)
    
    def __str__(self):
        return self.name


class Rating(models.Model):
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]
    salesperson = models.ForeignKey(Salesperson,
                                    related_name='salesperson',
                                    on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, blank=False, default=None)
    sent_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.salesperson.name} {self.salesperson.surname}"
