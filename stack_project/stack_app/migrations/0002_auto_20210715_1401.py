# Generated by Django 3.2.5 on 2021-07-15 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stack_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='score',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='questions',
            name='view_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]