# Generated by Django 2.2.10 on 2020-09-17 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20200917_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='cl_priority',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cl_priority', to='tasks.Priority', verbose_name='Класс приоритета'),
        ),
    ]