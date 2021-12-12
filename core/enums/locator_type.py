import enum


class LocatorType(enum.Enum):
    xpath = "xpath"
    name = "name"
    class_name = "class name"
    id = "id"
    tag_name = "tag name"
    css_selector = "css selector"
