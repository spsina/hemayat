# Generated by Django 3.0.4 on 2020-03-30 10:24

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 3, 30, 10, 24, 39, 651627, tzinfo=utc), help_text='Create datetime of the note'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='text',
            field=models.TextField(help_text='Note'),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='Optional name for the given location', max_length=255, null=True)),
                ('lat', models.DecimalField(decimal_places=16, help_text='latitude', max_digits=22)),
                ('lon', models.DecimalField(decimal_places=16, help_text='longitude', max_digits=22)),
            ],
            options={
                'unique_together': {('lat', 'lon')},
            },
        ),
        migrations.AddField(
            model_name='note',
            name='location',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='core.Location'),
            preserve_default=False,
        ),
    ]
