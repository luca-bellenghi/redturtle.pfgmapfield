from zope.i18nmessageid import MessageFactory
from redturtle.pfgmapfield import config, content

from Products.Archetypes import atapi
from Products.CMFCore import utils
from Products.CMFCore.permissions import setDefaultRoles
from Products.PloneFormGen.config import ADD_CONTENT_PERMISSION

MessageFactory = MessageFactory('redturtle.pfgmapfield')


def initialize(context):
    import widget

    content_types, constructors, ftis = atapi.process_types(
        atapi.listTypes(config.PROJECTNAME),
        config.PROJECTNAME)

    for atype, constructor in zip(content_types, constructors):
        utils.ContentInit(
            '%s: %s' % (config.PROJECTNAME, atype.portal_type),
            content_types=(atype,),
            permission=ADD_CONTENT_PERMISSION,
            extra_constructors=(constructor,),
        ).initialize(context)
