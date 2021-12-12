guidewire_10 = {
    'policy_center' : {
        "link": "//a[text()={label}]",
        "input": "//div[text()={label}]//..//div[contains(@class,'ValueWidget gw-editable')]//input",
        "select": "//div[text()={label}]//..//div[contains(@class,'gw-RangeValueWidget')]//select",
        "button": "//div[contains(normalize-space(.),{label})][contains(@class,'button gw-actionable') or (contains("
                  "@class,'gw-action--outer') and contains(@class,'Button'))]",
        "datePicker": "//div[text()={label}]//..//div[contains(@class,'parentForDatePicker')]//input",
        "checkbox": "//*[text()={label}]//parent::div//input[@type='checkbox']",
        "text_area": "//div[text()={label}]//..//div[2]/div[contains(@class,'InputWidget gw-ValueWidget "
                     "gw-editable')]/div/textarea",
        "section_title": "//div[text()={label} and contains(@class,'TitleBar')]",
        "sub_section_title": "//div[contains(@class,'boldLabel')][text()={label})]//ancestor::div[contains(@class,"
                             "'gw-LabelWidget')]",
        "label": "//div[text()={label}]/following-sibling::div//div[contains(@class,'ActionValueWidget') or contains("
                 "@class,'ValueWidget gw-readonly')]",
        "side_menu": "//div[text()={label}]//ancestor::div[contains(@class,'styleTag--MenuLinksWidget "
                     "gw-WestPanelMenuItem')]",
        "sub_menu": "//div[normalize-space(.)={label}]//ancestor::div[contains(@class,'styleTag--MenuItemWidget "
                    "gw-WestPanelMenuItem')]",
        "radio": "//*[text()={label}]//parent::*//input[@type='radio']",
        "tab": "//div[normalize-space(.)={label}]//parent::div[@role='tab']",
        "table": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//following-sibling::div["
                 "contains(@class,'table-wrapper')]//table/tbody",
        "table_add_button": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//div[contains("
                            "normalize-space(.),'Add')][contains(@role,'button')]",
        "table_remove_button": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//div[contains("
                               "normalize-space(.),'Remove')][contains(@role,'button')]",
        "yes_or_no": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'{option}')]/parent::*//input",
        "yes_radio": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'Yes')]/parent::*//input",
        "no_radio": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'No')]/parent::*//input",
        "expand_button": "//div[contains(text(),{label})]//parent::div[contains(@class,'InputColumnWidget')]//div["
                         "contains(@class,'expand-button')]",
        "table_yes_or_no": "//*[contains(text(), {label})]/../../../../following-sibling::td//span[contains(text(),"
                           "'{option}')]/parent::*//input",
        "table_yes_radio": "//div[contains(text(),{label})]//ancestor::tr//td//div//span[contains(text(),"
                           "'Yes')]/parent::*//input",
        "table_no_radio": "//div[contains(text(),{label})]//ancestor::tr//td//div//span[contains(text(),"
                          "'No')]/parent::*//input",
        "table_input": "//*[text()={label}]/ancestor::td/following-sibling::td//input",
        "table_checkbox": "//*[text()={label}]/ancestor::td/following-sibling::td//input",
        "table_select": "//*[text()={label}]/ancestor::td/following-sibling::td//select",
        "table_text_area": "//*[text()={label}]/ancestor::td/following-sibling::td//textarea",
        "table_label": "//div[text()={label}]//ancestor::tr//div//div//div//div",
        "form_section": "//div[@aria-label={label}][@role='group']"
    },
    "billing_center": {
        "input": "//div[text()={label}]//..//div[contains(@class,'ValueWidget gw-editable')]//input",
        "select": "//div[text()={label}]//..//div[contains(@class,'gw-RangeValueWidget')]//select",
        "button": "//div[contains(normalize-space(.),{label})][contains(@class,'button gw-actionable') or (contains("
                  "@class,'gw-action--outer') and contains(@class,'Button'))]",
        "datePicker": "//div[text()={label}]//..//div[contains(@class,'parentForDatePicker')]//input",
        "checkbox": "//*[text()={label}]//parent::div//input[@type='checkbox']",
        "text_area": "//div[text()={label}]//..//div[2]/div[contains(@class,'InputWidget gw-ValueWidget "
                     "gw-editable')]/div/textarea",
        "section_title": "//div[text()={label} and contains(@class,'TitleBar')]",
        "sub_section_title": "//div[contains(@class,'boldLabel')][text()={label})]//ancestor::div[contains(@class,"
                             "'gw-LabelWidget')]",
        "label": "//div[text()={label}]/following-sibling::div//div[contains(@class,'ActionValueWidget') or contains("
                 "@class,'ValueWidget gw-readonly')]",
        "side_menu": "//div[text()={label}]//ancestor::div[contains(@class,'styleTag--MenuLinksWidget "
                     "gw-WestPanelMenuItem')]",
        "sub_menu": "//div[normalize-space(.)={label}]//ancestor::div[contains(@class,'styleTag--MenuItemWidget "
                    "gw-WestPanelMenuItem')]",
        "radio": "//*[text()={label}]//parent::*//input[@type='radio']",
        "tab": "//div[normalize-space(.)={label}]//parent::div[@role='tab']",
        "table": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//following-sibling::div["
                 "contains(@class,'table-wrapper')]//table/tbody",
        "table_add_button": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//div[contains("
                            "normalize-space(.),'Add')][contains(@role,'button')]",
        "table_remove_button": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//div[contains("
                               "normalize-space(.),'Remove')][contains(@role,'button')]",
        "yes_or_no": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'{option}')]/parent::*//input",
        "yes_radio": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'Yes')]/parent::*//input",
        "no_radio": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'No')]/parent::*//input",
        "expand_button": "//div[contains(text(),{label})]//parent::div[contains(@class,'InputColumnWidget')]//div["
                         "contains(@class,'expand-button')]",
        "table_yes_or_no": "//*[contains(text(), {label})]/../../../../following-sibling::td//span[contains(text(),"
                           "'{option}')]/parent::*//input",
        "table_yes_radio": "//div[contains(text(),{label})]//ancestor::tr//td//div//span[contains(text(),"
                           "'Yes')]/parent::*//input",
        "table_no_radio": "//div[contains(text(),{label})]//ancestor::tr//td//div//span[contains(text(),"
                          "'No')]/parent::*//input",
        "table_input": "//*[text()={label}]/ancestor::td/following-sibling::td//input",
        "table_checkbox": "//*[text()={label}]/ancestor::td/following-sibling::td//input",
        "table_select": "//*[text()={label}]/ancestor::td/following-sibling::td//select",
        "table_text_area": "//*[text()={label}]/ancestor::td/following-sibling::td//textarea",
        "table_label": "//div[text()={label}]//ancestor::tr//div//div//div//div",
        "form_section": "//div[@aria-label={label}][@role='group']"
    },
    "claim_center": {
        "input": "//div[text()={label}]//..//div[contains(@class,'ValueWidget gw-editable')]//input",
        "select": "//div[text()={label}]//..//div[contains(@class,'gw-RangeValueWidget')]//select",
        "button": "//div[contains(normalize-space(.),{label})][contains(@class,'button gw-actionable') or (contains("
                  "@class,'gw-action--outer') and contains(@class,'Button'))]",
        "datePicker": "//div[text()={label}]//..//div[contains(@class,'parentForDatePicker')]//input",
        "checkbox": "//*[text()={label}]//parent::div//input[@type='checkbox']",
        "text_area": "//div[text()={label}]//..//div[2]/div[contains(@class,'InputWidget gw-ValueWidget "
                     "gw-editable')]/div/textarea",
        "section_title": "//div[text()={label} and contains(@class,'TitleBar')]",
        "sub_section_title": "//div[contains(@class,'boldLabel')][text()={label})]//ancestor::div[contains(@class,"
                             "'gw-LabelWidget')]",
        "label": "//div[text()={label}]/following-sibling::div//div[contains(@class,'ActionValueWidget') or contains("
                 "@class,'ValueWidget gw-readonly')]",
        "side_menu": "//div[text()={label}]//ancestor::div[contains(@class,'styleTag--MenuLinksWidget "
                     "gw-WestPanelMenuItem')]",
        "sub_menu": "//div[normalize-space(.)={label}]//ancestor::div[contains(@class,'styleTag--MenuItemWidget "
                    "gw-WestPanelMenuItem')]",
        "radio": "//*[text()={label}]//parent::*//input[@type='radio']",
        "tab": "//div[normalize-space(.)={label}]//parent::div[@role='tab']",
        "table": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//following-sibling::div["
                 "contains(@class,'table-wrapper')]//table/tbody",
        "table_add_button": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//div[contains("
                            "normalize-space(.),'Add')][contains(@role,'button')]",
        "table_remove_button": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//div[contains("
                               "normalize-space(.),'Remove')][contains(@role,'button')]",
        "yes_or_no": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'{option}')]/parent::*//input",
        "yes_radio": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'Yes')]/parent::*//input",
        "no_radio": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'No')]/parent::*//input",
        "expand_button": "//div[contains(text(),{label})]//parent::div[contains(@class,'InputColumnWidget')]//div["
                         "contains(@class,'expand-button')]",
        "table_yes_or_no": "//*[contains(text(), {label})]/../../../../following-sibling::td//span[contains(text(),"
                           "'{option}')]/parent::*//input",
        "table_yes_radio": "//div[contains(text(),{label})]//ancestor::tr//td//div//span[contains(text(),"
                           "'Yes')]/parent::*//input",
        "table_no_radio": "//div[contains(text(),{label})]//ancestor::tr//td//div//span[contains(text(),"
                          "'No')]/parent::*//input",
        "table_input": "//*[text()={label}]/ancestor::td/following-sibling::td//input",
        "table_checkbox": "//*[text()={label}]/ancestor::td/following-sibling::td//input",
        "table_select": "//*[text()={label}]/ancestor::td/following-sibling::td//select",
        "table_text_area": "//*[text()={label}]/ancestor::td/following-sibling::td//textarea",
        "table_label": "//div[text()={label}]//ancestor::tr//div//div//div//div",
        "form_section": "//div[@aria-label={label}][@role='group']"
    }
}

