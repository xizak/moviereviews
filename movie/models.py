from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=2500)
    image = models.ImageField(upload_to="movie/images/")
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=2500)
    Date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    watchAgain = models.BooleanField()

    def __str__(self) -> str:
        return f"what {self.user} thinks about {self.movie}"
