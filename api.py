from typing import Optional, Literal
from fastapi import FastAPI, Query, HTTPException, Request
from faker import Faker
import random
import uvicorn

app = FastAPI()
fake = Faker()

# Explicitly allowed query params
ALLOWED_QUERY_PARAMS = {"is_employee"}


@app.get("/person")
async def get_person(
        request: Request,
        is_employee: Optional[Literal["true", "false"]] = Query(
            default=None,
            description="Indicates if person is an employee. Accepts only 'true' or 'false'.",
        )
):
    """Return fake person data"""

    # Check for unexpected query parameters
    unexpected_params = set(request.query_params.keys()) - ALLOWED_QUERY_PARAMS
    if unexpected_params:
        raise HTTPException(
            status_code=400,
            detail=f"Unexpected query parameter(s): {', '.join(unexpected_params)}"
        )

    # Convert string to boolean
    is_employee = is_employee == "true" if is_employee is not None else random.choice([True, False])

    return {
        "name": fake.name(),
        "dob": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d"),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.address(),
        "zip_code": fake.zipcode(),
        "is_employee": is_employee,
        "salary": round(random.uniform(15000, 120000), 2),
        "company": fake.company(),
        "equipment": [
            {
                "product": fake.word(),
                "price": round(random.uniform(10, 500), 2),
                "date_given": fake.date_this_decade().strftime("%Y-%m-%d")
            }
            for _ in range(random.randint(1, 5))  # Add between 1 and 5 additional items
        ]
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=10200)
