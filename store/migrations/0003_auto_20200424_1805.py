# Generated by Django 2.2.6 on 2020-04-24 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200424_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageinfo',
            name='uploadImg',
            field=models.ImageField(default='', upload_to='store/images'),
        ),
    ]
