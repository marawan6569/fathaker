# Generated by Django 4.1.7 on 2023-03-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_navlink_path_navlink_destination_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navlink',
            name='icon',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='FontAwesome Icon Class'),
        ),
    ]
