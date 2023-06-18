from functions import Functions
import time

d = Functions()

d.open_page("https://www.depop.com/latinathrifts/")

cookies_path = "/html/body/div/div/div[2]/div[2]/button[2]"
loadmore_path = "html/body/div/div/main/div[2]/div/div/button"
shirt_path_start = "/html/body/div/div/main/div[2]/div/ul/li"
shirt_path_end = "/div/a"


if d.check_exists_by_xpath(cookies_path):
    d.click_button(cookies_path)

for i in range(1,3):
    shirt_path = shirt_path_start + "[" + str(i) + "]" + shirt_path_end
    d.press_product(shirt_path)
    d.back()
#d.click_button(shirt_path)
#time.sleep(2)
#d.back()

'''
# If you want to load the entire page
while d.check_exists_by_xpath(loadmore_path):
    d.load_more(loadmore_path)
'''



