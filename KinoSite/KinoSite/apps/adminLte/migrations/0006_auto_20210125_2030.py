# Generated by Django 3.1.5 on 2021-01-25 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminLte', '0005_auto_20210125_1653'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cinemahall',
            old_name='cinema_scheme',
            new_name='hall_scheme',
        ),
        migrations.AlterField(
            model_name='news',
            name='news_status',
            field=models.CharField(choices=[('ON', 'Active'), ('OF', 'Inactive')], max_length=2, verbose_name='Выбор статуса'),
        ),
    ]
