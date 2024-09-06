from typing import List
import pytest
import requests
from pytest_bdd import given, when, then, parsers 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException


from pagemodels.page import Page
from testdata.model.product import Product
from testdata.model.watchlist_entry import WatchListEntry
from testdata.provider.product_provider import ProductProvider
from testdata.provider.watchlist_entry_provider import WatchListEntryProvider
from configprovider.config_provider import ConfigProvider
from driverprovider.driver_provider import DriverProvider


# Shared fixtures

def clean_up_all_product_test_data():
    page: Page = Page(DriverProvider.get_driver())
    for product in ProductProvider.get_all_products():
        page.navbar.go_to_product_dashboard()
        if page.product_dashboard.is_product_displayed_in_table(product):
            page.product_dashboard.delete(product)
            page.product_delete.confirm_delete()
            page.close_app()

def clean_up_all_watchlist_test_data():
    page: Page = Page(DriverProvider.get_driver())
    for entry in WatchListEntryProvider.get_all_entries():
        page.navbar.go_to_watchlist_dashboard()
        if page.watchlist_dashboard.is_entry_displayed_in_table(entry):
            page.watchlist_dashboard.delete(entry)
            page.watchlist_delete.confirm_delete()
            page.close_app()

@pytest.fixture(scope="session", autouse=True)
def before_all_and_after_all():
    # Initialize test data
    ProductProvider.initialize_test_data()
    WatchListEntryProvider.initialize_test_data()
    yield
    
@pytest.fixture 
def scenario_context():
    # Initialize all page objects
    page = Page(DriverProvider.get_driver())
    # Store the page objects in scenario context
    sc = { "page": page }
    # Open the browser
    page.open_app()
    yield sc
    # Clean up product test data for this scenario
    if "product" in sc:
        product: Product = sc["product"]
        url = ConfigProvider.get_url() + "/ProductListApi/Delete/" + product.manufacturer + "/" + product.model
        requests.delete(url)
    # Clean up watchlist entry test data for this scenario
    if "watchlist_entry" in sc:
        watchlist_entry: WatchListEntry = sc["watchlist_entry"]
        url = ConfigProvider.get_url() + "/WatchListApi/Delete/" + watchlist_entry.manufacturer + "/" + watchlist_entry.model
        requests.delete(url)
    # Close the browser
    page.close_app()


# Shared steps 

@given(parsers.parse("a product is added with manufacturer {productManufacturer} and model {productModel}"))
def _(scenario_context: dict, productManufacturer, productModel):
    page: Page = scenario_context["page"]
    product = Product(productManufacturer, productModel, 100, 100)
    scenario_context["product"] = product

    page.navbar.go_to_product_dashboard()
    page.product_dashboard.add_new_product()
    page.product_add.add_product(product)

@given(parsers.parse("an entry is added with manufacturer {entryManufacturer} and model {entryModel}"))
def _(scenario_context: dict, entryManufacturer, entryModel):
    page: Page = scenario_context["page"]
    watchlist_entry = WatchListEntry(entryManufacturer, entryModel)
    scenario_context["watchlist_entry"] = watchlist_entry

    page.navbar.go_to_watchlist_dashboard()
    page.watchlist_dashboard.add_new_entry()
    page.watchlist_add.add_entry(watchlist_entry)

@then(parsers.parse("the product with manufacturer {productManufacturer} and model {productModel} is a standard match"))
def _(scenario_context: dict, productManufacturer, productModel):
    page: Page = scenario_context["page"]

    page.navbar.go_to_product_dashboard()
    page.product_dashboard.enable_standard_matching()
    assert page.product_dashboard.is_product_a_standard_match(Product(productManufacturer, productModel, 100, 100))