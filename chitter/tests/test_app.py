from playwright.sync_api import Page, expect

def test_get_index(db_connection, page, test_web_address):
    page.goto(f"http://{test_web_address}/")

    div_tags = page.locator("div")
    expect(div_tags).to_have_id("1")

    timestamps = page.locator(".timestamp")
    expect(timestamps).to_have_text("2023-12-07 11:13:15")

    contents = page.locator(".content")
    expect(contents).to_have_text("Welcome to Chitter!")

    by_users = page.locator(".by-user")
    expect(by_users).to_have_text("JMcK4529")