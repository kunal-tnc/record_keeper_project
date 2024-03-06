# Generated by Django 5.0.2 on 2024-03-06 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record_keeper', '0003_alter_record_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the activity.', max_length=100, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='record',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record_keeper.activity'),
        ),
    ]