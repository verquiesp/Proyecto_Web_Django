# Generated by Django 4.2.1 on 2023-05-23 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contenido',
            field=models.CharField(max_length=300),
        ),
    ]
