# Generated by Django 2.2.6 on 2019-11-01 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtube',
            name='original_full_sized',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
