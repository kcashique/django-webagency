# Generated by Django 4.0.3 on 2022-04-12 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_rename_services_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='btn_link',
            field=models.URLField(blank=True),
        ),
    ]
