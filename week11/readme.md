## Injection 
- FastAPI에서 **의존성 주입(Dependency Injection, DI)* *은 코드의 재사용성을 높이고, 테스트를 쉽게 만들며, 로직을 깔끔하게 분리할 수 있게 해주는 아주 강력한 도구
-         프로그래밍에서 의존성 주입은 객체가 필요한 객체(의존성)를 직접 생성하는 것이 아니라, 외부에서 넣어주는 방식
-         FastAPI에서는 Depends라는 클래스를 사용하여 구현
-     from typing import Annotated
      from fastapi import Depends, FastAPI
      app = FastAPI()
      # 1. 의존성 함수 정의
      async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
          return {"q": q, "skip": skip, "limit": limit}
      @app.get("/items/")
      # 2. Depends를 통한 주입
      async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
          return commons
      @app.get("/users/")
      async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
          return commons
