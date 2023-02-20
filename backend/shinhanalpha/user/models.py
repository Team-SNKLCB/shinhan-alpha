from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    # id = models.CharField("아이디", max_length=20)
    # pw = models.CharField("비밀번호", max_length=4)
    name = models.CharField("이름", max_length=20)
    ename = models.CharField("영문이름", max_length=20)
    rrn = models.CharField("주민등록번호", max_length=13)
    tel = models.CharField("연락처", max_length=12)
    tier = models.CharField("영문이름", max_length=20)
    e_active = models.BooleanField(default=False)
    status = models.CharField(max_length=16, default="일반",
        choices=(
            ('일반','일반'),
            ('탈퇴','탈퇴'),
            ('휴면','휴면'),
        )
    )
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='가입일')

    class Meta:
        db_table = 'shinhan_user'
        verbose_name = '회원'
        verbose_name_plural = '회원'

class Point(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='회원')
    # mission = models.ForeignKey('mission.Mission', on_delete=models.CASCADE, verbose_name='미션')
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')

    class Meta:
        db_table = 'shinhan_user_point'
        verbose_name = '회원 포인트'
        verbose_name_plural = '회원 포인트'

class UserApps(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='회원')
    app = models.ForeignKey('apps.Apps', on_delete=models.CASCADE, verbose_name='메뉴')
    flag = models.IntegerField(default=0, verbose_name='메뉴상태')
    class Meta:
        db_table = 'shinhan_user_apps'
        verbose_name = '회원 메뉴'
        verbose_name_plural = '회원 메뉴'

class SBLog(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='회원')
    # stock = models.ForeignKey('stock.Stock', on_delete=models.CASCADE, verbose_name='주식종목')
    tstamp = models.DateTimeField(auto_now_add=True, verbose_name='등록일시')
    class Meta:
        db_table = 'shinhan_user_sb'
        verbose_name = '회원 매매 로그'
        verbose_name_plural = '회원 매매 로그'

class RewardLog(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='회원')
    # reward = models.ForeignKey('reward.Reward', on_delete=models.CASCADE, verbose_name='리워드')
    flag = models.IntegerField(default=0, verbose_name='리워드상태')
    class Meta:
        db_table = 'shinhan_user_reward'
        verbose_name = '회원 리워드'
        verbose_name_plural = '회원 리워드'

class UserBank(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='회원')
    # bank = models.ForeignKey('bank.Bank', on_delete=models.CASCADE, verbose_name='계좌')
    class Meta:
        db_table = 'shinhan_user_bank'
        verbose_name = '회원 계좌'
        verbose_name_plural = '회원 계좌'

class UserInvite(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='회원')
    # invite = models.ForeignKey('invite.Invite', on_delete=models.CASCADE, verbose_name='초대')
    class Meta:
        db_table = 'shinhan_user_invite'
        verbose_name = '회원 초대'
        verbose_name_plural = '회원 초대'