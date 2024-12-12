
from rest_framework.response import Response
from enum import StrEnum
from rest_framework import status

class ResponseStatus(StrEnum):
    SUCCESS = "success"
    FAILURE = "failure"
    MDNF = "Matching Data Not Found"
    RDS = "Record Deleted Successfully"

def SuccessResponse(data):
    return Response(
        {"status": ResponseStatus.SUCCESS, "data": data},
        status=status.HTTP_200_OK,
    )

def CreatedResponse(data):
    return Response(
        {"status": ResponseStatus.SUCCESS, "data": data}, status=status.HTTP_201_CREATED
    )

def FailureResponse(data):
    return Response(
        {"status": ResponseStatus.FAILURE, "data": data},
        status=status.HTTP_400_BAD_REQUEST,
    )
