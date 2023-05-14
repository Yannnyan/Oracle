from readexcel import Data

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    print("hello")
    return {"messsdas": " World"}

@app.get("/data")
def hello_world():
    dataobj = Data('./exampledata.xlsx')
    dataobj.readAndStoreExcel()
    return {"message": dataobj.table.to_json()}



