def assert_status_code(response, expected_status):
    assert response.status_code == expected_status, (
        f"Expected status {expected_status}, "
        f"but got {response.status_code}"
    )


def assert_json_field(data, field, expected_value):
    assert field in data, f"Field '{field}' not found in response"

    assert data[field] == expected_value, (
        f"Expected '{field}' to be '{expected_value}', "
        f"but got '{data[field]}'"
    )