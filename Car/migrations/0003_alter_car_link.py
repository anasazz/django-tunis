# Generated by Django 4.0.4 on 2022-05-09 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Car', '0002_alter_car_cartransmission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='link',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
    ]