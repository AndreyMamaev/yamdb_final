# Generated by Django 2.2.16 on 2022-05-05 07:19

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_auto_20220505_1017'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-pub_date']},
        ),
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reviews.Review', verbose_name='Комментируемый отзыв'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='text',
            field=models.TextField(verbose_name='Текст комметария'),
        ),
        migrations.AlterField(
            model_name='review',
            name='score',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, message='Оценка должна быть больше 1.'), django.core.validators.MaxValueValidator(10, message='Оценка должна быть меньше 10.')], verbose_name='Оценка произведения'),
        ),
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(verbose_name='Текст отзыва'),
        ),
        migrations.AlterField(
            model_name='review',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.Title', verbose_name='Оцениваемое произведение'),
        ),
    ]
