from typing import Any, Dict, Tuple

from .errors import error_messages


class Response:
    @staticmethod
    def make_error(
        error: str, message: str = None, status: int = 400
    ) -> Tuple[Dict[str, Any], int]:

        return {
            "status": status,
            "error": error,
            "message": error_messages[error] if message is None else message,
        }, status
