# Generated by Django 4.1.1 on 2022-09-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model1', '0005_data_mobile_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='predictions',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]