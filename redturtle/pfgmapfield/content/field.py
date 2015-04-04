from Products.PloneFormGen.content.fields import BaseFormField
from Products.ATContentTypes.content.base import registerATCT
from redturtle.pfgmapfield.config import PROJECTNAME
from redturtle.pfgmapfield.widget import MapWidget
from Products.PloneFormGen.content.fields import PlainTextField
from Products.CMFCore.permissions import View


class FormMapField(BaseFormField):

    portal_type = meta_type = 'FormMapField'
    archetype_name = 'Form Map Field'

    def __init__(self, oid, **kwargs):
        """ initialize class """
        BaseFormField.__init__(self, oid, **kwargs)
        self.widget = MapWidget()
        self.fgField = PlainTextField('fg_text_field',
            searchable=0,
            required=0,
            write_permission=View,
            default_content_type='text/plain',
            allowable_content_types=('text/plain',),
            widget=MapWidget()
            )

registerATCT(FormMapField, PROJECTNAME)
