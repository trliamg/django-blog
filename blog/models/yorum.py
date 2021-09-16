from django.db import models
from django.contrib.auth.models import User
from blog.models import YazilarModel

class YorumModel(models.Model):
    yazan=models.ForeignKey(User, on_delete=models.CASCADE, related_name='yorum')
    yazi=models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorumlar')
    icerik=models.TextField()
    olusturmaTarihi=models.DateTimeField(auto_now_add=True)
    duzenlemeTarihi=models.DateTimeField(auto_now=True)

    class Meta:
        db_table='yorum'
        verbose_name_plural="Yorumlar"
        verbose_name="Yorum"
    
    def __str__(self):
        return self.yazan.username