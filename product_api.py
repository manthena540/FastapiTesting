from fastapi import FastAPI

app = FastAPI()

# Dummy data for products
products = {
    1: {"name": "Laptop", "price": 1000},
    2: {"name": "Phone", "price": 500},
}

@app.get("/products/{product_id}")
async def read_product(product_id: int):
    if product_id in products:
        return products[product_id]
    return {"message": "Product not found"}

@app.get("/products2/{product_id}")
async def read_product(product_id: int):
    if product_id in products:
        return products[product_id]
    return {"message": "Product not found"}

""" uvicorn product_api:app --reload """