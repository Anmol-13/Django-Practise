# Generated by Django 2.2.6 on 2020-04-20 15:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppTwo', '0002_auto_20200420_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Password',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='User',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
