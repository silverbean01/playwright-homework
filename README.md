# Playwright 네이버 검색 자동화 테스트

## 실습 내용
Python, pytest, Playwright를 활용하여 네이버 검색 기능을 자동으로 테스트했습니다.

## 테스트 항목
- TC-1: 네이버 접속 및 검색창 표시 확인
- TC-2: 검색어 입력 및 검색 실행 확인
- TC-3: 검색 결과 페이지에서 검색어 확인

## 실행 방법
1. pip install -r requirements.txt
2. python -m playwright install chromium
3. python -m pytest tests/test_naver.py -v

## 테스트 결과
- 총 3개 테스트 실행
- 3 passed (모두 통과)
- 실행 시간: 5.40초