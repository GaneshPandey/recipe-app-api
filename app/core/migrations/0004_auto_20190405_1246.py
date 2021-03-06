# Generated by Django 2.1.8 on 2019-04-05 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190404_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='swimmer',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='city_of_birth',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='distance',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='fathers_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='height_in_cm',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='main_stroke',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='max_heart_rate',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='mothers_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='phone_no',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='rest_heart_rate',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='school',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='state',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='stroke_rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='swimmer',
            name='weight_in_pound',
            field=models.IntegerField(default=0),
        ),
    ]
