# Generated by Django 3.2.5 on 2022-01-19 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salesperson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('image', models.ImageField(blank=True, upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=None)),
                ('sent_time', models.DateTimeField(auto_now_add=True)),
                ('salesperson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salesperson', to='rate.salesperson')),
            ],
        ),
    ]
