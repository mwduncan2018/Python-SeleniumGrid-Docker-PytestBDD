from pytest_bdd import scenario, scenarios, given, when, then, parsers

from pagemodels.page import Page
from testdata.model.product import Product
from testdata.provider.product_provider import ProductProvider

scenarios('../features/fuzzy_matching.feature')


@when("fuzzy matching is enabled")
def _(scenario_context):
    page: Page = scenario_context["page"]

    page.navbar.go_to_product_dashboard()
    page.product_dashboard.enable_fuzzy_matching()

@then(parsers.parse("the product with manufacturer {productManufacturer} and model {productModel} is a fuzzy match"))
def _(scenario_context, productManufacturer, productModel):
    page: Page = scenario_context["page"]

    page.navbar.go_to_product_dashboard()
    page.product_dashboard.enable_fuzzy_matching()
    assert page.product_dashboard.is_product_a_fuzzy_match(Product(productManufacturer, productModel, 100, 100))

@then(parsers.parse("the product with manufacturer {productManufacturer} and model {productModel} is not a fuzzy match"))
def _(scenario_context: dict, productManufacturer, productModel):
    page: Page = scenario_context["page"]

    page.navbar.go_to_product_dashboard()
    page.product_dashboard.enable_fuzzy_matching()
    assert not page.product_dashboard.is_product_a_fuzzy_match(Product( productManufacturer, productModel, 100, 100))