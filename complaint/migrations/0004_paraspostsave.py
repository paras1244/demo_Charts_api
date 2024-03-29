# Generated by Django 4.1 on 2023-02-02 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complaint', '0003_alter_complaint_unique_together'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParasPostSave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validation_code', models.CharField(blank=True, max_length=10, null=True)),
                ('complaint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='complaint.complaint')),
            ],
        ),
    ]
