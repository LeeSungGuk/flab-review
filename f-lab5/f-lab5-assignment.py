import asyncio
import concurrent.futures as futures
import aiohttp

from requests import Session
from utils.decorator import measuring_time


URL = "https://httpbin.org/uuid"
NUM_ITERATION = 10
SAMPLE_UUID = "a25bbf18-29ac-4e7b-b3c7-df747d55fbf4"


# 비동기 함수에 사용
async def get_uuid_async(session):
    async with session.get(URL) as response:
        uuid = await response.json()
    return uuid


def get_uuid(session):
    with session.get(URL) as response:
        uuid = response.json()["uuid"]
    return uuid


@measuring_time
def io_bound_sync():
    uuids = []
    with Session() as session:
        for _ in range(NUM_ITERATION):
            with session.get(URL) as response:
                uuids.append(response.json()["uuid"])
    return uuids


@measuring_time
def io_bound_multi_thread():
    session = Session()
    with futures.ThreadPoolExecutor(max_workers=NUM_ITERATION) as executor:
        result = executor.map(
            get_uuid,
            [session] * NUM_ITERATION,
        )
    return list(result)


@measuring_time
def io_bound_multi_process():
    session = Session()
    with futures.ProcessPoolExecutor(max_workers=NUM_ITERATION) as executor:
        result = executor.map(
            get_uuid,
            [session] * NUM_ITERATION,
        )
    return list(result)


@measuring_time
async def io_bound_asyncio():
    uuids = []

    # sessing 안되서 비동기 aiohttp 모듈을 사용
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.ensure_future(get_uuid_async(session=session))
            for _ in range(0, NUM_ITERATION)
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    for result in results:
        uuids.append(result.get("uuid"))

    return uuids


if __name__ == "__main__":
    sync_result = io_bound_sync()
    print(f"io_bound_sync result: {sync_result}")
    multi_thread_result = io_bound_multi_thread()
    print(f"multi_thread_result result: {multi_thread_result}")
    multi_process_result = io_bound_multi_process()
    print(f"multi_process_result result: {multi_process_result}")
    asyncio_result = asyncio.run(io_bound_asyncio())
    print(f"asyncio_result result: {asyncio_result}")

    assert (
        len(sync_result)
        == len(multi_thread_result)
        == len(multi_process_result)
        == len(asyncio_result)
        == NUM_ITERATION
    )
    for uuid in iter(
        sync_result + multi_thread_result + multi_process_result + asyncio_result
    ):
        assert len(uuid) == len(SAMPLE_UUID)
