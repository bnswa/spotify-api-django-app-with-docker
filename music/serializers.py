from rest_framework import serializers

class TopTrackSerializer(serializers.Serializer):
    track_name = serializers.CharField(max_length=200)
    artist = serializers.CharField(max_length=200)
    album = serializers.CharField(max_length=200)

class ArtistSerializer(serializers.Serializer):
    artist_id = serializers.CharField(max_length=200)
    artist_name = serializers.CharField(max_length=200)
    artist_genre = serializers.CharField(max_length=200)
