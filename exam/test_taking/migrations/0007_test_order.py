# Generated by Django 2.0 on 2017-12-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_taking', '0006_auto_20171215_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='order',
            field=models.IntegerField(blank=True, null=True, verbose_name='顺序'),
        ),
    ]