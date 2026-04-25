## 1. Injection 
- FastAPI에서 **의존성 주입(Dependency Injection, DI)* *은 코드의 재사용성을 높이고, 테스트를 쉽게 만들며, 로직을 깔끔하게 분리할 수 있게 해주는 아주 강력한 도구
-         프로그래밍에서 의존성 주입은 객체가 필요한 객체(의존성)를 직접 생성하는 것이 아니라, 외부에서 넣어주는 방식
-         FastAPI에서는 Depends라는 클래스를 사용하여 구현
            from typing import Annotated
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

## 2. Streamlit 
- Streamlit과 FastAPI를 연동하는 가장 표준적인 방법은 Client-Server 구조
-       Streamlit은 사용자 인터페이스(Frontend)를 담당(View)
        FastAPI는 로직이나 데이터 처리(Backend)를 담당(Control)
        두 사이는 requests 라이브러리로 통신
        Database(Model) : Injection 사용하여 요청시 DB 세션을 열고, 작업이 끝나면 자동으로 닫기
            def get_db():
            db = SessionLocal()
            try:
              yield db  # 요청 처리 시 DB 세션 제공
            finally:
              db.close() # 요청이 끝나면 자동으로 세션 종료
                  
            @app.get("/items/{item_id}")
            def read_item(item_id: int, db: Session = Depends(get_db)):
                return db.query(Item).filter(Item.id == item_id).first()
