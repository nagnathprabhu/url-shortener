
from config import *
from resources.url import UrlResource

# Add our endpoints to the API
api.add_resource(UrlResource, '/urls', '/urls/<string:short_url>')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)