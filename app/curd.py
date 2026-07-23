from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


todos = []

class Todo(BaseModel):
    id:int
    title:str
    completed:bool

@app.post("/todos")
def create_toto(todo:Todo):
    todos .append(todo)
    return{"message":"Todo Added","data":todo}

@app.get("/todos")
def get_todo():
    return todos
#parth params 
@app.get("/todos/{todo_id}")
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
          return todo
    return{"error":"Todo not found "}  

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id == todo_id:
           todos[index]= update_todo
           return {
               "mesage":"Data Updated",
               "data":update_todo
           }

@app.delete("/todos/{todo_id}")        
def delete_todo(todo_id:int):
    for index, todo in enumerate(todo):
        if todo.id == todo_id:
            todo.pop(index)
            return {"message:"Data Deleted"}
        return {"erorr":"Todo not found "}            