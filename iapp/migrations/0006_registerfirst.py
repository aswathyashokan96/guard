# Generated by Django 3.1.4 on 2021-05-07 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iapp', '0005_auto_20210506_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registerfirst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
