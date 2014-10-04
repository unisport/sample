class Document(object):

    def __init__(self, **kwargs):
        """Constructor assigns all parameters as properties, as it seems to be large amount of
        possible parameters for a document, and they are so likely to change.
        """

        for item in kwargs:
            setattr(self, item, kwargs[item])

    @property
    def sortable_price(self):
        return float(self.price.replace(",", "."))  # for correct sorting
