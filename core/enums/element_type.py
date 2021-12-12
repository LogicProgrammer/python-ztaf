import enum


class ElementType(enum.Enum):
    input = 0
    select = 1
    button = 2
    date_picker = 3
    checkbox = 4
    text_area = 5
    section_title = 6
    sub_section_title = 7
    label = 8
    side_menu = 9
    sub_menu = 10
    radio = 11
    tab = 12
    table = 13
    table_add_button = 14
    table_remove_button = 15
    yes_or_no = 16
    yes_radio = 17
    no_radio = 18
    table_yes_or_no = 19
    expand_button = 20
    label_checkbox = 21
    label_value = 22
    table_input = 23
    table_checkbox = 24
    table_select = 25
    table_label = 26
    yes_table_radio = 27
    no_table_radio = 28
    form_section = 29
    element = 30
    invalid = 31
