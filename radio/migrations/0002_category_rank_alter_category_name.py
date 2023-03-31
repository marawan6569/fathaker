# Generated by Django 4.1.7 on 2023-03-31 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='rank',
            field=models.IntegerField(blank=True, null=True, verbose_name='Category Rank'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30, verbose_name='Category Name'),
        ),
    ]