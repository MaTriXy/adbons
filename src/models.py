from dataclasses import dataclass
from typing import Optional


@dataclass
class Device:
    id: str
    description: Optional[str] = None
