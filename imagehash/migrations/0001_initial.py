# Generated by Django 5.1.3 on 2024-12-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField()),
                ('md5_hash', models.CharField(max_length=32)),
                ('phash', models.CharField(max_length=64)),
            ],
        ),
    ]
