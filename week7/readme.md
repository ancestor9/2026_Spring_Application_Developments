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
- 가상환경 생성과 Fast API 설치(웹서버 uvicorn) -> Optional
-          - FastAPI framework: pip install fastapi
           - Uvicorn web server: pip install uvicorn
           - HTTPie text web client: pip install httpie
           - Requests synchronous web client package: pip install requests
           - HTTPX sync/async web client package: pip install httpx

### Fast API 코드 실습 (순차적 학습)
- [FastAPI 맛보기](https://fastapi.tiangolo.com/ko/)
- main_server.py & client.py : CLient-Server 구조를 이해(request <---> response)
- main.py : 메모리에 저장된 상품 데이터를 조회, 추가, 수정하고 이를 CSV 파일로 다운로드 가능 --> CRUD를 직접 try it out !
- main_CRUD.py : Pydantic 모델을 활용하여 데이터의 형식 검증과 응답 모델링을 적용한 RESTful API의 CRUD(생성·조회·수정·삭제)

### Appendix
- [Firebase](https://www.youtube.com/watch?v=0A45kpsOCPY)
-     Firebase Studio에서 VIBE 코딩
      Firebase는 모바일 및 웹 애플리케이션을 개발하기 위한 구글의 플랫폼
