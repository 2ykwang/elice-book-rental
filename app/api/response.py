from http import HTTPStatus
from typing import Any, Dict, Tuple

from .errors import errors


class Response:
    def _make_response(
        status_code: HTTPStatus = HTTPStatus.OK,
        error: Dict[str, Any] = None,
        result: Dict[str, Any] = None,
    ):
        response = {
            "status": status_code,
            "error": error,
            "result": result,
        }, status_code
        print(response)
        return response

    @staticmethod
    def make_response(result: Dict[str, Any]):
        return Response._make_response(
            200, error={"error": "", "message": ""}, result=result
        )

    @staticmethod
    def make_error(
        error: str, message: str = None, status_code: int = None
    ) -> Tuple[Dict[str, Any], int]:

        # 정의된 에러가 아닐 경우
        if error not in errors:
            # raise ValueError(f"Unknown Error {error}")

            return Response._make_response(
                status_code=400 if status_code is None else status_code,
                error={
                    "error": error,
                    "message": "" if message is None else message,
                },
            )

        return Response._make_response(
            status_code=errors[error]["status_code"]
            if status_code is None
            else status_code,
            error={
                "error": error,
                "message": errors[error]["message"] if message is None else message,
            },
        )
