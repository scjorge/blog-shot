# Generated by Django 4.1.1 on 2022-10-09 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_created_post_updated_alter_post_title_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
