# Generated by Django 4.1.4 on 2022-12-16 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_remove_profile_grade'),
        ('classroom', '0017_remove_comment_user_c_alter_comment_event_c'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user_c',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.profile'),
            preserve_default=False,
        ),
    ]
