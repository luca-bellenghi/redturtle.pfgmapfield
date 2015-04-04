from Products.Archetypes.Widget import TypesWidget
from Products.Archetypes.Registry import registerWidget


class MapWidget(TypesWidget):
    """
    This widget draw collective.geo map in a form
    """

    _properties = TypesWidget._properties.copy()

    _properties.update({'macro': 'widgets/textarea',
                        },)

registerWidget(MapWidget,
               title='Map widget',
               description=('Renders map inside form',),
               used_for=('Products.Archetypes.Field.TextAreaField',)
               )
