# Generated by Django 5.0 on 2023-12-15 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sauda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sauda',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Data'),
        ),
    ]
