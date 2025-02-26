from fastapi import FastAPI 
 

app = FastAPI()  


@app.get("/") 
 
def home(): 
 
    return {"message": "Fake Job Email Detection API is running!"}