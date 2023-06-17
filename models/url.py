from config import db, SQLAlchemyAutoSchema


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Url {self.short_url}>'


# Create our Marshmallow schema
class UrlSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Url
