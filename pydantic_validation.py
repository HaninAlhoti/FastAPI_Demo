from datetime import datetime
from main import TaskCreate
import main

# Example usage of TaskCreate model
try:
    # This should work
    valid_task = TaskCreate(
        title="Complete project 1",
        description="Finish the FastAPI project",
        due_date=datetime(2025, 12, 31),
        priority=2,
        tags=["work", "important"]
    )
    main.tasks = valid_task
    print("Valid task created:", valid_task)

    # # This should fail
    # invalid_task = TaskCreate(
    #     title="a",  # Too short
    #     priority=6,  # Out of range
    #     due_date=datetime(2020, 1, 1)  # Past date
    # )
except ValueError as e:
    print("Validation error:", e)


### Running the Application
# To run this in a real environment:
# 1. Save your code in a file (e.g., pydantic_validation.py)
# 2. Run: python pydantic_validation.py