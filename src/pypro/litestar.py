from litestar import Litestar, get


@get("/status")
async def hello_world() -> dict[str, str]:
    return {"message": "ok"}


app = Litestar([hello_world])
