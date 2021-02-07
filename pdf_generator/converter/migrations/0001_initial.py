# Generated by Django 3.1.6 on 2021-02-07 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkInternetResource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, max_length=256, unique=True, verbose_name='Ссылка на ресурс для преобразования')),
            ],
            options={
                'verbose_name': 'Ссылка на интернет ресурс',
                'verbose_name_plural': 'Ссылки на интернет ресурс',
            },
        ),
        migrations.CreateModel(
            name='ProcessingRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_datetime', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата создания заявки')),
                ('done_datetime', models.DateTimeField(blank=True, null=True, verbose_name='Дата завершения заявки')),
                ('conversion_file_link', models.FileField(blank=True, null=True, upload_to='documents/html', verbose_name='Html файл для конвертирования')),
                ('status', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'В ожидании'), (2, 'В процессе'), (3, 'Готово')], null=True, verbose_name='Статус заявки')),
                ('final_file', models.FileField(blank=True, unique=True, upload_to='documents/pdf', verbose_name='Итоговый файл pdf')),
                ('resulting_file_size', models.IntegerField(blank=True, null=True, verbose_name='Размер итогового файла')),
                ('conversion_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='converter.linkinternetresource', verbose_name='Ссылка на ресурс для конвертирования')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Получатель')),
            ],
            options={
                'verbose_name': 'Заявка на преобразование в pdf',
                'verbose_name_plural': 'Заявки на преобразование в pdf',
            },
        ),
    ]