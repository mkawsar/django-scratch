from django.db import models

class TiktTokVideo(models.Model):
    username = models.CharField(max_length=255)
    video_url = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.username} - {self.video_url}'
    
    class Meta:
        db_table = 'tiktok_videos'
    
