# Generated by Django 2.0 on 2017-12-19 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test_taking', '0011_auto_20171219_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranswer',
            name='create_time',
            field=models.DateField(auto_now=True, verbose_name='答题时间'),
        ),
        migrations.AddField(
            model_name='useranswer',
            name='create_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_user', to=settings.AUTH_USER_MODEL, verbose_name='答题者'),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='update_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='update_user', to=settings.AUTH_USER_MODEL, verbose_name='修改者'),
        ),
    ]
