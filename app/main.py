from fastapi import FastAPI

app =  FastAPI()

@app.get("/")
def home():
    return {
        "message":"Alhamdullilah you are learning the Api in Python"
    }

@app.get("/about")
def about():
    return {
        "message":"This is About Page"
    }
@app.get("/users/{user_id}")
def get_user(user_id:int):
 return {"user_id":user_id}    

@app.get("/products")
def get_users(limit: int = 10):
   return {
      "limit":limit
   }

@app.get("/items")
def get_users(name: str = None, price : int =0):
   return {
      "Name":name, 
      "price":price
   }

@app.get("/users")
def get_users(name:str = None ):
    return{"Name":name}

