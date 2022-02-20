import os
from functools import reduce
from project.layout import get_template, create_HTML_tree, rs
import shutil


def tree(path):
    """
    Creates a nested dictionary that represents the folder structure of rootdir
    """
    dir = {}
    rootdir = path.rstrip(os.sep)
    start = rootdir.rfind(os.sep) + 1
    for path, dirs, files in os.walk(rootdir):
        folders = path[start:].split(os.sep)
        subdir = dict.fromkeys(files)
        parent = reduce(dict.get, folders[:-1], dir)
        parent[folders[-1]] = subdir
    return dir


def check_for_folder(tmp_location):
    if not os.path.exists(tmp_location):
        os.mkdir(tmp_location)
    return tmp_location


def main(path, project_folder):
    temp = rs()
    dest = os.path.join(path, "course-viewer")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    temp_folder = os.path.join(project_folder, "tmp")    
    temp_template_folder = os.path.join(temp_folder, temp)
    template = os.path.join(temp_template_folder, "course-viewer.html")

    check_for_folder(temp_folder)
    
    shutil.copytree(os.path.join(project_folder, "template"), temp_template_folder)
    html = get_template(template)
    htmltree = create_HTML_tree(next(iter(tree(path).values())))
    html.select("#sidebar-nav")[0].append(htmltree)
    

    with open(template, "w+", encoding='utf-8') as file:
        file.write(html.prettify())
    
    shutil.copytree(temp_template_folder, dest)
    shutil.rmtree(temp_template_folder)
    return os.path.join(dest, "course-viewer.html")
    
