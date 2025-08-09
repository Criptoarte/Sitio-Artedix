from flask import Blueprint, jsonify, request
from models import Artist, Artwork

bp = Blueprint('routes', __name__)

# ------------------- ARTIST -------------------

@bp.route('/artists', methods=['GET'])
def get_artists():
    artists = Artist.objects()
    return jsonify([{
        "id": str(artist.id),
        "name": artist.name,
        "about": artist.about,
        "email": artist.email,
        "portfolio_link": artist.portfolio_link
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
        "email": artist.email,
        "portfolio_link": artist.portfolio_link
    }), 200

@bp.route('/artists', methods=['POST'])
def create_artist():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("email"):
        return jsonify({"error": "Faltan campos requeridos (name, email)"}), 400
    
    artist = Artist(
        name=data["name"],
        about=data.get("about", ""),
        email=data["email"],
        portfolio_link=data.get("portfolio_link", "")
    )
    artist.save()
    return jsonify({
        "message": "Artista creado exitosamente", 
        "id": str(artist.id),
        "name": artist.name,
        "email": artist.email
    }), 201

@bp.route('/artists/<string:artist_id>', methods=['PUT'])
def update_artist(artist_id):
    artist = Artist.objects(id=artist_id).first()
    if not artist:
        return jsonify({"error": "Artista no encontrado"}), 404
    data = request.get_json()
    artist.name = data.get("name", artist.name)
    artist.about = data.get("about", artist.about)
    artist.email = data.get("email", artist.email)
    artist.portfolio_link = data.get("portfolio_link", artist.portfolio_link)
    artist.save()
    return jsonify({"message": "Artista actualizado exitosamente"}), 200

@bp.route('/artists/<string:artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
    artist = Artist.objects(id=artist_id).first()
    if not artist:
        return jsonify({"error": "Artista no encontrado"}), 404
    artist.delete()
    return jsonify({"message": "Artista eliminado exitosamente"}), 200

# ------------------- ARTWORK -------------------
@bp.route('/artworks', methods=['OPTIONS'])
def handle_artworks_options():
    return '', 200

@bp.route('/artworks', methods=['POST'])
def create_artwork():
    data = request.get_json()
    if not data or not data.get("name") or not data.get("artist_id"):
        return jsonify({"error": "Faltan campos requeridos (name, artist_id)"}), 400

    artwork = Artwork(
        name=data["name"],
        quantity=int(data.get("quantity", 1)),
        artist_id=data["artist_id"]
    )
    artwork.save()
    return jsonify({
        "message": "Artwork creado exitosamente", 
        "id": str(artwork.id),
        "name": artwork.name,
        "quantity": artwork.quantity,
        "artist_id": artwork.artist_id
    }), 201

@bp.route('/artworks', methods=['GET'])
def get_artworks():
    artworks = Artwork.objects()
    return jsonify([{
        "id": str(art.id),
        "name": art.name,
        "quantity": art.quantity,
        "artist_id": art.artist_id
    } for art in artworks]), 200

@bp.route('/artworks/<string:artwork_id>', methods=['GET'])
def get_artwork_by_id(artwork_id):
    artwork = Artwork.objects(id=artwork_id).first()
    if not artwork:
        return jsonify({"error": "Artwork no encontrado"}), 404
    return jsonify({
        "id": str(artwork.id),
        "name": artwork.name,
        "quantity": artwork.quantity,
        "artist_id": artwork.artist_id
    }), 200

@bp.route('/artworks/artist/<string:artist_id>', methods=['GET'])
def get_artworks_by_artist(artist_id):
    artworks = Artwork.objects(artist_id=artist_id)
    return jsonify([{
        "id": str(art.id),
        "name": art.name,
        "quantity": art.quantity,
        "artist_id": art.artist_id
    } for art in artworks]), 200
