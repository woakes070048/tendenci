# Generated by Django 3.2.12 on 2022-12-11 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainings', '0003_outsideschool'),
    ]

    operations = [
        migrations.AddField(
            model_name='outsideschool',
            name='certification_track',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainings.certification'),
        ),
    ]