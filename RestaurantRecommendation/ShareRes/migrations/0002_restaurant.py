# Generated by Django 3.2.4 on 2021-06-25 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShareRes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant_name', models.CharField(max_length=100)),
                ('restaurant_link', models.CharField(max_length=500)),
                ('restaurant_content', models.TextField()),
                ('restaurant_keyword', models.CharField(max_length=50)),
                ('category', models.ForeignKey(default=3, on_delete=django.db.models.deletion.SET_DEFAULT, to='ShareRes.category')),
            ],
        ),
    ]
