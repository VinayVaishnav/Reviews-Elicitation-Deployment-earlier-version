# Generated by Django 4.2.1 on 2023-06-24 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_review_communication_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_rating_1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_rating_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='review_rating_3',
            field=models.IntegerField(default=0),
        ),
    ]