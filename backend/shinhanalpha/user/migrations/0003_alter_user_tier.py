# Generated by Django 4.1.7 on 2023-02-23 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_usermission_flag_alter_user_tier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tier',
            field=models.CharField(default=1, max_length=20, verbose_name='티어'),
        ),
    ]
