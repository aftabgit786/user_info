# Generated by Django 5.0.4 on 2024-04-21 21:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='educationalinfo',
            name='mobile_number',
            field=models.CharField(blank=True, help_text='Enter your mobile number.', max_length=15),
        ),
        migrations.AlterField(
            model_name='educationalinfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educational_info', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='PersonalInfo',
        ),
    ]
