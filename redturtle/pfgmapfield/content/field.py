from Products.PloneFormGen.content.fields import FGStringField
from Products.ATContentTypes.content.base import registerATCT
from redturtle.pfgmapfield.config import PROJECTNAME


class FormMapField(FGStringField):

    portal_type = meta_type = 'FormMapField'
    archetype_name = 'Form Map Field'

registerATCT(FormMapField, PROJECTNAME)
