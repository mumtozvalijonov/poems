# Generated by Django 3.2.7 on 2021-10-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poem', '0006_author_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(null=True, upload_to='media/images'),
        ),
    ]