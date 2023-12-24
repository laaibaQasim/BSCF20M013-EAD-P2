from typing import Dict, List, Union


def success(
    data: Union[list, dict, str] = [], total_rows: int = None, errors: List = []
) -> dict:
    """
    Create response format which contain objects

    Args:
        data: Defaults to [].
        total_rows: total number of rows. Defaults to None.
        errors: Defaults to [].

    Returns:
        response
    """
    response = {"status": "ok", "object": data}
    if total_rows is not None:
        response["total_rows"] = total_rows
    if len(errors) > 0:
        response["errors"] = errors
    return response


def failure(error_list: Union[str, List, None] = None, data: List = []) -> dict:
    """
    Create response format which contain errors

    Args:
        error_list: Defaults to None.
        data: Defaults to [].

    Returns:
        failure
    """
    if not error_list:
        error_list = ["Something went wrong."]
    if type(error_list) == str:
        error_list = [error_list]
    return {"status": "nok", "object": data, "errors": error_list}


def error(message: str = None, data: Dict = None) -> dict:
    """
    Set error message for response object

    Args:
        message: Error message. Defaults to None.
        data: Defaults to None.

    Returns:
        errors
    """
    message = message or "Something went wrong."
    return {
        "message": message,
        "object": data,
    }
