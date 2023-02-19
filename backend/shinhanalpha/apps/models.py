from django.db import models

# Create your models here.
class Apps(models.Model):
    name = models.CharField(max_length=128, verbose_name='이름')
    description = models.TextField(verbose_name='설명')

    class Meta:
        db_table = 'shinhan_apps'
        verbose_name = '메뉴'
        verbose_name_plural = '메뉴'