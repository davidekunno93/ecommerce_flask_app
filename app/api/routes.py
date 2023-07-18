from flask import Blueprint
from ..models import Product


api = Blueprint("api", __name__, url_prefix="/api")

@api.get('/amiibos')
def amiibos():
    # (http://)127.0.0.1/api/amiibos
    amiibos = Product.query.all()
    amiibo_set = [amiibo.to_dict() for amiibo in amiibos]
    return {
        "status": "OK",
        "amiibo_set": amiibo_set
    }