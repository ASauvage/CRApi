

class CRError(Exception):
    pass

class RateLimitError(CRError):
    pass

class NotFoundError(CRError):
    pass