guidewire_9 = {
    "policy_center": {
        "link": "//a[text()={label}]",
        "input": "//div[text()={label}]//..//div[contains(@class,'ValueWidget gw-editable')]//input",
        "select": "//div[text()={label}]//..//div[contains(@class,'gw-RangeValueWidget')]//select",
        "button": "//div[contains(normalize-space(.),{label})][contains(@class,'button gw-actionable') or (contains("
                  "@class,'gw-action--outer') and contains(@class,'Button'))]",
        "datePicker": "//div[text()={label}]//..//div[contains(@class,'parentForDatePicker')]//input",
        "checkbox": "//*[text()={label}]//parent::div//input[@type='checkbox']",
        "text_area": "//div[text()={label}]//..//div[2]/div[contains(@class,'InputWidget gw-ValueWidget "
                     "gw-editable')]/div/textarea",
        "section_title": "//div[text()={label} and contains(@class,'TitleBar')]",
        "sub_section_title": "//div[contains(@class,'boldLabel')][text()={label})]//ancestor::div[contains(@class,"
                             "'gw-LabelWidget')]",
        "label": "//div[text()={label}]/following-sibling::div//div[contains(@class,'ActionValueWidget') or contains("
                 "@class,'ValueWidget gw-readonly')]",
        "side_menu": "//div[text()={label}]//ancestor::div[contains(@class,'styleTag--MenuLinksWidget "
                     "gw-WestPanelMenuItem')]",
        "sub_menu": "//div[normalize-space(.)={label}]//ancestor::div[contains(@class,'styleTag--MenuItemWidget "
                    "gw-WestPanelMenuItem')]",
        "radio": "//*[text()={label}]//parent::*//input[@type='radio']",
        "tab": "//div[normalize-space(.)={label}]//parent::div[@role='tab']",
        "table": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//following-sibling::div["
                 "contains(@class,'table-wrapper')]//table/tbody",
        "table_add_button": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//div[contains("
                            "normalize-space(.),'Add')][contains(@role,'button')]",
        "table_remove_button": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//div[contains("
                               "normalize-space(.),'Remove')][contains(@role,'button')]",
        "yes_or_no": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'{option}')]/parent::*//input",
        "yes_radio": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'Yes')]/parent::*//input",
        "no_radio": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'No')]/parent::*//input",
        "expand_button": "//div[contains(text(),{label})]//parent::div[contains(@class,'InputColumnWidget')]//div["
                         "contains(@class,'expand-button')]",
        "table_yes_or_no": "//*[contains(text(), {label})]/../../../../following-sibling::td//span[contains(text(),"
                           "'{option}')]/parent::*//input",
        "table_yes_radio": "//div[contains(text(),{label})]//ancestor::tr//td//div//span[contains(text(),"
                           "'Yes')]/parent::*//input",
        "table_no_radio": "//div[contains(text(),{label})]//ancestor::tr//td//div//span[contains(text(),"
                          "'No')]/parent::*//input",
        "table_input": "//*[text()={label}]/ancestor::td/following-sibling::td//input",
        "table_checkbox": "//*[text()={label}]/ancestor::td/following-sibling::td//input",
        "table_select": "//*[text()={label}]/ancestor::td/following-sibling::td//select",
        "table_text_area": "//*[text()={label}]/ancestor::td/following-sibling::td//textarea",
        "table_label": "//div[text()={label}]//ancestor::tr//div//div//div//div",
        "form_section": "//div[@aria-label={label}][@role='group']"
    },
    "billing_center": {
        "input": "//div[text()={label}]//..//div[contains(@class,'ValueWidget gw-editable')]//input",
        "select": "//div[text()={label}]//..//div[contains(@class,'gw-RangeValueWidget')]//select",
        "button": "//div[contains(normalize-space(.),{label})][contains(@class,'button gw-actionable') or (contains("
                  "@class,'gw-action--outer') and contains(@class,'Button'))]",
        "datePicker": "//div[text()={label}]//..//div[contains(@class,'parentForDatePicker')]//input",
        "checkbox": "//*[text()={label}]//parent::div//input[@type='checkbox']",
        "text_area": "//div[text()={label}]//..//div[2]/div[contains(@class,'InputWidget gw-ValueWidget "
                     "gw-editable')]/div/textarea",
        "section_title": "//div[text()={label} and contains(@class,'TitleBar')]",
        "sub_section_title": "//div[contains(@class,'boldLabel')][text()={label})]//ancestor::div[contains(@class,"
                             "'gw-LabelWidget')]",
        "label": "//div[text()={label}]/following-sibling::div//div[contains(@class,'ActionValueWidget') or contains("
                 "@class,'ValueWidget gw-readonly')]",
        "side_menu": "//div[text()={label}]//ancestor::div[contains(@class,'styleTag--MenuLinksWidget "
                     "gw-WestPanelMenuItem')]",
        "sub_menu": "//div[normalize-space(.)={label}]//ancestor::div[contains(@class,'styleTag--MenuItemWidget "
                    "gw-WestPanelMenuItem')]",
        "radio": "//*[text()={label}]//parent::*//input[@type='radio']",
        "tab": "//div[normalize-space(.)={label}]//parent::div[@role='tab']",
        "table": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//following-sibling::div["
                 "contains(@class,'table-wrapper')]//table/tbody",
        "table_add_button": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//div[contains("
                            "normalize-space(.),'Add')][contains(@role,'button')]",
        "table_remove_button": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//div[contains("
                               "normalize-space(.),'Remove')][contains(@role,'button')]",
        "yes_or_no": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'{option}')]/parent::*//input",
        "yes_radio": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'Yes')]/parent::*//input",
        "no_radio": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'No')]/parent::*//input",
        "expand_button": "//div[contains(text(),{label})]//parent::div[contains(@class,'InputColumnWidget')]//div["
                         "contains(@class,'expand-button')]",
        "table_yes_or_no": "//*[contains(text(), {label})]/../../../../following-sibling::td//span[contains(text(),"
                           "'{option}')]/parent::*//input",
        "table_yes_radio": "//div[contains(text(),{label})]//ancestor::tr//td//div//span[contains(text(),"
                           "'Yes')]/parent::*//input",
        "table_no_radio": "//div[contains(text(),{label})]//ancestor::tr//td//div//span[contains(text(),"
                          "'No')]/parent::*//input",
        "table_input": "//*[text()={label}]/ancestor::td/following-sibling::td//input",
        "table_checkbox": "//*[text()={label}]/ancestor::td/following-sibling::td//input",
        "table_select": "//*[text()={label}]/ancestor::td/following-sibling::td//select",
        "table_text_area": "//*[text()={label}]/ancestor::td/following-sibling::td//textarea",
        "table_label": "//div[text()={label}]//ancestor::tr//div//div//div//div",
        "form_section": "//div[@aria-label={label}][@role='group']"
    },
    "claim_center": {
        "input": "//div[text()={label}]//..//div[contains(@class,'ValueWidget gw-editable')]//input",
        "select": "//div[text()={label}]//..//div[contains(@class,'gw-RangeValueWidget')]//select",
        "button": "//div[contains(normalize-space(.),{label})][contains(@class,'button gw-actionable') or (contains("
                  "@class,'gw-action--outer') and contains(@class,'Button'))]",
        "datePicker": "//div[text()={label}]//..//div[contains(@class,'parentForDatePicker')]//input",
        "checkbox": "//*[text()={label}]//parent::div//input[@type='checkbox']",
        "text_area": "//div[text()={label}]//..//div[2]/div[contains(@class,'InputWidget gw-ValueWidget "
                     "gw-editable')]/div/textarea",
        "section_title": "//div[text()={label} and contains(@class,'TitleBar')]",
        "sub_section_title": "//div[contains(@class,'boldLabel')][text()={label})]//ancestor::div[contains(@class,"
                             "'gw-LabelWidget')]",
        "label": "//div[text()={label}]/following-sibling::div//div[contains(@class,'ActionValueWidget') or contains("
                 "@class,'ValueWidget gw-readonly')]",
        "side_menu": "//div[text()={label}]//ancestor::div[contains(@class,'styleTag--MenuLinksWidget "
                     "gw-WestPanelMenuItem')]",
        "sub_menu": "//div[normalize-space(.)={label}]//ancestor::div[contains(@class,'styleTag--MenuItemWidget "
                    "gw-WestPanelMenuItem')]",
        "radio": "//*[text()={label}]//parent::*//input[@type='radio']",
        "tab": "//div[normalize-space(.)={label}]//parent::div[@role='tab']",
        "table": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//following-sibling::div["
                 "contains(@class,'table-wrapper')]//table/tbody",
        "table_add_button": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//div[contains("
                            "normalize-space(.),'Add')][contains(@role,'button')]",
        "table_remove_button": "//div[text()={label}]//ancestor::div[contains(@class,'UI-section')]//div[contains("
                               "normalize-space(.),'Remove')][contains(@role,'button')]",
        "yes_or_no": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'{option}')]/parent::*//input",
        "yes_radio": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'Yes')]/parent::*//input",
        "no_radio": "//*[contains(text(), {label})]/parent::*//span[contains(text(),'No')]/parent::*//input",
        "expand_button": "//div[contains(text(),{label})]//parent::div[contains(@class,'InputColumnWidget')]//div["
                         "contains(@class,'expand-button')]",
        "table_yes_or_no": "//*[contains(text(), {label})]/../../../../following-sibling::td//span[contains(text(),"
                           "'{option}')]/parent::*//input",
        "table_yes_radio": "//div[contains(text(),{label})]//ancestor::tr//td//div//span[contains(text(),"
                           "'Yes')]/parent::*//input",
        "table_no_radio": "//div[contains(text(),{label})]//ancestor::tr//td//div//span[contains(text(),"
                          "'No')]/parent::*//input",
        "table_input": "//*[text()={label}]/ancestor::td/following-sibling::td//input",
        "table_checkbox": "//*[text()={label}]/ancestor::td/following-sibling::td//input",
        "table_select": "//*[text()={label}]/ancestor::td/following-sibling::td//select",
        "table_text_area": "//*[text()={label}]/ancestor::td/following-sibling::td//textarea",
        "table_label": "//div[text()={label}]//ancestor::tr//div//div//div//div",
        "form_section": "//div[@aria-label={label}][@role='group']"
    }
}
