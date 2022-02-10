import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from util import config
import selenium
from selenium import webdriver
import time

DEFAULT_BOOKING_COM_URL = "https://www.booking.com/searchresults.html?label=gen173nr-1DCAEoggI46AdIM1gEaKkBiAEBmAExuAEXyAEM2AED6AEB-AECiAIBqAIDuAKn_pGQBsACAdICJDAwMTc1NGNiLWUwY2YtNDBhZi05NjlkLTAzZTU4MTkzZWY5YdgCBOACAQ&sid=ffd7ca868d6d04275c7091b539c7a70b&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.html%3Flabel%3Dgen173nr-1DCAEoggI46AdIM1gEaKkBiAEBmAExuAEXyAEM2AED6AEB-AECiAIBqAIDuAKn_pGQBsACAdICJDAwMTc1NGNiLWUwY2YtNDBhZi05NjlkLTAzZTU4MTkzZWY5YdgCBOACAQ%3Bsid%3Dffd7ca868d6d04275c7091b539c7a70b%3Bsb_price_type%3Dtotal%26%3B&ss={q}&is_ski_area=0&checkin_year={ciy}&checkin_month={cim}&checkin_monthday={cid}&checkout_year={coy}&checkout_month={com}&checkout_monthday={cod}&group_adults={ga}&group_children={gc}&no_rooms={ra}&b_h4u_keep_filters=&from_sf=1&ss_raw={q}&search_pageview_id=ba5214d3914902b1"
CHROME_DRIVER = config()["chrome-driver"]
driver = webdriver.Chrome(CHROME_DRIVER)


def search_booking(query, check_in_year, check_in_month, check_in_day, check_out_year, check_out_month, check_out_day,
                   adult_amount, room_amount, children):
    children_parsed = ""
    children_parsed = children_parsed + str(len(children))
    for child in children:
        children_parsed = children_parsed + "&age=" + str(child)

    # Fill in as much information as booking will allow at this time.
    driver.get(DEFAULT_BOOKING_COM_URL.format(q=query, ciy=check_in_year, cim=check_in_month, cid=check_in_day,
                                              coy=check_out_year, com=check_out_month, cod=check_out_day,
                                              ga=adult_amount, ra=room_amount, gc=children_parsed))

    search_bar = driver.find_elements(By.ID, "ss")[0]  # returns array
    search_bar.send_keys(query)
    search_bar.send_keys(Keys.ENTER)

    print(search_bar)
    time.sleep(60)
    driver.quit()
