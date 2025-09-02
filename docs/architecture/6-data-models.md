## 6. Data Models

The core data model for the application is the `Pokemon` model. It will be defined as a Pydantic model to ensure data validation at the API boundary and as a SQLAlchemy model for database persistence.

#### 6.1. Pydantic Model (`backend/app/models.py`)

This model is used for API request/response validation.

```python
from pydantic import BaseModel, HttpUrl

class Pokemon(BaseModel):
    id: int
    name: str
    sprite_url: HttpUrl

    class Config:
        from_attributes = True
```
