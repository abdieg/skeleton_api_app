from typing import Optional

from fastapi import FastAPI
from faker import Faker
import random
import uvicorn

app = FastAPI()
fake = Faker()


@app.get("/person")
def get_person(
    is_employee: Optional[bool] = None,
):
    """Return fake person data"""
    return {
        "name": fake.name(),
        "dob": fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%Y-%m-%d"),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.address(),
        "zip_code": fake.zipcode(),
        "is_employee": is_employee if is_employee is not None else random.choice([True, False]),
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
    uvicorn.run(app, host="127.0.0.1", port=11000)
