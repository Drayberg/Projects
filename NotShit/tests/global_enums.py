from enum import Enum


class GlobalErrors(Enum):
    WRONG_STATUS_CODE = 'Got wrong status code'
    NO_SUCH_ELEMENT = 'There is no such element on the page'
