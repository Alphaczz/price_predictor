# Generated by Django 4.1.1 on 2022-09-17 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model1', '0009_alter_data_pri_cam_alter_data_ram_alter_data_rom_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='pre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('predict', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
