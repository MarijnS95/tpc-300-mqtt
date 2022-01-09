from fastapi import FastAPI, Request, Body
import tpc


app = FastAPI()


@app.get("/switch/{index}/{state}")
def set_switch(index: int, state: bool):
    print(f"Setting {index} to {'on' if state else 'off'}")
    tpc.control_channel(index, state)


@app.post("/switch/{index}")
async def post_switch(
    index: int, request: Request = Body(..., media_type="text/plain")
):
    data = await request.body()
    print(data)
    state = data == b"ON"
    print(f"Setting {index} to {'on' if state else 'off'}")
    tpc.control_channel(index, state)
