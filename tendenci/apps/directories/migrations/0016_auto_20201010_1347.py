# Generated by Django 2.2.16 on 2020-10-10 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directories', '0015_auto_20201007_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('position',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='position',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Position'),
        ),
    ]