# -*- coding: utf-8 -*-
# @Author : jjxu
# @time: 2019/1/14 14:35

from werkzeug.exceptions import HTTPException

from app.libs.error import ApiException
from app.libs.error_code import ServerError

from app import create_app

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, ApiException):
        return e
    elif isinstance(e, HTTPException):
        return ApiException(msg=e.description, code=e.code, error_code=1007)
    else:
        if not app.config["DEBUG"]:
            return ServerError()
        else:
            return e


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host=app.config["HOST"])
