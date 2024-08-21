import falcon.asgi


class AsyncStatusController:
    async def on_get(self, _req, resp):
        resp.media = {"message": "ok"}


app = falcon.asgi.App()
app.add_route("/status", AsyncStatusController())
