from urllib.parse import quote


def build_path(*parts: str) -> str:
    return "/" + "/".join(quote(part, safe="") for part in parts)


def params_format(**kwargs) -> dict:
    return {key: value for key, value in kwargs.items() if value}
