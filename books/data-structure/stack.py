from typing import TypeVar, Generic

T = TypeVar("T")


# list 구현된
class Stack(Generic[T]):
    """
    list로 구현 Stack
    """

    def __init__(self):
        self._stack = list()

    def push(self, v: T) -> None:
        self._stack.append(v)

    def pop(self) -> T:
        return self._stack.pop()

    def __len__(self) -> int:
        count: int = 0
        for _ in self._stack:
            count += 1
        return count


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert len(stack) == 2
    value = stack.pop()
    assert value == 2
    assert len(stack) == 1
