## Modern Web
[동기방식, 동시성과 병렬성](동시성(Concurrency)_병렬성(Parallelism).pdf)
### 코드 실습
- 0422_sync_async_clean.ipynb
- 0422_concurrency.py

### MVC (Model-View-Controller) 패턴이란?
- 소프트웨어 공학에서 사용되는 **모델-뷰-컨트롤러(Model-View-Controller)**라는 디자인 패턴
- 애플리케이션의 데이터(모델), 사용자 인터페이스(뷰), 그리고 데이터와 뷰 사이의 논리 및 흐름을 제어하는(컨트롤러) 세 부분으로 나누는 방법

<img src="https://tecoble.techcourse.co.kr/static/c73f913a7c220ec8cb3ee9a8579468b4/73a7d/mvc.avif" width="600" height="500">

- Can you recognize model, view, controller in the below playing Logo picture? 

![](https://images.unsplash.com/photo-1575364289437-fb1479d52732?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTF8fCVFQiU4NiU4MCVFQiU4QiVBNHxlbnwwfHwwfHx8MA%3D%3D)

### Modern Web Architecture
<img src="https://www.simform.com/wp-content/uploads/2021/05/webapparchitecture5.png" width="600" height="500">


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
