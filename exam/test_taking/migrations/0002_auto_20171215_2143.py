# Generated by Django 2.0 on 2017-12-15 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_taking', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testdetail',
            options={'ordering': ['course_id', 'serial_number'], 'verbose_name': '考题', 'verbose_name_plural': '考题'},
        ),
        migrations.AddField(
            model_name='test',
            name='stage',
            field=models.CharField(blank=True, max_length=20, verbose_name='阶段'),
        ),
    ]