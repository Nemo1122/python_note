# Generated by Django 2.0 on 2017-12-15 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_taking', '0008_auto_20171215_2334'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testdetail',
            options={'ordering': ['course_id', 'level', 'serial_number'], 'verbose_name': '考题', 'verbose_name_plural': '考题'},
        ),
    ]
