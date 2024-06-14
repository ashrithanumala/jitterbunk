from django.db import models

# Create your models here.
class User(models.Model):
    username =  models.CharField(max_length=200)
    photo = models.CharField(max_length=200)

    def __str__(self):
        return f"username: {self.username}, photo: {self.photo}"
    
class Bunk(models.Model):

    from_user = models.ForeignKey(User, related_name = 'from+', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name = 'to+', on_delete=models.CASCADE)
    time = models.DateTimeField("Bunk Time")

    def __str__(self):
        return f"{self.from_user} bunked {self.to_user} at {self.time}"



