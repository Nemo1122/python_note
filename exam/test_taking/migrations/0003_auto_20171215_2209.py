# Generated by Django 2.0 on 2017-12-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_taking', '0002_auto_20171215_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdetail',
            name='questions_type',
            field=models.CharField(choices=[('c', '选择题'), ('g', '填空题'), ('t', '判断题'), ('s', '简答题')], max_length=20, verbose_name='题目类型'),
        ),
    ]
