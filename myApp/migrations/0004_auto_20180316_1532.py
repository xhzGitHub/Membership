# Generated by Django 2.0.2 on 2018-03-16 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_auto_20180316_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userLoginStatus',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='userCoupon',
            field=models.CharField(default='无', max_length=150),
        ),
        migrations.AlterField(
            model_name='user',
            name='userExpensesRecord',
            field=models.CharField(default='无', max_length=150),
        ),
    ]
