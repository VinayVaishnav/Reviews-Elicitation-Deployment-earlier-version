# Generated by Django 4.2.1 on 2023-06-24 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_rename_problem_sol_review_problem_solving_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='communication',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='problem_solving',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='review',
            name='sociability',
            field=models.TextField(default='', max_length=1000),
        ),
    ]
