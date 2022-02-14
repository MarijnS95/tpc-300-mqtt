from fastapi import FastAPI, Request, Body
import tpc
import logging

logging.basicConfig(format="%(asctime)s:" + logging.BASIC_FORMAT)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

app = FastAPI()


@app.get("/switch/{index}/{state}")
def set_switch(index: int, state: bool):
    logger.debug(f"Setting {index} to {'on' if state else 'off'}")
    tpc.control_channel(index, state)


@app.post("/switch/{index}")
async def post_switch(
    index: int, request: Request = Body(..., media_type="text/plain")
):
    data = await request.body()
    logger.debug(data)
    state = data == b"ON"
    logger.debug(f"Setting {index} to {'on' if state else 'off'}")
    tpc.control_channel(index, state)
