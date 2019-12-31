from django.db    import models
from django.conf  import settings
from django.utils import timezone

# モデルを定義する
class Post(models.Model):
    # データ型の定義
    author       = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    title        = models.CharField(max_length=200)
    text         = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True , null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title



