from fastapi import FastAPI
from fastapi import Response

app = FastAPI()

@app.get("/")
def root():
    return {'message': "welcome!"}

@app.get("/csv")
def csv():
    csv_content = "name,age,city\nMarisa,30,nyc"
    return Response(content=csv_content, media_type="text/plain")
