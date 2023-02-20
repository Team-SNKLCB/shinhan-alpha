from django.db import models

# Create your models here.
class Mission(models.Model):
    name = models.CharField(max_length=128, verbose_name='미션 이름')
    point = models.CharField(max_length=128, verbose_name='포인트')
    description = models.CharField(max_length=128, verbose_name='설명')

    class Meta:
        db_table = 'shinhan_mission'
        verbose_name = '미션'
        verbose_name_plural = '미션'