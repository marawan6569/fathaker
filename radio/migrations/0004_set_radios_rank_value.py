# Generated by Django 4.1.7 on 2024-03-22 22:44

from django.db import migrations


def ranking_radios(apps, schema_editor):
    """
    Set Category Value Rank To  autoincrement integer (a)  value
    """
    a = 1
    Radio = apps.get_model('radio', 'Radio')
    for radio in Radio.objects.all():
        radio.rank = a
        radio.save()
        a += 1


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0003_radio_rank'),
    ]

    operations = [
        migrations.RunPython(ranking_radios),
    ]