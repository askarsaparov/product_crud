from drf_yasg import openapi

from accounts.serializers import RegisterSerializer

verify_phone_number_schema = {
    "200": openapi.Response(
        description="Successfully",
        examples={
            "application/json": {'detail': 'Verification code sent successfully'}
        }
    ),
    "400": openapi.Response(
        description="Failed",
        examples={
            "application/json": {'detail': 'Failed to send verification code'}
        }
    ),
}

verify_phone_forgot_pass_number_schema = {
    "200": openapi.Response(
        description="Successfully",
        examples={
            "application/json": {'detail': 'Verification code sent successfully'}
        }
    ),
    "400": openapi.Response(
        description="Failed",
        examples={
            "application/json": {'detail': 'Failed to send verification code'}
        }
    ),
}

verify_code_schema = {
    "200": openapi.Response(
        description="Successfully",
        examples={
            "application/json": {'detail': 'Verification successful'}
        }
    ),
    "400": openapi.Response(
        description="Failed",
        examples={
            "application/json": {'detail': 'Verification failed'}
        }
    ),
}

register_schema = {
    "200": openapi.Response(
        description="Successfully",
        examples={
            "application/json": {
                "access_token": "access_token",
                "refresh_token": "refresh_token",
                "token_type": "Bearer",
                "user": RegisterSerializer().data
            }
        }
    )
}

update_password_schema = {
    "200": openapi.Response(
        description="Successfully",
        examples={
            "application/json": {'detail': 'Password updated successfully'}
        }
    ),
    "404": openapi.Response(
        description="User not found",
        examples={
            "application/json": {'detail': "Not found."}
        }
    ),
    "400": openapi.Response(
        description="Bad request",
        examples={
            "application/json": {
                "non_field_errors": [
                    "Password fields didn't match.."
                ],
                "password": [
                    "This field is required."
                ],
                "phone": [
                    "Enter a valid phone number."
                ]
            }
        }
    )
}
