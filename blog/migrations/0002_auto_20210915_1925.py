# Generated by Django 3.2.5 on 2021-09-15 16:25

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kategorimodel',
            options={'verbose_name': 'Kategori', 'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.CreateModel(
            name='YazilarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=50)),
                ('icerik', models.TextField()),
                ('olusturmaTarihi', models.DateTimeField(auto_now_add=True)),
                ('duzenlemeTarihi', models.DateTimeField(auto_now=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='baslik', unique=True)),
                ('resim', models.ImageField(upload_to='yazi_resimleri')),
                ('kategoriler', models.ManyToManyField(related_name='yazi', to='blog.KategoriModel')),
                ('yazar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yazilar', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Yazılar',
                'verbose_name_plural': 'Yazlar',
                'db_table': 'yazi',
            },
        ),
    ]
