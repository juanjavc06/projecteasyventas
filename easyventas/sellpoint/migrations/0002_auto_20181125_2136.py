# Generated by Django 2.1.2 on 2018-11-25 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellpoint', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('almacen', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Corte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total_vendido', models.IntegerField()),
                ('total_comprado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Corte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=200)),
                ('cantidad', models.IntegerField()),
                ('total', models.FloatField()),
                ('iva', models.FloatField()),
                ('corte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellpoint.Corte')),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('existencias', models.IntegerField()),
                ('producto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movimientos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=255)),
                ('producto', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Perfiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfil', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Productos_Proveedores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('costo_total', models.FloatField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellpoint.Productos')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores_Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_comencial', models.CharField(max_length=255)),
                ('rfc', models.CharField(max_length=18)),
                ('direccion', models.CharField(max_length=255)),
                ('tipo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuarios', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=100)),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellpoint.Perfiles')),
            ],
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='productos_proveedores',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellpoint.Proveedores_Clientes'),
        ),
        migrations.AddField(
            model_name='movimientos',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellpoint.Zona'),
        ),
        migrations.AddField(
            model_name='inventario',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellpoint.Zona'),
        ),
        migrations.AddField(
            model_name='almacen',
            name='zona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellpoint.Zona'),
        ),
        migrations.AddField(
            model_name='compras',
            name='proveedor',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='sellpoint.Proveedores_Clientes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ventas',
            name='cliente',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='sellpoint.Proveedores_Clientes'),
            preserve_default=False,
        ),
    ]
