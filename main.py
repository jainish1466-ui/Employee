from fastapi import FastAPI
from routers.employeeRouter import employeeRouter

app = FastAPI()

app.include_router(employeeRouter)


@app.get("/")
async def root():
    return {"message": "Employee CRUD Application"}