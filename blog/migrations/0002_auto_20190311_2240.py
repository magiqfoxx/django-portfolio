# Generated by Django 2.0.2 on 2019-03-11 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(max_length=10000),
        ),
    ]
