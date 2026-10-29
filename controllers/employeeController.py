from fastapi import Response
from bson import ObjectId
from models.employeeModel import Employee
from dbConnect import employeeCollection


# Create employee
async def create_employee_controller(
    employee: Employee,
    response: Response
):
    try:
        employee_data = employee.model_dump(exclude={"id"})

        result = await employeeCollection.insert_one(employee_data)

        employee_data["id"] = str(result.inserted_id)

        response.status_code = 201

        return {
            "isSuccess": True,
            "message": "Employee created successfully",
            "data": employee_data
        }

    except Exception as e:
        print(e)
        response.status_code = 500

        return {
            "isSuccess": False,
            "message": str(e)
        }


# Get all employees
async def get_employees_controller(response: Response):
    try:
        employees = []

        async for employee in employeeCollection.find():
            employee["id"] = str(employee["_id"])
            employee.pop("_id", None)

            employees.append(employee)

        return {
            "isSuccess": True,
            "employees": employees
        }

    except Exception as e:
        print(e)
        response.status_code = 500

        return {
            "isSuccess": False,
            "message": "Error fetching employees"
        }


# Get employee by ID
async def get_employee_by_id(id: str, response: Response):
    try:
        if not ObjectId.is_valid(id):
            response.status_code = 400

            return {
                "isSuccess": False,
                "message": "Invalid employee ID"
            }

        employee = await employeeCollection.find_one(
            {"_id": ObjectId(id)}
        )

        if employee:
            employee["id"] = str(employee["_id"])
            employee.pop("_id", None)

            return {
                "isSuccess": True,
                "data": employee
            }

        response.status_code = 404

        return {
            "isSuccess": False,
            "message": "Employee not found"
        }

    except Exception as e:
        print(e)
        response.status_code = 500

        return {
            "isSuccess": False,
            "message": str(e)
        }


# Update employee
async def update_employee_controller(
    id: str,
    employee: Employee,
    response: Response
):
    try:
        if not ObjectId.is_valid(id):
            response.status_code = 400

            return {
                "isSuccess": False,
                "message": "Invalid employee ID"
            }

        employee_data = employee.model_dump(exclude={"id"})

        result = await employeeCollection.update_one(
            {"_id": ObjectId(id)},
            {"$set": employee_data}
        )

        if result.matched_count > 0:
            employee_data["id"] = id

            return {
                "isSuccess": True,
                "message": "Employee updated successfully",
                "data": employee_data
            }

        response.status_code = 404

        return {
            "isSuccess": False,
            "message": "Employee not found"
        }

    except Exception as e:
        print(e)
        response.status_code = 500

        return {
            "isSuccess": False,
            "message": str(e)
        }


# Delete employee
async def delete_employee_controller(id: str, response: Response):
    try:
        if not ObjectId.is_valid(id):
            response.status_code = 400

            return {
                "isSuccess": False,
                "message": "Invalid employee ID"
            }

        result = await employeeCollection.delete_one(
            {"_id": ObjectId(id)}
        )

        if result.deleted_count > 0:
            return {
                "isSuccess": True,
                "message": "Employee deleted successfully"
            }

        response.status_code = 404

        return {
            "isSuccess": False,
            "message": "Employee not found"
        }

    except Exception as e:
        print(e)
        response.status_code = 500

        return {
            "isSuccess": False,
            "message": str(e)
        }