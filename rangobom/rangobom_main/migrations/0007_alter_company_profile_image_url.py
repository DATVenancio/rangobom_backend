# Generated by Django 5.1.6 on 2025-02-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rangobom_main', '0006_remove_company_profile_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='profile_image_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
