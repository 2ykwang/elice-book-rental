ERROR_NOT_FOUND_RESOURCE = "err-001"
ERROR_BAD_REQUEST = "err-002"


errors = {
    ERROR_NOT_FOUND_RESOURCE: {"message": "요청한 리소스를 찾을 수 없습니다.", "status_code": 404},
    ERROR_BAD_REQUEST: {"message": "잘못된 요청 입니다.", "status_code": 400},
}
__all__ = [ERROR_NOT_FOUND_RESOURCE]
