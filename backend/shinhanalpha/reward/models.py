from django.db import models

# Create your models here.
class Reward(models.Model):
    reward_name = models.CharField(max_length=128, verbose_name='리워드 이름')
    tier_name = models.CharField(max_length=128, verbose_name='티어 이름')
    tier_point = models.CharField(max_length=128, verbose_name='기준 점수')

    class Meta:
        db_table = 'shinhan_reward'
        verbose_name = '리워드'
        verbose_name_plural = '리워드'