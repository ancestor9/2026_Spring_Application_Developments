## APIRouter를 사용하여 프로젝트를 구조화하고 모듈화하는 방법

1. 파일별 요약
- product.py: 제품(Product) 관련 API 엔드포인트들을 정의한 모듈로 제품 목록 조회, 상세 조회, 생성 기능을 포함
- customer.py: 고객(Customer) 관련 API 엔드포인트들을 정의한 모듈로 고객 목록 조회 및 상세 조회 기능을 포함
- main_product_customer.py: 메인 애플리케이션 파일로 product.py와 customer.py에서 정의한 라우터들을 하나로 통합(include_router)하여 실제로 서버를 실행하는 역할

2. Router(APIRouter)의 기능 설명
APIRouter는 "미니 FastAPI 앱"으로 규모가 큰 애플리케이션을 만들 때 모든 경로(Route)를 파일 하나에 작성하면 코드가 복잡해지는데, 이를 해결하기 위해 사용
- 주요 특징 및 장점: 코드의 구조화 (Modularity), 기능별(예: 제품 관리, 사용자 관리, 주문 관리)로 파일을 나누어 관리할 수 있어 유지보수의 용이성
- 접두사(Prefix) 설정:
-     router = APIRouter(prefix="/product")와 같이 설정하면, 해당 파일 내의 모든 경로 앞에 자동으로 /product가 붙dma (예: @router.get("/")는 실제 주소에서 /product/가 됨)
-     태그(Tags) 지정:tags=["products"]를 설정하면 Swagger UI(자동 생성 문서)에서 관련 API들을 그룹화하여 보기 좋게 표시
-     공통 설정 적용: 특정 라우터 전체에 공통적인 인증(Dependencies)이나 응답 메시지(404 오류 등)를 한 번에 적용할 수 있습니다.

3. 작동 방식 요약:
- 각 도메인 파일(product.py, customer.py)에서 APIRouter 객체를 생성하고 API를 정의
- 메인 파일(main_product_customer.py)에서 이 라우터들을 import
- app.include_router(router) 명령어를 통해 메인 앱에 하나로 합쳐서 실행
