# Generated by Django 4.1.4 on 2023-01-02 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='user',
            new_name='user_info',
        ),
    ]
