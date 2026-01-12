from requests import Session
from typing import Any


class HttpClient:
    def __init__(self, base_url: str, token: str | None = None) -> None:
        self.base_url = base_url
        self.session = Session()

        if token:
            self.session.headers.update({
                "Autorozation": f"Bearer {token}"
            })
    
    def get(self, path: str, params: dict | None = None) -> Any:
        response = self.session.get(
            url=self.base_url + path,
            params=params,
            timeout=10
        )
        if not response.ok:
            raise Exception(response.text)
        
        return response.json()
