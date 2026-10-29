from fastapi import APIRouter, Response
from models.employeeModel import Employee

from controllers.employeeController import (
    create_employee_controller,
    get_employees_controller,
    get_employee_by_id,
    update_employee_controller,
    delete_employee_controller
)

employeeRouter = APIRouter(prefix="/employees")


# Create employee
@employeeRouter.post("/")
async def create_employee(
    employee: Employee,
    response: Response
):
    return await create_employee_controller(employee, response)


# Get all employees
@employeeRouter.get("/")
async def get_employees(response: Response):
    return await get_employees_controller(response)


# Get employee by ID
@employeeRouter.get("/{id}")
async def get_employee(id: str, response: Response):
    return await get_employee_by_id(id, response)


# Update employee
@employeeRouter.put("/{id}")
async def update_employee(
    id: str,
    employee: Employee,
    response: Response
):
    return await update_employee_controller(id, employee, response)


# Delete employee
@employeeRouter.delete("/{id}")
async def delete_employee(id: str, response: Response):
    return await delete_employee_controller(id, response)