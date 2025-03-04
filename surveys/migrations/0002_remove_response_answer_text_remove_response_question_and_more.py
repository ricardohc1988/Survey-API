# Generated by Django 5.0.7 on 2024-07-09 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='answer_text',
        ),
        migrations.RemoveField(
            model_name='response',
            name='question',
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.question')),
            ],
        ),
        migrations.AddField(
            model_name='response',
            name='choice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='surveys.choice'),
            preserve_default=False,
        ),
    ]
