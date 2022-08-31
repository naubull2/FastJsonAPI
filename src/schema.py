# coding: utf-8
"""
Sample Schema
__author__ = 'naubull2 (naubull2@gmail.com)'
"""
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel  # , validator
from pydantic import StrictInt  # , constr


class SortMethod(str, Enum):
    merge = "merge"
    stalin = "stalin"


class SortPayload(BaseModel):
    class Config:
        extra = "forbid"  # {allow, ignore, forbid}

    """Define input payload"""
    intArr: List[StrictInt]
    # method : Optional[constr(regex=r"^(merge|stalin)$")]
    method: Optional[SortMethod]  # The same as Union[SortMethod, None]
    reverse: Optional[bool] = False

    # @validator("intArr")
    # def valid_array(cls, v):
    #    # NOTE: Make any specific validations you want to incorporate
    #    if not v or len(v) < 1 or len(v) > 1000:
    #        raise HTTPException(
    #            status_code=422,
    #            detail="INVALID_PARAMETER_VALUE: Size of a valid input array must be within the range 1-1000",
    #        )
    #    return v


# class SortResponse(BaseModel):
#    """Define output payload if needed"""
#    result: List[int]
#    version: str = app.version
