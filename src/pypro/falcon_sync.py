import falcon


class StatusController:
    def on_get(self, _req, resp) -> None:
        resp.media = {"message": "ok"}


app = falcon.App()
app.add_route("/status", StatusController())
