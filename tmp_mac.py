import sys
import webbrowser
import os
from project.index_files import main

path = sys.argv[1]


path = os.path.abspath(path)
url = main(path, os.path.abspath(os.path.dirname(__file__)))
webbrowser.open_new_tab("file://" + url) 