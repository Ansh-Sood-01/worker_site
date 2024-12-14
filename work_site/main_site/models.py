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
