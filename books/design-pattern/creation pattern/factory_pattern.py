"""
    팩토리 패턴 - 팩토리를 사용해 객체 생성하기
    생성 패턴인 팩토리 패턴을 소개한다.

    팩토리 패턴 개요
    팩토리란 다른 클래스의 객체를 생성하는 클래스를 일컫는다.

    - 객체 생성과 클래스 구현을 나눠 상호 의존도를 줄인다.
    - 클라이언트는 생성하려는 객체 클래스 구현과 상관없이 사용할 수 있다.
      객체를 생성할 때 필요한 인터페이스와 메소드, 인자 등의 정보만 있으면 된다.
      따라서 클라이언트의 일이 줄어든다.
    - 코드를 수정하지 않고 간단하게 팩토리에 새로운 클래스를 추가 할 수 있다.
      인자 추가가 전부인 경우도 있다.
    - 재활용할 수 있따. 직접 객체를 생성하는 경우 매번 새로운 객체가 생성된다.

    팩토리 패턴은 다음과 같이 3가지 종류가 있다.
    1. 심플 팩토리 패턴: 인터페이스는 객체 생성 로직을 숨기고 객체를 생성한다.
    2. 팩토리 메소드 패턴: 인터페이스를 통해 객체를 생성하지만 서브 클래스가 객체 생성에 필요한 클래스를 선택한다.
    3. 추상 팩토리 패턴: 객체 생성에 필요한 클래스를 노출하지 않고 객체를 생성하는 인터페이스이다.

"""
from abc import ABC, abstractclassmethod


# 심플 팩토리 패턴
class Animal(ABC):
    @abstractclassmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow!!")


class Cat(Animal):
    def do_say(self):
        print("Meow Meow!!")


# forest factory 정의
class ForestFactory:
    def make_sound(self, object_type):
        return object_type().do_say()


# 팩토리 메소드 패턴
# (1). 인터페이스를 통해 객체를 생성하지만 팩토리가 아닌 서브 클래스가 해당 객체 생성을 위해 어던 클래스를
# 호출할지 결정한다.
# (2). 팩토리 메소드는 인스턴스화가 아닌 상속을 통해 객체를 생성한다.
# (3). 팩토리 메소드 디자인은 유동적이다. 심플 팩토리 메소드처럼 특정 객체가 아닌 같은 인스턴스나 서브 클래스
# 객체를 반환 할 수 있다.


# 추상 클래스 선언
class Section(ABC):
    @abstractclassmethod
    def describe(self):
        pass


if __name__ == "__main__":
    # 심플 팩토리 패턴
    ff = ForestFactory()
    # animal = input("Which animal should make sound Dog or Cat")
    ff.make_sound(Dog)
