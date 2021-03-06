# Generated by Django 2.2.10 on 2020-09-17 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20200915_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority_lvl', models.IntegerField(choices=[(1, 'Высокий приоритет'), (2, 'Средний приоритет'), (3, 'Низкий приоритет')], default=2, verbose_name='Приоритет')),
                ('priority_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Приоритет',
            },
        ),
        migrations.AddField(
            model_name='todoitem',
            name='cl_priority',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cl_priority', to='tasks.Priority', verbose_name='Класс приоритета'),
        ),
    ]
