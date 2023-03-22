import time
from inspect import iscoroutinefunction


def measuring_time(func):
    # 코루틴 체크 하는 함수
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
