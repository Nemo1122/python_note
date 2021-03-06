# Generated by Django 2.0 on 2017-12-15 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_taking', '0003_auto_20171215_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='stage',
            field=models.CharField(blank=True, choices=[(1, '第一阶段'), (2, '第二阶段'), (3, '第三阶段')], max_length=20, verbose_name='阶段'),
        ),
        migrations.AlterField(
            model_name='testdetail',
            name='answer',
            field=models.TextField(blank=True, default='', verbose_name='标准答案'),
        ),
    ]
