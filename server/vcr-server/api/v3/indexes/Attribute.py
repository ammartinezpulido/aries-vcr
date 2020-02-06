import logging

from haystack import indexes

from api.v2.models.Attribute import Attribute as AttributeModel
from api.v2.search.index import TxnAwareSearchIndex

LOGGER = logging.getLogger(__name__)


class AttributeIndex(TxnAwareSearchIndex, indexes.Indexable):
    document = indexes.CharField(document=True)

    name_text = indexes.CharField(model_attr="text")
    name_language = indexes.CharField(model_attr="language", null=True)
    name_type = indexes.CharField(model_attr="type")

    def get_model(self):
        return NameModel
