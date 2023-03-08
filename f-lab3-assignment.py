# python range()  함수를 iterator 클래스와 generator 함수로 각각 구현해보세요


""" 다음 list comprehension과 generator의 생성 시간을 비교하고 각 object의 size를 구하시오
    list_comp = [i for i in range(1000000)]
    gen = (i for i in range(1000000))
"""


# python range()  함수를 iterator 클래스와 generator 함수로 각각 구현해보세요


class irange:
    def __init__(self, n: int):
        self.stop = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current < self.stop:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration


def grange(n: int) -> int:
    start = 0

    while start < n:
        yield start
        start += 1


def get_obejct_size():
    # 다음 list comprehension과 generator의 생성 시간을 비교하고 각 object의 size를 구하시오
    import time

    s = time.time()
    list_comp = [i for i in range(1000000)]
    end_list_compe = time.time() - s

    s = time.time()
    gen = (i for i in range(1000000))
    end_gen = time.time() - s

    print(f"list comprehension 생성 시간: {end_list_compe}")
    print(f"generator의 생성 시간: {end_gen}")

    import sys

    print(sys.getsizeof(int(1)))
    print(f"list comprehension size: {len(list_comp)}")
    print(f"list comprehension size: {sys.getsizeof(list_comp)}")
    print(f"generator의 size: {sys.getsizeof(gen)}")


if __name__ == "__main__":
    for i, j in enumerate(range(5)):
        assert i == j

    for i, j in enumerate(irange(5)):
        assert i == j

    for i, j in enumerate(grange(5)):
        assert i == j

    get_obejct_size()
