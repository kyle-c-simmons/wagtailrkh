from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.core.blocks import (
  CharBlock, StructBlock, URLBlock, PageChooserBlock)


class HomePage(Page):
    templates = 'home/home_page.html'
    
    body = StreamField([
        ('paragraph', blocks.RichTextBlock(required=False)),
        ('image', ImageChooserBlock(icon="image", required=False)),
        ('gallary', blocks.StructBlock([
            ('title', CharBlock(required=False)),
            ('link', URLBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
        ], icon='xyz', required=False)),
        ('info', blocks.StructBlock([
            ('title', blocks.CharBlock(classname="full title", required=False)),
            ('body', blocks.RichTextBlock(required=False, features=[
                "blod", "ol"])),
            ('external_url', URLBlock(required=False)),
            ('internal_link', PageChooserBlock(required=False)),
        ], icon='user', required=False))
    ])
    
    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname='full'),
    ]
