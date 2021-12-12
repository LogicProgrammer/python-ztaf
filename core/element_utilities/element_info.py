from core.enums.element_type import ElementType
from core.enums.locator_type import LocatorType


class ElementInfo:

    def __init__(self, value=None, element_type=ElementType.element, template=ElementType.invalid, index=1,
                 loc_type=LocatorType.xpath, loc=None):
        self.__name = None
        self.__value = value
        self.__type = element_type
        self.__template = template
        self.__index = index
        self.__loc_type = loc_type
        self.__loc = loc
        self.__by_loc = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def template(self):
        return self.__template

    @template.setter
    def template(self, value):
        self.__template = value

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, value):
        self.__index = value

    @property
    def loc_type(self):
        return self.__loc_type

    @loc_type.setter
    def loc_type(self, value):
        self.__loc_type = value

    @property
    def loc(self):
        return self.__loc

    @loc.setter
    def loc(self, value):
        self.__loc = value

    @property
    def by_loc(self):
        return self.__by_loc

    @by_loc.setter
    def by_loc(self, value):
        self.__by_loc = value
