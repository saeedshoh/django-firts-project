# Generated by Django 4.1.3 on 2022-12-15 16:52

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('parent', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='testapp.rubrik')),
            ],
        ),
    ]
