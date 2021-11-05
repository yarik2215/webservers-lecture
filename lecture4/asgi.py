from random import randint

async def application(scope, receive, send):
    event = await receive()
    print(event)
    assert scope["type"] == "http"
    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text/plain"],
                [b"x-custom-header", b"python"],
            ]
        }
    )
    await send(
        {
            "type": "http.response.body",
            "body": bytes(f"Hello ASGI {randint(0, 100)}!", "utf-8")
        }
    )