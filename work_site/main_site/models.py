from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="images")
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image_file = models.ImageField(upload_to="work_images/")

    def __str__(self):
        return self.title
    

class Worker(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='workers')
    description = models.TextField()
    image = models.ImageField(upload_to='worker_images/')
    profile_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

