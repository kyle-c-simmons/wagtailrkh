# Generated by Django 3.1.1 on 2020-09-11 09:38

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0052_pagelogentry'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image', required=False)), ('gallary', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('link', wagtail.core.blocks.URLBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))], icon='xyz', required=False)), ('info', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(classname='full title', required=False)), ('body', wagtail.core.blocks.RichTextBlock(features=['blod', 'ol'], required=False)), ('external_url', wagtail.core.blocks.URLBlock(required=False)), ('internal_link', wagtail.core.blocks.PageChooserBlock(required=False))], icon='user', required=False))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
