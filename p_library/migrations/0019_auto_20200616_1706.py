# Generated by Django 3.0.7 on 2020-06-16 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0018_auto_20200616_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='friend_reader',
            field=models.ManyToManyField(related_name='reader', to='p_library.Friend'),
        ),
    ]
