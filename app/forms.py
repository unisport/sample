from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired

#WTF-form for creating a new product
class CreateProduct(FlaskForm):
    image = StringField('Image URL', validators=[DataRequired()])
    name = StringField('Product name', validators=[DataRequired()])
    price = IntegerField('Product price', validators=[DataRequired()])
    submit = SubmitField('Create product')


#WTF.form for editing an already existing product.
class EditProduct(FlaskForm):
    image = StringField('Image URL', validators=[DataRequired()])
    name = StringField('Product name', validators=[DataRequired()])
    price = IntegerField('Product price', validators=[DataRequired()])
    submit = SubmitField('Submit changes')
