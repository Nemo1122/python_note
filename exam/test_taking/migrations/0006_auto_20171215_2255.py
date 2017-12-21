# Generated by Django 2.0 on 2017-12-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_taking', '0005_auto_20171215_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='stage',
            field=models.CharField(blank=True, choices=[('F', '第一阶段'), ('S', '第二阶段'), ('T', '第三阶段')], max_length=20, verbose_name='阶段'),
        ),
        migrations.AlterField(
            model_name='testdetail',
            name='questions_type',
            field=models.CharField(choices=[('C', '选择题'), ('F', '填空题'), ('T', '判断题'), ('S', '简答题')], max_length=20, verbose_name='题目类型'),
        ),
    ]
