from typing import Any, Dict, List
from abc import ABC


class AbstractStateMachine(ABC):
    INITIAL_STATE: Any = None
    MUTATION_SCHEMA: List[Dict[str, Any]] = None
