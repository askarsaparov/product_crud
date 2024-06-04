from django_elasticsearch_dsl import Document, Index, fields

from .models import Product, Category

# Define the index
product_index = Index('products')

# Define the settings of the index
product_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@product_index.doc_type
class ProductDocument(Document):
    category = fields.NestedField(properties={
        'title': fields.TextField(),
    })

    class Django:
        model = Product  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'id',
            'title',
            'description',
            'price',
            'image',
        ]

        # Related fields to be indexed
        related_models = [Category]

    def get_queryset(self):
        """Not mandatory but to improve performance we can select related in one sql request"""
        return super(ProductDocument, self).get_queryset().select_related(
            'category'
        )

    def get_instances_from_related(self, related_instance):
        """If related_models is set, define how to retrieve the related model instances"""
        if isinstance(related_instance, Category):
            return related_instance.products.all()

    def to_dict(self, include_meta=False, skip_empty=True):
        data = super(ProductDocument, self).to_dict(include_meta, skip_empty)
        data['image'] = self.image.url
        print("self.image.url")
        print(self.image.url)
        return data
