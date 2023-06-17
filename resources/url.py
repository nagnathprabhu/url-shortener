from flask_restful import Resource, reqparse
from config import r
from models.url import *
from flask import jsonify, redirect
from utilities import generate_short_url


class UrlResource(Resource):
    def get(self, short_url):
        url = ''
        if r.exists(short_url):
            url = r.get(short_url).decode()
        else:
            url_object = Url.query.filter_by(short_url=short_url).first_or_404()
            url = url_object.long_url
            r.set(short_url, url)
            r.expire(short_url, 300)
        return redirect(url)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('long_url', type=str, required=True)
        args = parser.parse_args()

        # Generate a random 6-character string for the short URL
        # To-Do: make the short url generation be a service of it's own to avoid duplicates
        short_url = generate_short_url()

        url = Url(long_url=args['long_url'], short_url=short_url)
        db.session.add(url)
        db.session.commit()

        url_schema = UrlSchema()
        url = jsonify(url_schema.dump(url))
        if r.exists(url.short_url):
            pass
        else:
            r.set(url.short, url.long_url)
            r.expire(url.short, 300)
        return url
