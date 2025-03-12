# from fastapi import FastAPI, Path, Query
# from typing import Optional, List
# from pydantic import BaseModel, validator, Field
# from datetime import datetime

# app = FastAPI()

# # @app.get("/")
# # async def root():
# #     return {"message": "Hello World"}

# # To run this in a real environment:
# # uvicorn main:app --reload

# # This will start the FastAPI server and reload the app on code changes.
# # You can then access the API at http://127.0.0.1:8000.

# # Task model
# class Task(BaseModel):
#     title: str
#     description: Optional[str] = None
#     due_date: Optional[datetime] = None
#     priority: int = 1
#     tags: List[str] = []
#     completed: bool = False

# # In-memory database
# tasks = {}

# # GET all tasks
# @app.get("/tasks/")
# def get_tasks():
#     return tasks

# # GET single task
# @app.get("/tasks/{task_id}")
# def get_task(task_id: int = Path(..., title="The ID of the task to get")):
#     if task_id not in tasks:
#         return {"error": "Task not found"}
#     return tasks[task_id]

# # POST new task
# @app.post("/tasks/")
# def create_task(task: Task):
#     task_id = len(tasks) + 1
#     tasks[task_id] = task
#     return {"task_id": task_id, **task.dict()}

# # Example usage:
# # new_task = Task(title="Learn FastAPI", description="Complete the tutorial")
# # result = await create_task(new_task)

# # PUT update task
# @app.put("/tasks/{task_id}")
# def update_task(task_id: int, task: Task):
#     if task_id not in tasks:
#         return {"error": "Task not found"}
#     tasks[task_id] = task
#     return {"task_id": task_id, **task.dict()}

# # DELETE task
# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int):
#     if task_id not in tasks:
#         return {"error": "Task not found"}
#     del tasks[task_id]
#     return {"message": "Task deleted"}

# class TaskCreate(BaseModel):
#     title: str = Field(..., min_length=1, max_length=100)
#     description: Optional[str] = Field(None, max_length=1000)
#     due_date: Optional[datetime] = None
#     priority: int = Field(1, ge=1, le=5)
#     tags: List[str] = Field(default_factory=list)

#     @validator('title')
#     def title_must_be_meaningful(cls, v):
#         if len(v.strip()) < 3:
#             raise ValueError('Title must be meaningful (at least 3 characters)')
#         return v.strip()

#     @validator('due_date')
#     def due_date_must_be_future(cls, v):
#         if v and v < datetime.now():
#             raise ValueError('Due date must be in the future')
#         return v

#     @validator('tags')
#     def validate_tags(cls, v):
#         # Convert tags to lowercase
#         tags = [tag.lower() for tag in v]
#         # Remove duplicates while preserving order
#         unique_tags = list(dict.fromkeys(tags))
#         return unique_tags
    
#     # Example usage of TaskCreate model
# # try:
# #     # This should work
# #     valid_task = TaskCreate(
# #         title="Complete project",
# #         description="Finish the FastAPI project",
# #         due_date=datetime(2024, 12, 31),
# #         priority=2,
# #         tags=["work", "important"]
# #     )
# #     print("Valid task created:", valid_task)

# #     # This should fail
# #     invalid_task = TaskCreate(
# #         title="a",  # Too short
# #         priority=6,  # Out of range
# #         due_date=datetime(2020, 1, 1)  # Past date
# #     )
# # except ValueError as e:
# #     print("Validation error:", e)


# ### Running the Application
# # To run this in a real environment:
# # 1. Save your code in a file (e.g., main.py)
# # 2. Run: uvicorn main:app --reload
# # 3. Visit http://localhost:8000/docs or http://localhost:8000/redoc
