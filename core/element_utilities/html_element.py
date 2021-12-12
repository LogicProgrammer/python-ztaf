from core.enums.element_type import ElementType
from core.enums.locator_type import LocatorType
from .element_info import ElementInfo


def html_element(element_type=ElementType.element, template=ElementType.invalid, index=1, loc='',
                 loc_type=LocatorType.xpath):
    def decorator(func):
        def inner(self):
            info = ElementInfo()
            info.name = func.__name__
            info.value = func(self)
            info.type = element_type
            info.template = template
            info.index = index
            info.loc_type = loc_type
            info.loc = loc
            return info

        return inner

    return decorator
