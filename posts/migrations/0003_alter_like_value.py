# Generated by Django 4.0.3 on 2022-04-04 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], max_length=8),
        ),
    ]
