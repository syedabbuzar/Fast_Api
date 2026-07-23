from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
#nasted Data 
#create Schemas 
#data validation
class Address(BaseModel):
     city:str
     pincode:int
     
class User(BaseModel):
     name:str
     age:int
     email:str 
     address:Address
    
@app.post("/create-user")
def create_user(user:User):
    return {
        "message":"User Created",
        "date":user    
        } 
 

