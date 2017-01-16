from wtforms import Form, StringField, FloatField, RadioField, BooleanField
from wtforms.validators import DataRequired, URL, NumberRange


class ProductForm(Form):
    currency = RadioField('Currency', [DataRequired()],
                          choices=[('DKK', 'Denmark Krone'), ('EUR', 'Euro')])
    delivery = RadioField('Delivery', [DataRequired()],
                          choices=[('1-2 dage', '1-2 dage'),
                                   ('2-3 dage', '2-3 dage')])
    kids = BooleanField('Kids', default=0)
    name = StringField('Name', [DataRequired()])
    package = BooleanField('Package', default=False)
    kid_adult = BooleanField('Kid adult', default=0)
    free_porto = BooleanField('Free porto', default=0)
    image = StringField('Image', [URL(require_tld=False)])
    sizes = StringField('Sizes', [DataRequired()], default='One Size')
    price = FloatField('Price', [NumberRange(min=0)], default=float(0))
    url = StringField('URL', [URL()])
    online = BooleanField('Online', default=0)
    price_old = FloatField('Price Old', [NumberRange(min=0)], default=float(0))
    img_url = StringField('Image url', [URL(require_tld=False)])
    women = BooleanField('Women', default=0)
