from pytest_bdd import scenario, scenarios, given, when, then, parsers

from pagemodels.page import Page
from testdata.model.product import Product
from testdata.provider.watchlist_entry_provider import WatchListEntryProvider
from testdata.provider.product_provider import ProductProvider

scenarios('../features/standard_matching.feature')


@when("standard matching is enabled")
def _(scenario_context):
    page: Page = scenario_context["page"]

    page.navbar.go_to_product_dashboard()
    page.product_dashboard.enable_standard_matching()

@then(parsers.parse("the product with manufacturer {productManufacturer} and model {productModel} is not a standard match"))
def _(scenario_context: dict, productManufacturer, productModel):
    page: Page = scenario_context["page"]

    page.navbar.go_to_product_dashboard()
    page.product_dashboard.enable_standard_matching()
    assert not page.product_dashboard.is_product_a_standard_match(Product(productManufacturer, productModel, 100, 100))

