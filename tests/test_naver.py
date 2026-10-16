import re
from playwright.sync_api import Page, expect

SEARCH_KEYWORD = "Playwright 자동화"

def test_naver_search_box_exists(page: Page):
    """TC-1: 네이버 검색창 확인"""
    page.goto("https://www.naver.com")
    expect(page).to_have_title("NAVER")
    expect(page.locator("#query")).to_be_visible()

def test_naver_search(page: Page):
    """TC-2: 검색어 입력 및 검색 실행"""
    page.goto("https://www.naver.com")
    page.locator("#query").fill(SEARCH_KEYWORD)
    page.locator("#query").press("Enter")
    page.wait_for_url("**/search.naver**")
    expect(page).to_have_url(re.compile(r"https://search\.naver\.com/search\.naver\?.*"))
def test_naver_search_results(page: Page):
    """TC-3: 검색 결과 페이지에서 검색어 확인"""
    page.goto("https://www.naver.com")
    page.locator("#query").fill(SEARCH_KEYWORD)
    page.locator("#query").press("Enter")
    page.wait_for_url("**/search.naver**")
    expect(page.locator("body")).to_contain_text(SEARCH_KEYWORD)
    print("검색 결과 페이지에서 검색어 확인 완료!")