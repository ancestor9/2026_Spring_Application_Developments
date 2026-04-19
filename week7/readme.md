## Modern Web
[동기방식, 동시성과 병렬성](동시성(Concurrency)_병렬성(Parallelism).pdf)
### 코드 실습
- 0422_sync_async_clean.ipynb
- 0422_concurrency.py

#### 4.1. Fast API Architecture
[Learn_FastAPI_01](Learn_FastAPI_01.pdf)

[Learn_FastAPI_02](Learn_FastAPI_02.pdf)

![](https://media.licdn.com/dms/image/v2/D4D12AQG_nawivlNG-Q/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1688666263274?e=1778112000&v=beta&t=Axaxao_igLjKrua2h2eBMFrr32bz6suIsO5pvcTJ3XA)

#### 4.2. Fast API 시작
- [FastAPI 맛보기](https://fastapi.tiangolo.com/ko/)
- [Firebase](https://www.youtube.com/watch?v=0A45kpsOCPY)
-     Firebase Studio에서 VIBE 코딩
      Firebase는 모바일 및 웹 애플리케이션을 개발하기 위한 구글의 플랫폼
- 가상환경 생성과 Fast API 설치(웹서버 uvicorn) -> Optional
-          - FastAPI framework: pip install fastapi
           - Uvicorn web server: pip install uvicorn
           - HTTPie text web client: pip install httpie
           - Requests synchronous web client package: pip install requests
           - HTTPX sync/async web client package: pip install httpx
#### 4.2.1.  Path와 Query Parameter 이해
-     REST API 설계 시 path는 “무엇(리소스)”을 요청하는지, query는 “어떻게(조건, 옵션)”을 요청하는지 전달하는 방식으로 구분해 활용
#### 4.2.2.  Request Body, Head
-     사전형, JSON, Pydantic 모듈 (Request/Response Body, POST Method), 여러 개 Request Body

### Fast API 코드 실습
