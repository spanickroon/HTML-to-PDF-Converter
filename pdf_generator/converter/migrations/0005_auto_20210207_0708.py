# Generated by Django 3.1.6 on 2021-02-07 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0004_auto_20210207_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processingrequest',
            name='final_file',
            field=models.FileField(blank=True, default='example.pdf', null=True, upload_to='documents/pdf', verbose_name='Итоговый файл pdf'),
        ),
    ]
