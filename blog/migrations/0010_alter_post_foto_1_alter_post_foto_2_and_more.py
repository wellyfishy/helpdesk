# Generated by Django 4.0.3 on 2022-05-31 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_foto_default_alter_post_foto_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='foto_1',
            field=models.ImageField(blank=True, null=True, upload_to='POST/sebelum/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='foto_2',
            field=models.ImageField(blank=True, null=True, upload_to='POST/sesudah/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='foto_default',
            field=models.ImageField(blank=True, default='notfound.jpg', null=True, upload_to=''),
        ),
    ]
