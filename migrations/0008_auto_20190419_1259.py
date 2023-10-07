# Generated by Django 2.0.8 on 2019-04-19 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('socialissue', '0007_auto_20190419_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='user_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialissue.Post'),
        ),
        migrations.AlterField(
            model_name='votes_comments',
            name='user_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialissue.Post'),
        ),
    ]
