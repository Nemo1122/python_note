# Generated by Django 2.0 on 2017-12-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_taking', '0009_auto_20171215_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='status',
            field=models.CharField(choices=[('I', '无效'), ('V', '有效')], default='V', max_length=10, verbose_name='状态'),
        ),
        migrations.AddField(
            model_name='testdetail',
            name='status',
            field=models.CharField(choices=[('I', '无效'), ('V', '有效')], default='V', max_length=10, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='test',
            name='stage',
            field=models.CharField(blank=True, choices=[('F', '第一阶段'), ('S', '第二阶段'), ('T', '第三阶段')], max_length=10, verbose_name='阶段'),
        ),
        migrations.AlterField(
            model_name='testdetail',
            name='questions_type',
            field=models.CharField(choices=[('C', '选择题'), ('F', '填空题'), ('T', '判断题'), ('S', '简答题')], max_length=10, verbose_name='题目类型'),
        ),
    ]