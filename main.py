from flask import Flask, jsonify, request
from ytmusicapi import YTMusic

app = Flask(__name__)

# Initialize YTMusic API
ytmusic = YTMusic()

# ========================== API ENDPOINTS ============================

# 1. Search songs, albums, artists, playlists
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    search_filter = request.args.get('filter', None)  # Options: 'songs', 'videos', 'albums', 'artists', etc.
    results = ytmusic.search(query, filter=search_filter)
    return jsonify(results)


# 2. Get song details by song ID
@app.route('/song/<song_id>', methods=['GET'])
def get_song(song_id):
    song_info = ytmusic.get_song(song_id)
    return jsonify(song_info)


# 3. Get charts (Top songs, Trending, Top Playlists) based on country
@app.route('/charts', methods=['GET'])
def get_charts():
    country = request.args.get('country', 'US')  # Default to US charts if country not provided
    charts = ytmusic.get_charts(country=country)
    return jsonify(charts)


# 4. Get playlist details (All songs in the playlist)
@app.route('/playlist/<playlist_id>', methods=['GET'])
def get_playlist(playlist_id):
    playlist = ytmusic.get_playlist(playlist_id)
    return jsonify(playlist)


# 5. Get album details by album ID (All songs in an album)
@app.route('/album/<album_id>', methods=['GET'])
def get_album(album_id):
    album = ytmusic.get_album(album_id)
    return jsonify(album)


# 6. Get artist details by artist ID (Top songs, albums, singles, related artists)
@app.route('/artist/<artist_id>', methods=['GET'])
def get_artist(artist_id):
    artist = ytmusic.get_artist(artist_id)
    return jsonify(artist)


# 7. Get lyrics for a song by song ID
@app.route('/lyrics/<song_id>', methods=['GET'])
def get_lyrics(song_id):
    song = ytmusic.get_song(song_id)
    lyrics = song.get('lyrics', 'No lyrics available')
    return jsonify({"lyrics": lyrics})


# 8. Get Trending Music Videos
@app.route('/trending', methods=['GET'])
def get_trending():
    trending_videos = ytmusic.get_trending()
    return jsonify(trending_videos)


# 9. Get Recommendations
@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    song_id = request.args.get('song_id', None)
    artist_id = request.args.get('artist_id', None)
    recommendations = ytmusic.get_recommendations(song_id=song_id, artist_id=artist_id)
    return jsonify(recommendations)


# 10. Get Music Genres
@app.route('/genres', methods=['GET'])
def get_genres():
    genres = ytmusic.get_music_genres()
    return jsonify(genres)


# 11. Get Playlist Sections
@app.route('/playlist_sections/<playlist_id>', methods=['GET'])
def get_playlist_sections(playlist_id):
    playlist_sections = ytmusic.get_playlist_sections(playlist_id)
    return jsonify(playlist_sections)


# 12. Get Album Recommendations
@app.route('/album_recommendations/<album_id>', methods=['GET'])
def get_album_recommendations(album_id):
    album_recommendations = ytmusic.get_album_recommendations(album_id)
    return jsonify(album_recommendations)


# 13. Get Song Comments
@app.route('/song_comments/<song_id>', methods=['GET'])
def get_song_comments(song_id):
    comments = ytmusic.get_song_comments(song_id)
    return jsonify(comments)


# 14. Get User Playlists (Public Playlists)
@app.route('/user_playlists', methods=['GET'])
def get_user_playlists():
    playlists = ytmusic.get_user_playlists()
    return jsonify(playlists)


# ======================== RUN SERVER ==============================

if __name__ == '__main__':
    app.run(debug=True)
