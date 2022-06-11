# Generated by Django 4.0.5 on 2022-06-11 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cmnt', models.TextField(blank=True, max_length=200)),
                ('commentedon', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogapp.blog')),
            ],
        ),
    ]
