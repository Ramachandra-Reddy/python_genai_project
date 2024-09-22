import uvicorn
from fastapi import FastAPI
from typing import Dict
from models.datamodels import Employee

# from resources import load_config

app = FastAPI()

# @app.on_event("startup")
# async def startup_event():
#     load_config()

employee_lists: Dict[int, Employee] = {}


@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI World"}


@app.post("/employees/")
def add_employee(new_employee: Employee) -> Dict:
    if new_employee.emp_id in employee_lists:
        return {"message": "Employee id is already present", "employees": employee_lists}
    employee_lists[new_employee.emp_id] = new_employee
    return {"message": "Employee added Successfully", "employees": employee_lists}


@app.get("/employees/{emp_id}/{emp_name}")
def get_employee(emp_id: int, emp_name: str) -> Dict:
    for emp in employee_lists.values():
        if (emp.emp_id == emp_id) and (emp.emp_name == emp_name):
            return {"My ID": {emp.emp_id}, "Name": {emp.emp_name}, "Age": {emp.emp_age}, "Salary": {emp.emp_salary}}
        return {"message": "You are not in the Employee list"}


@app.get("/employees/{emp_id}")
def get_employee_by_id(emp_id: int) -> Dict:
    for emp in employee_lists.values():
        if emp.emp_id == emp_id:
            return {"My ID": {emp.emp_id}, "Name": {emp.emp_name}, "Age": {emp.emp_age}, "Salary": {emp.emp_salary}}
        return {"message": "Your id is not in the Employee list"}


@app.get("/employees/{emp_name}")
def get_employee_by_name(emp_name: str) -> Dict:
    for emp in employee_lists.values():
        if emp.emp_name == emp_name:
            return {"My ID": {emp.emp_id}, "Name": {emp.emp_name}, "Age": {emp.emp_age}, "Salary": {emp.emp_salary}}
        return {"error": "Your name is not in the Employee list"}


@app.delete("/employees/delete/{id}")
def delete_employee(emp_id: int) -> Dict:
    if emp_id in employee_lists:
        del employee_lists[emp_id]
        return {"message": "Your record is successfully removed", "employees": employee_lists}
    return {"message": "Your record is not found in the Employee list", "employees": employee_lists}


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=9000, reload=True)
