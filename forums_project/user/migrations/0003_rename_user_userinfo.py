# Generated by Django 4.1.4 on 2023-01-02 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_rename_user_subject_user_info'),
        ('thread', '0002_rename_user_thread_user_info'),
        ('comment', '0003_rename_user_comment_user_info'),
        ('comment_emoji', '0002_rename_user_commentemoji_user_info'),
        ('user', '0002_rename_icon_user_icon'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='UserInfo',
        ),
    ]
