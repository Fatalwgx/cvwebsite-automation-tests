from src.enums.global_enums import GlobalErrorMessages


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.parse_obj(item)
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self
        else:
            assert self.response_status == status_code, self
        return self
    
    def validate_user(self, test_user):
        assert self.response_json.get('username') == test_user.username
        assert self.response_json.get('email') == test_user.email
        assert self.response_json.get('id') == test_user.id

    def __str__(self):
        return (
            f"\n Status code: {self.response_status}"
            f"\n Requested URL: {self.response.url}"
            f"\n Response body: {self.response_json}"
        )
