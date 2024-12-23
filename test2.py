import re
from playwright.sync_api import Playwright, sync_playwright, expect

def test() -> None:
 with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.cheapoair.ca/")
    page.get_by_label("To where?").click()
    page.get_by_label("To where?").fill("bom")
    page.get_by_text("BOM - Mumbai, India").click()
    page.get_by_label("Choose a departure date.").click()
    page.get_by_text("One Way", exact=True).click()
    page.get_by_label("Choose a departure date.").click()
    page.get_by_label("13 January").click()
    page.get_by_role("button", name="Traveler").click()
    page.get_by_label("Add falseseniors").click()
    page.get_by_label("Added 1 falseadults").click()
    page.get_by_role("button", name="Search Flights").click()
    page.goto("https://www.cheapoair.ca/air/listing?&d1=YEA&r1=BOM&dt1=01/13/2025&tripType=ONEWAYTRIP&cl=ECONOMY&ad=2&se=1&ch=0&infs=0&infl=0&flightsearch=true")
    page.get_by_role("button", name="Modify Search").click()
    page.get_by_label("By Alliances").click()
    page.get_by_text("OneworldC$").click()
    page.get_by_label("Select this contract of 2630.").click()

    # ---------------------
    context.close()
    browser.close()



