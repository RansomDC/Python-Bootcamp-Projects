import page_gen_gui
import page_gen_main
import webbrowser
import os


def generate(self):
    #Get the text input from the form
    var_file = self.inp_filename.get() + ".html"
    var_content = self.inp_content.get()

    #Create/open a file and overwrite the data within with the html.
    app = open(var_file, "w")
    app.write("<html>\n \
        \t<body>\n \
        \t\t<h1>\n \
        \t{}\n \
        \t\t</h1>\n \
        \t</body>\n \
        </html> \
        ".format(var_content))
    app.close()

    #Open the file that was created
    webbrowser.open_new_tab(var_file)












if __name__ == '__main__':
    pass
