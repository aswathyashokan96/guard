# Generated by Django 3.1.4 on 2021-05-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iapp', '0004_auto_20210505_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='about',
            name='image',
        ),
    ]
