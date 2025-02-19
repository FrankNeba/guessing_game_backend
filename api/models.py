from django.db import models
from django.contrib.auth. models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='profiles')
    code = models.PositiveIntegerField(null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username



class Score(models.Model):
    score = models.IntegerField(default = 0)
    highestScore = models.IntegerField(default=0) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['highestScore']
def __str__(self):
    return f'{self.user.username}'

def save(self, *args, **kwargs):
    if self.pk:
        if self.score > self.highestScore:
            self.highestScore = self.score
    super().save(*args, **kwargs)
