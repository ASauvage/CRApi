from requests import JSONDecodeError, Session
from typing import Any

from .exception import ClientError


class HttpClient:
    def __init__(self, hostname: str, version: str = "v1", token: str | None = None) -> None:
        self.base_url = hostname + version
        self.session = Session()

        if token:
            self.session.headers.update({
                "Autorozation": f"Bearer {token}"
            })
    
    def get(self, path: str, **kwargs) -> Any:
        response = self.session.get(
            url=self.base_url + path,
            **kwargs,
            timeout=10
        )

        try:
            data = response.json()
            if not response.ok:
                raise ClientError(
                    response.status_code,
                    reason=data["reason"],
                    message=data["message"] if "message" in data.keys() else None,
                    detail=data["detail"] if "message" in data.keys() else None
                )

            return data
        except JSONDecodeError:
            raise Exception(response.text)
