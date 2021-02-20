import graphene
from graphene_django import DjangoObjectType

from .models import Artist, Band, Genre, Subgenre, Song

class ArtistType(DjangoObjectType):
    class Meta:
        model = Artist
        fields = ("id", "name", "artists_songs")

class BandType(DjangoObjectType):
    class Meta:
        model = Band
        fields = ("id", "name", "bands_songs")

class SongType(DjangoObjectType):
    class Meta:
        model = Song
        fields = (
            "external_id",
            "name",
            "similar_band",
            "tag",
            "instrument",
            "band",
            "artist",
            "genre",
            "subgenre")

class Query(graphene.ObjectType):
    all_songs = graphene.List(SongType)
    band_by_name = graphene.Field(BandType, name=graphene.String(required=True))
    artist_by_name = graphene.Field(ArtistType, name=graphene.String(required=True))

    def resolve_all_songs(root, info):
        # We can easily optimize query count in the resolve method
        return Song.objects.select_related("artist").all()

    def resolve_artist_by_name(root, info, name):
        try:
            return Artist.objects.get(name=name)
        except Artist.DoesNotExist:
            return None

    def resolve_band_by_name(root, info, name):
        try:
            return Band.objects.get(name=name)
        except Band.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)
