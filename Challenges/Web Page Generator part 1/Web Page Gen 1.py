import webbrowser
import os

app = open('page.html', "w")
app.write("<html>\n \
        \t<body>\n \
        \t\t<h1>\n \
        \tStay tuned for our amazing summer sale!\n \
        \t\t</h1>\n \
        \t</body>\n \
        </html> \
        ")
app.close()
        
webbrowser.open_new_tab('page.html')
