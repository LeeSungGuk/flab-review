"""
다음 코드의 measuring_time은 전달받은 함수를 실행하는데 걸리는 소요시간을 출력하는 함수입니다. 내용을 채워주세요
cpu를 많이 요하는 연산이 포함된 함수 cpu_bound를 반복하여 수행하는 케이스에 대해
for loop, multiprocess, multithread, asyncio 를 이용하여 같은 결과를 내도록 함수의 로직을 짜보세요
각각의 수행시간을 비교해보고 왜 그런 결과가 나왔는지 설명을 해보세요
"""

import time
import asyncio

from inspect import iscoroutinefunction
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def measuring_time(func):
    if iscoroutinefunction(func):

        async def wrapps():
            s = time.time()
            name = func.__name__
            print(f"함수 {name} 시작")
            r = await func()
            e = time.time() - s
            print(f"함수 로직 수행 시간: {e}")
            print(f"함수 {name} 끝")
            return r

    else:

        def wrapps():
            s = time.time()
            name = func.__name__
            print(f"함수 {name} 시작")
            r = func()
            e = time.time() - s
            print(f"함수 로직 수행 시간: {e}")
            print(f"함수 {name} 끝")
            return r

    return wrapps


NUMBERS = [10**6 + i for i in range(20)]


def cpu_bound(n):
    return sum(i * i for i in range(n))


async def cpu_bound_aync(n):
    return sum(i * i for i in range(n))


@measuring_time
def cpu_bound_for_loop():
    result = 0
    for number in NUMBERS:
        result += cpu_bound(number)
    return result


@measuring_time
def cpu_bound_multi_thread():
    result = 0

    with ThreadPoolExecutor(max_workers=min(10, len(NUMBERS))) as executor:
        result = executor.map(cpu_bound, NUMBERS)

    return sum(list(result))


@measuring_time
def cpu_bound_multi_process():
    result = 0

    with ProcessPoolExecutor(max_workers=min(10, len(NUMBERS))) as executor:
        result = executor.map(cpu_bound, NUMBERS)

    return sum(list(result))


@measuring_time
async def cpu_bound_asyncio():
    futures = [asyncio.ensure_future(cpu_bound_aync(number)) for number in NUMBERS]
    result = await asyncio.gather(*futures)
    return sum(result)


if __name__ == "__main__":
    for_result = cpu_bound_for_loop()
    print(f"for_result: {for_result}\n")

    thread_result = cpu_bound_multi_thread()
    print(f"thread_result: {thread_result}\n")

    multiprocess_result = cpu_bound_multi_process()
    print(f"multiprocess_result: {multiprocess_result}\n")

    asyncio_result = asyncio.run(cpu_bound_asyncio())
    print(f"asyncio_result: {asyncio_result}\n")
    assert for_result == thread_result == multiprocess_result
