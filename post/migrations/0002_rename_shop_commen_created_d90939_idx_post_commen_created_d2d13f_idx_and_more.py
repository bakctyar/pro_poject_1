# Generated by Django 5.0.2 on 2024-02-12 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameIndex(
            model_name='comment',
            new_name='post_commen_created_d2d13f_idx',
            old_name='shop_commen_created_d90939_idx',
        ),
        migrations.RenameIndex(
            model_name='post',
            new_name='post_post_publish_2758a7_idx',
            old_name='shop_post_publish_1785cc_idx',
        ),
    ]