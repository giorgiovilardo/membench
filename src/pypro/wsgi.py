import json


class Application:
    def __call__(self, environ, start_response):
        if environ["REQUEST_METHOD"] == "GET":
            status, response = self.do_get(environ)
        else:
            status, response = "404 Not Found", b""

        start_response(status, [("Content-Type", "application/json")])
        return [response]

    def do_get(self, environ):
        """Handle GET http request."""
        match environ["PATH_INFO"]:
            case "/status":
                response_body = json.dumps({"message": "ok"})
                status = "200 OK"
                return status, response_body.encode("utf-8")
        return "404 Not Found", b""


app = Application()
