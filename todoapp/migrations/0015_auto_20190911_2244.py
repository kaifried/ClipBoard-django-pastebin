# Generated by Django 2.0.9 on 2019-09-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0014_auto_20190911_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='lang',
            field=models.CharField(choices=[('text', 'None'), ('c', 'C'), ('cpp', 'C++'), ('csharp', 'C#'), ('java', 'Java'), ('js', 'JavaScript'), ('php', 'PHP'), ('py', 'Python'), ('sql', 'SQL')], default='text', max_length=10),
        ),
    ]