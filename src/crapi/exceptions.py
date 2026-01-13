

class ClientError(Exception):
    def __init__(self, status_code: int, reason: str, message: str | None = None, detail: dict | None = None) -> None:
        self.status_code = status_code
        self.reason = reason
        self.message = message
        self.detail = detail

        super().__init__(f"{status_code}: {reason}")
