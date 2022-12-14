# Generated by Django 4.1.1 on 2022-11-30 13:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Persona",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gov_id",
                    models.CharField(
                        max_length=50,
                        unique=True,
                        verbose_name="documento de identidad",
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profiles",
                        verbose_name="foto de perfil",
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="correo electrónico"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="nombres"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="apellidos"
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="ciudad"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="número de teléfono",
                    ),
                ),
                (
                    "dependency",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("1", "Rectorado - Gabinete"),
                            ("2", "Vice Rectorado"),
                            ("3", "Rectorado - Secretaria General"),
                            ("4", "Rectorado - Asesoría Jurídica"),
                            ("5", "Rectorado - Auditoría General"),
                            ("6", "Rectorado - DGA"),
                            ("7", "Rectorado - DGAyF"),
                            ("8", "Rectorado - DGEU"),
                            ("9", "Rectorado - DGICT"),
                            ("10", "Rectorado - DGGyTH"),
                            ("11", "Rectorado - DGOTI"),
                            ("12", "Rectorado - DGPD"),
                            ("13", "Rectorado - DGP"),
                            ("14", "Rectorado - DGPRI"),
                            ("15", "CNC - UNA"),
                            ("16", "CNEA - UNA"),
                            ("17", "CEMIT - UNA"),
                            ("18", "CETTRI - UNA"),
                            ("19", "IICS - UNA"),
                            ("20", "Biblioteca Central"),
                            ("21", "INCUNA"),
                            ("22", "UA - FDCS"),
                            ("23", "UA - FCM"),
                            ("24", "UA - FI"),
                            ("25", "UA - FCE"),
                            ("26", "UA - FO"),
                            ("27", "UA - FCQ"),
                            ("28", "UA - FCA"),
                            ("29", "UA - FF"),
                            ("30", "UA - FCV"),
                            ("31", "UA - FADA"),
                            ("32", "UA - FP"),
                            ("33", "UA - FACEN"),
                            ("34", "UA - FENOB"),
                            ("35", "UA - FACSO"),
                        ],
                        max_length=2,
                        null=True,
                        verbose_name="dependencia",
                    ),
                ),
                (
                    "vinc_type",
                    models.CharField(
                        blank=True,
                        choices=[("1", "Contratado"), ("2", "Permanente")],
                        max_length=1,
                        null=True,
                        verbose_name="tipo de vinculación",
                    ),
                ),
            ],
            options={
                "verbose_name": "persona",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="nombre de usuario"
                    ),
                ),
                (
                    "persona",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="users.persona",
                    ),
                ),
                (
                    "role",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Director"),
                            (2, "Analista"),
                            (3, "Cliente"),
                            (4, "Técnico"),
                        ],
                        default=3,
                        verbose_name="rol",
                    ),
                ),
                ("is_staff", models.BooleanField(default=False, verbose_name="staff")),
                ("is_active", models.BooleanField(default=True, verbose_name="activo")),
                (
                    "date_joined",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "usuario",
                "ordering": ["-date_joined"],
            },
        ),
    ]
