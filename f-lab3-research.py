# bytes 자료형 조사


def get_bytes_data(value: bytes):
    import sys

    # 영어, 숫자, 한글에 대한 한 글자 데이터 사이즈 얻기
    print(sys.getsizeof(value))
    print(len(value))


e = b"a"
get_bytes_data(e)
