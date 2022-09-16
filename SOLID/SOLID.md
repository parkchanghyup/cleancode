# SOLID

객체지향 설계 5대 원칙이라 부르는 `SOLID 원칙`은 `SRP(단일 책임 원칙)`, `OCP(개방-폐쇄 원칙)`, `LSP(리스코프 치환 원칙)`, `ISP(인터페이스 분리 원칙)`, `DIP(의존 역전 원칙)`을 말하고 각 원칙의 앞자를 따서 SOILD 원칙이라고 부른다.

## Single Responsiblity

Single Responsiblity은 객체는 하나의 책임만을 지녀야 한다는 법칙이다. 

여러 책임을 동시에 가지는 객체는 처음에 코드를 짤 때는 편하지만 **코드가 복잡해질수록 에러가 날 확률도 높아지며 직관적으로 코드를 이해하기 어려워진다.**  
따라서 객체를 설계하기 전 책임을 확실하게 부여하는 것이 중요하다.  

### AS-IS 

```python
# 하나의 클래스(객체)가 여러 책임을 가지고  있을때
class Employee:
    def coding(self):
        print("코딩을 합니다")

    def design(self):
        print("디자인을 합니다")
    
    def analyze(self):
        print("분석을 합니다")
```
### TO-BE

```python
#각 객체가 역할을 나눠서 가지고 있을때
class Developer:
    def coding(self):
        print("코딩을 합니다")

class Designer:
    def design(self):
        print("디자인을 합니다")

class Analyst:
    def analyze(self):
        print("분석을 합니다")
```

## Open Closed
---
Open Closed Principle는 객체는 **확장에는 열려있고, 수정에는 닫혀있게 해야 한다는 법칙**이다.  

객체는 기존의 코드를 변경하지 않으면서 추가할 수 있도록 설계되어야 한다.   
OCP에서 중요한 부분은 요구사항이 변경되었을 때 코드의 변경되어야 할 부분과 그렇지 않아야 할 부분이 명확하게 구분되어 있어야 한다.  
보통 이를 지키기 위해선 인터페이스나 추상 클래스를 통해 추상화시키고 이를 상속,구현하게 된다.  
새로운 기능을 추가한다고 할 때, 다형성을 사용해 기존 코드를 변경하지 않으면서(변경에 닫혀있음), 추상 클래스를 상속받아 쉽게 코드를 추가할 수 있다.(확장에 열려 있음)  

### AS-IS 

```python
class Developer:
    def coding(self):
        print("코딩을 합니다")

class Designer:
    def design(self):
        print("디자인을 합니다")

class Analyst:
    def analyze(self):
        print("분석을 합니다")

class Company:
    def __init__(self, employees):
        self.employees = employees

    # employee가 다양해질수록 코드를 계속 변경해야 한다.
    def make_work(self):
        for employee in self.employees:
            if isinstance(employee, Developer):
                employee.coding()
            elif isinstance(employee, Designer):
                employee.design()
            elif isinstance(employee, Analyst):
                employee.analyze()
```
### TO-BE

```python

# 각 객체들의 역할을 아우르는 추상 클래스(고수준)을 생성합니다.
class Employee(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def work(self):
        ...

class Developer(Employee):
    def work(self):
        print("코딩을 합니다")

class Designer(Employee):
    def work(self):
        print("디자인을 합니다")

class Analyst(Employee):
    def work(self):
        print("분석을 합니다")

#상속을 통해 쉽게 구현이 가능함 -> 확장에 열려있다.
class Manager(Employee):
    def work(self):
		print("매니징을 합니다")

class Company:
    def __init__(self, employees: List[Employee]):
        self.employees = employees

    # employee가 늘어나더라도 변경에는 닫혀있다.
    def make_work(self):
        for employee in self.employees:
            employee.work()
```

## Liskov Substitution  
---  
`Liskov Substitution Principle(리스코브 치환 원칙)`은 **부모 객체의 역할은 자식 객체도 할 수 있어야 된다는 원칙**이다.

B 객체가 A 객체의 자식이라면 B객체의 타입을 A로 바꾸더라도 작동에 문제가 없어야 한다. 상위 타입에서 정한 명세를 하위 타입에서도 그대로 지킬 수 있을 때 상속을 해야 한다.

일반적으로 **Liskov Substitution Principle이 지켜지지 않으면 Open Closed Principle을 위반하게 된다.**

### 위반할 사례1
```python
import abc

class Employee(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def work(self):
        ...

class Developer(Employee):
    def work(self):
        print("코딩을 합니다")
        return ["if..", "for..."]

class FrontEndDeveloper(Developer):
    def work(self):
        print("프론트엔드 개발을 합니다")
        #결과를 반환하지 않음

if __name__ == "__main__":
    def make_code(developer: Developer):
        code = developer.work()
        print(f"총 {len(code)}줄의 코드를 작성하였습니다")

    make_code(Developer())
    make_code(FrontEndDeveloper())
```

### 위반한 사례 2
```python
# 유명한 직사각형, 정사각형 사례
# 일반적으로 정사각형은 직사각형입니다. 즉 정사각형 is 직사각형의 관계이며, 이는 상속이 가능합니다. 
class Rectangle:
    def get_width(self):
        return self.width;

    def get_height(self):
        return self.height;

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

class Square(Rectangle):
    def set_width(self, width):
        self.width = width
        self.height = width
    
    def set_height(self, height):
        self.width = height
        self.height = height

if __name__ == "__main__":
	square = Square()
	square.set_width(20)
	square.set_height(30)
	check = square.get_width() == 20 && square.get_height() == 30 #부모의 명세와 다름
	
```

