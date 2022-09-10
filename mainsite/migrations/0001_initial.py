# Generated by Django 4.0.6 on 2022-08-16 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=50)),
                ('book_description', models.CharField(max_length=500)),
                ('book_genre', models.CharField(max_length=50)),
                ('book_price', models.PositiveSmallIntegerField(default=0)),
                ('book_image', models.ImageField(default='', upload_to='images/')),
                ('book_rate_apple', models.FloatField(default=0)),
                ('book_rate_android', models.FloatField(default=0)),
                ('book_rate_site', models.FloatField(default=0)),
                ('book_show_order', models.PositiveSmallIntegerField(default=0)),
                ('book_free_audio_fragment', models.FileField(default='', upload_to='audio/')),
                ('book_free_pdf_fragment', models.FileField(default='', upload_to='books/pdf/')),
                ('book_free_single_html_fragment', models.FileField(default='', upload_to='books/')),
            ],
        ),
    ]