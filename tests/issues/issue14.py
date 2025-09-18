from pydantic import BaseModel
from requests import HTTPError


class Foo(BaseModel, arbitrary_types_allowed=True):

    type_is_out_of_module: HTTPError
    """the type of this field is outside of this module"""
