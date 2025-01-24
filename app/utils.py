import httpx

WILDBERRIES_API_URL = "https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={artikul}"

async def fetch_product_data(artikul: int):
    url = WILDBERRIES_API_URL.format(artikul=artikul)
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise ValueError("Product not found")
        data = response.json()["data"]["products"][0]
        return {
            "artikul": artikul,
            "name": data["name"],
            "price": data["priceU"] / 100,
            "rating": data.get("rating", 0),
            "total_quantity": data["quantity"]
        }