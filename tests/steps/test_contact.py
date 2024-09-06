from pytest_bdd import scenario, scenarios, given, when, then, parsers

from pagemodels.page import Page


scenarios('../features/contact.feature')

@when("the Contact page is viewed")
def _(scenario_context: dict):
    page: Page = scenario_context["page"]
    page.navbar.go_to_contact()
    import time
    time.sleep(1)


@then(parsers.parse("the footer text should include {footerText} within {seconds:d} seconds"))
def _(scenario_context: dict, footerText: str, seconds: int):
    page: Page = scenario_context["page"]
    assert page.contact.does_footer_text_contain(footerText, seconds)
    import time
    time.sleep(1)

@then(parsers.parse("the GitHub link {gitHub} should be provided"))
def _(scenario_context: dict, gitHub: str):
    page: Page = scenario_context["page"]
    assert page.contact.get_github_href() == gitHub
    import time
    time.sleep(1)

@then(parsers.parse("the following {skill} should be listed"))
def _(scenario_context: dict, skill: str):
    page: Page = scenario_context["page"]
    assert skill in page.contact.get_list_of_skills()
    import time
    time.sleep(1)
