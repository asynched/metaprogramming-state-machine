from typing import Any, Dict, List


class AbstractStateMachine:
    INITIAL_STATE: Any = None
    MUTATION_SCHEMA: List[Dict[str, Any]] = None
