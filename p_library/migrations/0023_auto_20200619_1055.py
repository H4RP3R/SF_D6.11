# Generated by Django 3.0.7 on 2020-06-19 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0022_auto_20200617_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='copy_count',
            field=models.SmallIntegerField(blank=True, default=0, verbose_name='Кол-во копий'),
        ),
        migrations.AlterField(
            model_name='book',
            name='friend_reader',
            field=models.ManyToManyField(blank=True, related_name='reader', to='p_library.Friend', verbose_name='Читающие друзья'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, verbose_name='Цена'),
        ),
    ]
