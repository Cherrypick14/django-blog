from django.db import models
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
    )
    bio = models.CharField(max_length=240, blank=True)
    image= models.ImageField(default='default.jpg', upload_to='profile_pics')
    following=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'
class Post(models.Model):

    class Meta:
        ordering =['-published']
    
    slug = models.SlugField(max_length=240, unique=True)
    title = models.CharField(max_length=240, unique=True)
    # subtitle = models.CharField(max_length=240, blank=True)
    body = models.TextField()
    description = models.CharField(max_length=155, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    # date_modified = models.DateTimeField(auto_now=True)
    # publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=True)

    # author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    # tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
