import pychrome
import time


# create a browser instance
browser = pychrome.Browser(url="http://127.0.0.1:9222")

js = "document.getElementsByClassName('qr_code')[0].getElementsByTagName('img')[1].src = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.geuUq3-NpDwcOByuLfsx4AHaD4%26pid%3DApi&f=1&ipt=d7ace9fd689763139dab9a7b643f5ec5c472ca37018052d4c2fdc33eca2eda38&ipo=images'"

# # Do alert 1 on google.com
for tab in browser.list_tab():
    tab.start()
    tab.call_method("Runtime.evaluate", expression=js)
    tab.stop()
