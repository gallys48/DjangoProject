# Generated by Django 4.2.6 on 2023-11-16 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0004_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='Название страны')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatars/default.jpg', upload_to='avatars/%Y/%m/%d/', verbose_name='Аватар'),
        ),
        migrations.AddField(
            model_name='travel',
            name='country',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, to='travels.country', verbose_name='Страна путешествия'),
        ),
    ]
