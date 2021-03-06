# Generated by Django 3.2.6 on 2021-08-09 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('stena', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=25, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='mes',
            options={'ordering': ['-published'], 'verbose_name': 'Объявление', 'verbose_name_plural': 'Объявления'},
        ),
        migrations.AlterField(
            model_name='mes',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Содержание сообщения'),
        ),
        migrations.AlterField(
            model_name='mes',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Цена (если указана)'),
        ),
        migrations.AlterField(
            model_name='mes',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='mes',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='mes',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='stena.category',
                                    verbose_name='Категория'),
        ),
    ]