## Interface Segregation  
---
Interface Segregation은 **클라이언트가 자신이 이용하지 않는 메서드는 의존하지 않아야 한다는 원칙**이다.  
SOLID의 1 원칙인 Single Responsibility Principle은 객체가 하나의 책임만을 가져야 한다고 했는데, 여기서는 인터페이스(혹은 추상 클래스)가 하나의 책임만을 가져야 한다고 이해하면 된다.   

인터페이스를 책임에 맞게 잘 쪼개둔다면, 클라이언트 입장에서는 필요한 역할만 구현(혹은 상속)하여  사용할 수 있다.  

### AS-IS
```python
 from abc import *

class Smartphone(metaclass=ABCMeta):
	@abstractmethod
	def call(self):
		...

	@abstractmethod
	def send_message(self):
		...
	
	@abstractmethod
	def see_youtube(self):
		...
	
	@abstractmethod
	def take_picture(self):
		...

#카메라가 없는 클래스에서 take_picture는 불필요한 메서드가 된다.
class PhoneWithNoCamera(Smartphone):
	...
```

### TO-BE 
```python
#인터페이스를 역할 단위로 나눈다. 
class Telephone(metaclass=ABCMeta):
	@abstractmethod
	def call(self):
		...

	@abstractmethod
	def send_message(self):
		...
	
class Camera(metaclass=ABCMeta):
	@abstractmethod
	def take_picture(self):
		...

class Application(metaclass=ABCMeta):
	@abstractmethod
	def see_youtube(self):
        ...

class PhoneWithNoCamera(Telephone, Application):
	...

```

## Dependency Inversion 
---
Dependency Inversion princplie는 **의존성을 항상 고수준으로 향하게 하여 예측할 수 없는 의존성의 변화를 줄이자는 원칙**이다.  
일반적으로 의존성을 가지는 대상이 변경되면 의존하는 주체도 함께 변경된다.  
만약 자주 바뀌는 구현체(저수준)를 의존하게 된다면 코드의 변경이 잦을 것이며, 버그와 사이드 이펙트가 날 확률이 높아진다.  
이때 코드가 덜 바뀌는 인터페이스나 추상 클래스(고수준)을 의존한다면 상대적으로 안정적인 코드를 짤 수 있다.  

### 기본 코드 
```python
import abc

class Database:
    @abc.abstractmethod
    def connect(uri: str):
        ...
    
    @abc.abstractmethod
    def store_data(data: any):
        ...

class InMemoryDatabase(Database):
    def __init__(self):
        self.data = None
    
    def connect(uri: str):
        pass    
    
    def store_data(self, data):
        print("inmemory에 저장합니다")

class Mysqldatabase(Database):
    def connect(uri: str):
        print(f"{uri}에 연결합니다")
    
    def store_data(self, data):
        print("mysql에 저장합니다")
```

### AS-IS
```python
class App():
    def __init__(self):
        self.inmemory_db = InMemoryDatabase() #구현체에 의존하고 있습니다.
    
    def save_user(self, data):
        self.inmemory_db.store_data(data)

if __name__ == "__main__":
    app = App()
    app.save_user({"id":1,"name":"grab"})
```
만약 App에서 다른 데이터베이스를 사용하고 싶다면, 코드를 직접 변경해야 한다. 또한 App을 테스트하는 코드를 작성할 때도 의존성이 강하게 결합되어 테스트가 쉽지 않다.  

### TO-BE
1. 의존성 역전

```python 

class App():
    def __init__(self):
        # 고수준을 의존하지만 구현체를 구현하는 코드가 함께 들어있어 반쪽짜리 의존성 역전입니다. 
        self.inmemory_db : Database = InMemoryDatabase() 
    
    def save_user(self, data):
        self.inmemory_db.store_data(data)

if __name__ == "__main__":
    app = App()
    app.save_user({"id":1,"name":"grab"})
```

2. 의존성 주입과 함께
일반적으로 의존성 역전을 하면서 의존성 주입을 함께 사용한다.  
의존성 주입을 사용하게 되면 객체의 생성을 외부에 맡기게 된다. 그러면 해당 클래스는 외부 의존성에 조금 더 자유룝게 되며 테스트를 작성할 때도 용이하다.  
```python
class App():
    def __init__(self, database: Database): #고수준에 의존합니다. 
        self.database = database
    
    def save_user(self, data):
        self.database.store_data(data)

if __name__ == "__main__":
    inmemory_db = InMemoryDatabase()
    app = App(inmemory_db)  # 외부에서 의존성을 생성 후 주입해 줍니다. 
    app.save_user({"id":1,"name":"grab"})
```
> **TIP**  
 >의존성 주입(DI)을 해주기 위해선 결국 이를 사용하는 클라이언트에서 의존성들을 일일이 넣어줘야 합니다. 만약 잘못 코드를 작성하면 의존성 관계가 복잡해질 수 있습니다.
> 그래서 보통 의존성 주입을 별도로 관리해주는 라이브러리나 프레임워크를 사용합니다.
