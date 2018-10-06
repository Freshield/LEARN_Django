# Generated by Django 2.0.1 on 2018-03-23 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('weight', models.CharField(max_length=20, verbose_name='重量')),
                ('size', models.CharField(max_length=20, verbose_name='尺寸')),
            ],
            options={
                'permissions': (('visit_Product', 'Can visit Product'),),
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='序号')),
                ('type_name', models.CharField(max_length=20, verbose_name='产品类型')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='index.Type', verbose_name='产品类型'),
        ),
    ]
