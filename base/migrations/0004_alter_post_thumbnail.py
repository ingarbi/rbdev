# Generated by Django 4.1.4 on 2022-12-09 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_post_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, default='/placeholder.jpg', null=True, upload_to='images'),
        ),
    ]
