# This File is Take From https://github.com/pokurt/Nana-Remix/blob/master/nana/utils/sauce.py
import requests

airing_query = """
query ($id: Int,$search: String) {
    Media (id: $id, type: ANIME,search: $search) {
        id
        episodes
        title {
            romaji
            english
            native
        }
        nextAiringEpisode {
            airingAt
            timeUntilAiring
            episode
        }
    }
}
"""

fav_query = """
query ($id: Int) {
    Media (id: $id, type: ANIME) {
        id
        title {
            romaji
            english
            native
        }
    }
}
"""

anime_query = """
query ($id: Int,$search: String) {
    Media (id: $id, type: ANIME,search: $search) {
        id
        title {
            romaji
            english
            native
        }
        description (asHtml: false)
        startDate{
            year
        }
        episodes
        season
        type
        format
        status
        duration
        siteUrl
        studios{
            nodes{
                name
            }
        }
        trailer{
            id
            site
            thumbnail
        }
        averageScore
        genres
        bannerImage
    }
}
"""

character_query = """
query ($query: String) {
    Character (search: $query) {
        id
        name {
            first
            last
            full
        }
        siteUrl
        image {
            large
        }
        description
    }
}
"""

manga_query = """
query ($id: Int,$search: String) {
    Media (id: $id, type: MANGA,search: $search) {
        id
        title {
            romaji
            english
            native
        }
        description (asHtml: false)
        startDate{
            year
        }
        type
        format
        status
        siteUrl
        averageScore
        genres
        bannerImage
    }
}
"""


url = 'https://graphql.anilist.co'


def airing_sauce(query):
    variables = {'search': query}
    resp = requests.post(url, json={'query': airing_query, 'variables': variables})
    return resp.json()


def fav_sauce(query):
    variables = {'search': query}
    resp = requests.post(url, json={'query': fav_query, 'variables': variables})
    return resp.json()


def anime_sauce(query):
    variables = {'search': query}
    resp = requests.post(url, json={'query': anime_query, 'variables': variables})
    return resp.json()


def character_sauce(query):
    variables = {'search': query}
    resp = requests.post(url, json={'query': character_query, 'variables': variables})
    return resp.json()


def manga_sauce(query):
    variables = {'search': query}
    resp = requests.post(url, json={'query': manga_query, 'variables': variables})
    return resp.json()

def shorten(description, info='anilist.co'):
    ms_g = ''
    if len(description) > 700:
        description = description[0:500] + '....'
        ms_g += f'\n**Description**: __{description}__[Read More]({info})'
    else:
        ms_g += f'\n**Description**: __{description}__'
    return (
        ms_g.replace('<br>', '')
        .replace('</br>', '')
        .replace('<i>', '')
        .replace('</i>', '')
    )

