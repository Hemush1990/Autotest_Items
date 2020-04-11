import time

def test_test_item_add_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    #time.sleep(30) (необходимо активировать при проверке)
    button = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert button, "Нет данной кнопки"
