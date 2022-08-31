# coding: utf-8
"""
Sample API 
__author__ = 'naubull2 (naubull2@gmail.com)'
"""
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError

from .application import FastJsonAPI
from .model import SortMachine
from .schema import SortPayload

app = FastJsonAPI(
    title="Sort-machine",
    description="Sample sorting model as a placeholder",
    version="1.2.3",
)

res = dict()


@app.on_event("startup")
def init_model():
    # NOTE: Initialize model on start up
    res["model"] = SortMachine()
    return res


@app.post("/v1/post/sort")
async def v1_post_sort(request: Request, payload: SortPayload = None):
    output_obj = {"result": payload.intArr}
    try:
        output_obj.update(
            {
                "result": res["model"].sort(
                    payload.intArr, reverse=payload.reverse, method=payload.method
                )
            }
        )
    except ValidationError as e:
        raise e
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"INTERNAL_SERVER_ERROR:Internal server error: {str(e)}",
        )

    headers = {"x-call-count": "1"}
    return JSONResponse(status_code=200, content=output_obj, headers=headers)
