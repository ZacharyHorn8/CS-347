import django.db.models.deletion
from django.db import migrations, models


def convert_languages(apps, schema_editor):
    Language = apps.get_model("catalog", "Language")

    # Get the existing language names from the Book table.
    with schema_editor.connection.cursor() as cursor:
        cursor.execute(
            "SELECT DISTINCT language FROM catalog_book "
            "WHERE language IS NOT NULL AND language != ''"
        )
        languages = [row[0] for row in cursor.fetchall()]

    # Create a Language row for each existing language name.
    for name in languages:
        Language.objects.get_or_create(name=name)

    # Replace the language names in catalog_book with the
    # corresponding Language IDs.
    with schema_editor.connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE catalog_book
            SET language = (
                SELECT id
                FROM catalog_language
                WHERE catalog_language.name = catalog_book.language
            )
            WHERE language IS NOT NULL AND language != ''
            """
        )


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_book_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=100)),
            ],
        ),

        migrations.RunPython(convert_languages),

        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to='catalog.language',
            ),
        ),
    ]
