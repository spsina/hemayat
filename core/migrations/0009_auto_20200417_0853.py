# Generated by Django 3.0.4 on 2020-04-17 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200417_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='mantaqe',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='pelak',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='postal_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='rabet',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='sarparast',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
