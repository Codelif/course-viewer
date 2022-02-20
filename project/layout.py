from bs4 import BeautifulSoup
import bs4
import string
import random

includedType = ['.mp4', '.pdf', '.html', '.txt']


def rs(limit:int=20) -> str:
    return (''.join([random.choice(string.ascii_letters) for i in range(limit)]))


def create_file_tag(title, path, ext):
    soup = BeautifulSoup("", "html5lib")

    file_text = soup.new_tag(
        'p',
        **{
            'style': "margin-top: 0; margin-bottom: 0;"
        }
    )
    file_text.string = title
    type_icon = soup.new_tag(
        'i',
        **{
            'class': "bi bi-filetype-" + ext[1:]
        }
    )
    file_tag = soup.new_tag(
        'a',
        **{
            'href': '#',
            'class': 'list-group-item list-group-item-action',
            'path': path,
            'title': title,
            'type': 'video' if '.mp4' == ext else 'file',
            'onclick': "changeScene(this);"
        }
    )

    file_tag.append(
        file_text
    )
    file_tag.append(
        type_icon
    )

    return file_tag


def create_folder_tag(title, collapse_id, parent_id , button_id):
    soup = BeautifulSoup("", "html5lib")

    accordion_container_tag = soup.new_tag(
        "div", 
        **{
            'class':"accordion-item", 
            'id': rs(50)
        }
    )

    button_container_tag = soup.new_tag(
        "h2", 
        **{
            'class': 'accordion-header', 
            'id': button_id
        }
    )

    button_tag = soup.new_tag(
        'button',
        **{
            'class': 'accordion-button',
            'data-bs-toggle': 'collapse',
            'data-bs-target': f'#{collapse_id}',
            'aria-expanded': 'true',
            'aria-controls': collapse_id,
        }
    )
    button_tag.string = title    
       
    collapse_container_tag = soup.new_tag(
        'div',
        **{
            'class': 'accordion-collapse collapse',
            'id': collapse_id,
            'aria-labelledby': button_id,
            'data-bs-parent': f'#{parent_id}',
        }
    )

    collapse_tag = soup.new_tag(
        'div',
        **{
            'class': 'accordion-body'
        }
    )
    
    ##Appends to parent tags
    button_container_tag.append(
        button_tag
    )
    collapse_container_tag.append(
        collapse_tag
    )
    accordion_container_tag.append(
        button_container_tag
    )
    accordion_container_tag.append(
        collapse_container_tag
    )

    return accordion_container_tag


def get_template(template_loc):
    with open(template_loc) as html_doc:
        return BeautifulSoup(html_doc.read(), "html5lib")


## PLEASE DON'T ASK ME HOW THIS WORKS! IT JUST DOES! IT'S A MIRACLE I CODED THIS WITHOUT STACKOVERFLOW.
def create_HTML_tree(tree:dict):
    folderTag = bs4.element.Tag(name="div")
    folderTag["class"] = "accordion"
    parent_id = rs(50)
    folderTag["id"] = parent_id

    for i in sorted(tree.keys()):
        if tree[i]:
            folder = create_folder_tag(i, rs(50), parent_id, rs(50))
            folder.select('.accordion-body')[0].append(create_HTML_tree(tree[i]))
            folderTag.append(folder)
        else:
            for ext in includedType:
                index = -1*len(ext)
                if ext == i[index:]:
                    folderTag.append(create_file_tag(i[:index].replace("_", " "), i, ext))
    return folderTag

