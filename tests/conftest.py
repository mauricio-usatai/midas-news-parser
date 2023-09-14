import pytest


@pytest.fixture
def raw_news_feed():
    return {
        "status": "ok",
        "totalResults": 2,
        "articles": [
            {
                "source": {"id": None, "name": "Abril.com.br"},
                "author": "Gustavo Maia",
                "title": "Some title",
                "description": "Some description",
                "url": "https://veja.abril.com.br/some-title",
                "urlToImage": "https://veja.abril.com.br/",
                "publishedAt": "2023-09-13T15:42:02Z",
                "content": "Some content… [+301 chars]",
            },
            {
                "source": {"id": "globo", "name": "Globo"},
                "author": None,
                "title": "WEG e Petrobras assinam...",
                "description": "Aerogerador em terra...",
                "url": "https://valor.globo.com/empresas/noticia/2023/09/13/weg.ghtml",
                "urlToImage": "https://s2-valor.glbimg.com/",
                "publishedAt": "2023-09-13T11:55:18Z",
                "content": "A WEG e a Petrobras … [+419 chars]",
            },
        ],
    }
