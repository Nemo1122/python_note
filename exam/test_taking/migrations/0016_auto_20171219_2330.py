# Generated by Django 2.0 on 2017-12-19 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_taking', '0015_auto_20171219_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='create_time',
            field=models.DateTimeField(auto_now=True, verbose_name='答题时间'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='update_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='修改时间'),
        ),
    ]
