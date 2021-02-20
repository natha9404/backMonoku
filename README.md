Uso de Queries y Mutaciones:

Get all songs and by genre,subgenre and similar band:
query {
  allSongsFilter(genre:"pop"){
    edges {
      node {
        name,
        similarBand,
        instrument
      }
    }
  }
}


Find Bands:
query {
  bandByName(name:"rbd"){
    name,
    bandsSongs{
      name,
      instrument,
      tag
    }
  }
}

Find Artists: 
query {
  artistByName(name:"dulce maria"){
    name,
    artistsSongs{
      edges{
        node{
          name,
          subgenre,
          genre,
          tag,
          instrument
        }
      }
    }
  }
}

Create Artists: 
mutation{createArtist(name:"Ana Gabriel"){
  artist{
    name
  }
}}

