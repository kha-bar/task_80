# Generated by Django 4.0.6 on 2022-08-08 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news_db', '0001_initial'),
        ('news_app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='news_db.author')),
            ],
            bases=('news_db.author',),
        ),
    ]
