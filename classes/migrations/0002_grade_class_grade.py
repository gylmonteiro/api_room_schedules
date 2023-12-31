# Generated by Django 5.0 on 2023-12-20 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('period', models.CharField(blank=True, choices=[('M', 'MANHÃ'), ('T', 'TARDE'), ('N', 'NOITE'), ('I', 'INTEGRAL')], max_length=1, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.grade'),
        ),
    ]
