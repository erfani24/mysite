# Generated by Django 3.2.18 on 2023-03-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='login_requier',
            field=models.BooleanField(default=False),
        ),
    ]
