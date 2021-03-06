from django.db import models


class Post(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=False)
    content = models.TextField()
    author = models.CharField(max_length=255, blank=False)
    owner = models.ForeignKey(
        'auth.user', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
