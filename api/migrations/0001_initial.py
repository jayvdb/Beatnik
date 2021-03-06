# Generated by Django 2.1.7 on 2019-08-04 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.TextField(null=True, verbose_name="Client's user agent")),
                ('ip_address', models.CharField(max_length=45, null=True, verbose_name="Client's IP address")),
                ('referer', models.URLField(null=True, verbose_name='HTTP referer')),
                ('query_string', models.TextField(verbose_name='Query string')),
                ('query', models.TextField(verbose_name="The 'q' parameter in the query")),
                ('path', models.TextField(null=True, verbose_name='The URL path')),
            ],
        ),
    ]
