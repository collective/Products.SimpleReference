"""Definition of the SimpleReference content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from Products.SimpleReference.interfaces import ISimpleReference
from Products.SimpleReference.config import PROJECTNAME
from Products.SimpleReference import SimpleReferenceMessageFactory as _


SimpleReferenceSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    atapi.ReferenceField(
        title=_(u"Reference"),
        relationship='simplereference',
    ),

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

SimpleReferenceSchema['title'].storage = atapi.AnnotationStorage()
SimpleReferenceSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(SimpleReferenceSchema, moveDiscussion=False)


class SimpleReference(base.ATCTContent):
    """Reference Item for RichDocument"""
    implements(ISimpleReference)

    meta_type = "SimpleReference"
    schema = SimpleReferenceSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(SimpleReference, PROJECTNAME)
