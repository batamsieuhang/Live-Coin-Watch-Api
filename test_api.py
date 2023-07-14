import requests,json
url = "https://graphql.coincap.io/"

payload = {
    "query": """
        query ($id: ID!, $direction: SortDirection, $first: Int!, $sort: ExchangeMarketSortInput) {
            exchange(id: $id) {
                id
                subscription
                __typename
            }
            exchangeMarkets(
                exchangeId: $id
                direction: $direction
                first: $first
                sort: $sort
            ) {
                pageInfo {
                    hasNextPage
                    __typename
                }
                edges {
                    node {
                        id
                        baseSymbol
                        exchangeId
                        baseId
                        quoteSymbol
                        quoteId
                        rate
                        priceUsd
                        tradesCount24Hr
                        volumeUsd24Hr
                        percentExchangeVolume
                        updatedAt
                        __typename
                    }
                    __typename
                }
                __typename
            }
        }
    """,
    "variables": {
        "id": "binance",
        "direction": "DESC",
        "first": 10,
        "sort": "volumeUsd24Hr"
    }
}

headers = {
        'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

response = requests.post(url, json=payload,headers=headers)
print(json.loads(response.text)['data']['exchangeMarkets']['edges'][0]['node']['quoteSymbol'])