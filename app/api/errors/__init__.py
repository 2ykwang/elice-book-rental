from http import HTTPStatus

ERROR_NOT_FOUND_RESOURCE = "err-001"
ERROR_BAD_REQUEST = "err-002"
ERROR_VALUE_ALREADY_EXISTS = "err-003"


errors = {
    ERROR_NOT_FOUND_RESOURCE: {
        "message": "요청한 리소스를 찾을 수 없습니다.",
        "status_code": HTTPStatus.NO_CONTENT[0],
    },
    ERROR_BAD_REQUEST: {
        "message": "잘못된 요청 입니다.",
        "status_code": HTTPStatus.BAD_REQUEST[0],
    },
    ERROR_VALUE_ALREADY_EXISTS: {
        "message": "이미 존재하는 리소스/값 입니다.",
        "status_code": HTTPStatus.CONFLICT[0],
    },
}

"""
200: OK (정상, 데이터 있음)
204: No Contents (정상, 데이터 없음)
301: Moved Permanently (리다이렉션)
400: Bad Request (실패, 클라이언트에서 넘어온 파라미터가 이상함)
401: Unauthorized (실패, 클라이언트에서 넘어온 보안 토큰이 이상함)
403: Forbidden (실패, 사용자의 권한으로 리소스를 사용할 수 없음)
404: Not Found (실패, 데이터가 있어야 하나 없음)
410: Gone (실패, 데이터가 있었으나 삭제됨. 이건 굳이...?)
500: Internal Server Error (실패, 서버 로직 문제)
501: Not Implemented (실패, 없는 리소스 요청)
"""
