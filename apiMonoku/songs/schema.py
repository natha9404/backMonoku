import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Artist, Band, Song

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

class SongNode(DjangoObjectType):
    class Meta:
        model = Song
        # Allow for some more advanced filtering here
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'genre': ['exact', 'icontains', 'istartswith'],
            'subgenre': ['exact', 'icontains', 'istartswith'],
            'similar_band': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    all_songs = graphene.List(SongType)
    all_songs2 = DjangoFilterConnectionField(SongNode)    
    band_by_name = graphene.List(BandType, name=graphene.String(required=True))
    artist_by_name = graphene.List(ArtistType, name=graphene.String(required=True))

    def resolve_all_songs(root, info):
        # We can easily optimize query count in the resolve method
        return Song.objects.select_related("artist").all()

    def resolve_artist_by_name(root, info, name):
        try:
            return Artist.objects.filter(name=name)
        except Artist.DoesNotExist:
            return None

    def resolve_band_by_name(root, info, name):
        try:
            return Band.objects.filter(name=name)
        except Band.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)
