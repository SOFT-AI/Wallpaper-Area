# Generated by Django 2.2.3 on 2019-07-19 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_development', '0011_auto_20190719_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='api',
            old_name='link',
            new_name='link_thumbnail',
        ),
        migrations.AddField(
            model_name='api',
            name='link_original',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
