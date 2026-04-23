
# 📌 Chinook EDA Dashboard 코드 요약

## 🎯 목적
- SQLite 기반 Chinook DB 분석
- FastAPI + Gradio 통합 웹 서비스

---

## 🗄 DB 처리
- DB 없으면 GitHub에서 자동 다운로드
- SQLite + Pandas로 데이터 조회

---

## 🔍 데이터 조회 기능
- `get_tables()` → 테이블 목록 조회
- `preview_table()` → 테이블 상위 10개 조회
- `run_sql()` → 사용자 SQL 실행

---

## 📊 EDA 시각화
- 장르별 트랙 수
- 국가별 매출
- 결과 → 이미지(PIL) 반환

---

## 🖥 Gradio UI
- 4개 탭 구성
  1. 테이블 목록
  2. 테이블 미리보기
  3. SQL 실행
  4. 시각화
- 버튼 클릭 → 함수 실행 → 결과 출력

---

## 🚀 FastAPI 통합
- `/` → API 상태 확인
- `/gradio` → Gradio UI 접속
- `mount_gradio_app()` 사용하여 통합 실행

---

## 🔄 실행 흐름
사용자 → Gradio UI → FastAPI → SQLite → 결과 반환

---

## 📌 핵심 포인트
- DB → SQL → 시각화 → UI 흐름 구현
- FastAPI + Gradio 결합 구조
- 데이터 분석 대시보드 실습 예제
