from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class IssueStatus(str, Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"

class IssuePriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

class IssueCreate(BaseModel):
    title: str = Field(min_length = 3, max_length = 100) # Think if this like Jakarta validation annotations in Spring Boot
    description: str = Field(min_length=5, max_length = 1000)
    priority: IssuePriority = IssuePriority.medium

class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, max_length = 100) # when updating ,we don't want to necessarily pass every field again
    description: Optional[str] = Field(default=None, max_length = 1000)
    priority: Optional[IssuePriority] = None
    status: Optional[IssueStatus] = None

# Schemas for response
class IssueOut(BaseModel):
    id: str
    title: str
    description: str
    priority: IssuePriority
    status: IssueStatus

