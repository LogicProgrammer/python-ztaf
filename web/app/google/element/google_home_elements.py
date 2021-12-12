from core.element_utilities.element_info import ElementInfo
from core.enums.locator_type import LocatorType


class IGoogleHome:
    name = "btnK"
    search_box: ElementInfo = ElementInfo(value="search box", loc_type=LocatorType.name, loc='q')
    search_button: ElementInfo = ElementInfo(value="search button", loc=f'//input[@name="{name}"]', index=2)

    # @html_element(loc_type=LocatorType.name, loc='q')
    # def search_box(self):
    #     return "google search box"
    #
    # @html_element(loc_type=LocatorType.xpath, loc=f'//input[@name="{name}"]', index=2,
    # element_type=ElementType.button) def search_button(self): return "google search button"
