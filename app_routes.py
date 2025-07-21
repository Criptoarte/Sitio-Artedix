from flask import Blueprint, jsonify, request
from models import Artist, NFT
from mongoengine.connection import get_db

bp = Blueprint('routes', __name__)

# Ruta raíz de prueba
@bp.route('/')
def index():
    return jsonify({"message": "API de Artedix funcionando correctamente"}), 200

# ------------------- ARTIST -------------------

@bp.route('/artists', methods=['GET'])
def get_artists():
    artists = Artist.objects()
    return jsonify([{
        "id": str(artist.id),
        "name": artist.name,
        "about": artist.about,
        "email": artist.email
    } for artist in artists]), 200

@bp.route('/artists/<string:artist_id>', methods=['GET'])
def get_artist_by_id(artist_id):
    artist = Artist.objects(id=artist_id).first()
    if not artist:
        return jsonify({"error": "Artista no encontrado"}), 404
    return jsonify({
        "id": str(artist.id),
        "name": artist.name,
        "about": artist.about,
        "email": artist.email
    }), 200

@bp.route('/artists', methods=['POST'])
def create_artist():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Faltan campos requeridos (name, email)"}), 400
    artist = Artist(
        name=data["name"],
        about=data.get("about", ""),
        email=data["email"]
    )
    artist.save()
    return jsonify({"message": "Artista creado", "id": str(artist.id)}), 201

@bp.route('/artists/<string:artist_id>', methods=['PUT'])
def update_artist(artist_id):
    artist = Artist.objects(id=artist_id).first()
    if not artist:
        return jsonify({"error": "Artista no encontrado"}), 404
    data = request.get_json()
    artist.name = data.get("name", artist.name)
    artist.about = data.get("about", artist.about)
    artist.email = data.get("email", artist.email)
    artist.save()
    return jsonify({"message": "Artista actualizado"}), 200

@bp.route('/artists/<string:artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    artist = Artist.objects(id=artist_id).first()
    if not artist:
        return jsonify({"error": "Artista no encontrado"}), 404
    artist.delete()
    return jsonify({"message": "Artista eliminado"}), 200

# ------------------- NFT -------------------

@bp.route('/nfts', methods=['GET'])
def get_nfts():
    nfts = NFT.objects()
    return jsonify([{
        "id": str(nft.id),
        "name": nft.name,
        "price": nft.price,
        "category": nft.category,
        "file": nft.file
    } for nft in nfts]), 200

@bp.route('/nfts/<string:nft_id>', methods=['GET'])
def get_nft_by_id(nft_id):
    nft = NFT.objects(id=nft_id).first()
    if not nft:
        return jsonify({"error": "NFT no encontrado"}), 404
    return jsonify({
        "id": str(nft.id),
        "name": nft.name,
        "price": nft.price,
        "category": nft.category,
        "file": nft.file
    }), 200

@bp.route('/nfts', methods=['POST'])
def create_nft():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("price"):
        return jsonify({"error": "Faltan campos requeridos (name, price)"}), 400
    nft = NFT(
        name=data["name"],
        price=float(data["price"]),
        category=data.get("category", ""),
        file=data.get("file", "")
    )
    nft.save()
    return jsonify({"message": "NFT creado", "id": str(nft.id)}), 201

@bp.route('/nfts/<string:nft_id>', methods=['PUT'])
def update_nft(nft_id):
    nft = NFT.objects(id=nft_id).first()
    if not nft:
        return jsonify({"error": "NFT no encontrado"}), 404
    data = request.get_json()
    nft.name = data.get("name", nft.name)
    nft.price = float(data.get("price", nft.price))
    nft.category = data.get("category", nft.category)
    nft.file = data.get("file", nft.file)
    nft.save()
    return jsonify({"message": "NFT actualizado"}), 200

@bp.route('/nfts/<string:nft_id>', methods=['DELETE'])
def delete_nft(nft_id):
    nft = NFT.objects(id=nft_id).first()
    if not nft:
        return jsonify({"error": "NFT no encontrado"}), 404
    nft.delete()
    return jsonify({"message": "NFT eliminado"}), 200

# ------------------- RAW TEST -------------------

@bp.route('/test_raw', methods=['GET'])
def test_raw():
    db_conn = get_db()
    result = list(db_conn['artist'].find())
    for doc in result:
        doc['_id'] = str(doc['_id'])
    return jsonify(result), 200