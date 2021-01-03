from fastapi.exceptions import HTTPException


class NotFoundHTTP(HTTPException):
    def __init__(self, entity_name):
        self.message = f'{entity_name} not found.'
        super().__init__(status_code=404, detail=self.message)
        