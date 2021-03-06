# Generated by Django 2.0 on 2017-12-15 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_taking', '0007_test_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='test',
            options={'ordering': ['order'], 'verbose_name': '考试科目', 'verbose_name_plural': '考试科目'},
        ),
        migrations.AddField(
            model_name='testdetail',
            name='level',
            field=models.IntegerField(default=1, verbose_name='试题等级'),
        ),
        migrations.AddField(
            model_name='testdetail',
            name='parent',
            field=models.IntegerField(default=0, verbose_name='父级ID'),
        ),
    ]
