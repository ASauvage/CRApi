from urllib.parse import quote


def build_path(*parts: str) -> str:
    return "/" + "/".join(quote(part, safe="") for part in parts)
