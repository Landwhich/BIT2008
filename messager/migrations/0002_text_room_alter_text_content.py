# Generated by Django 5.1.3 on 2024-12-10 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='room',
            field=models.CharField(default='garbage-collect', max_length=50),
        ),
        migrations.AlterField(
            model_name='text',
            name='content',
            field=models.TextField(),
        ),
    ]
