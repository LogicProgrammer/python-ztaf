import logging

from behave import *

log = logging.getLogger(__name__)


@given("user opens website {url}")
def launch_url(context, url):
    log.info("launching url")


@when("user performs an action")
def launch_url(context):
    log.info(f"user performs action in the page")


@then("user verifies data")
def launch_url(context):
    log.info("user verifies data in the page")
