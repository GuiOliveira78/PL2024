import re

# Função que converte um título de md para html
def convert_title(text):
    return re.sub(r'(^#+)\s*(.*)', lambda t: f'<h{len(t[1])}>{t[2]}</h{len(t[1])}>', text, flags=re.MULTILINE)

# Função que converte um espaço em bold de md para html
def convert_bold(text):
    return re.sub(r'^\*\*(.*)\*\*', r'<b>\1</b>', text, flags=re.MULTILINE)

# Função que converte um espaço em itálico de md para html
def convert_italico(text):
    return re.sub(r'^\*(.*)\*', r'<i>\1</i>', text, flags=re.MULTILINE)

# Função que converte um blockquote de md para html
def convert_blockquote(text):
    return re.sub(r'^> (.*)', r'<blockquote>\1</blockquote>', text, flags=re.MULTILINE)

# Função que converte uma ordered list de md para html
def convert_oList(text):
    lista_ul = re.findall(r'^\d\. .*', text, flags=re.MULTILINE)
    lista_ul[0] = '<ol>\n' + lista_ul[0]
    lista_ul[-1] = lista_ul[-1] + '\n</ol>'
    for elem in lista_ul:
        elem = re.sub(r'^\d\. (.+)$', r'    <li>\1</li>', elem, flags=re.MULTILINE)
        text = re.sub(r'^\d\. .*$', elem, text, count=1, flags=re.MULTILINE)
    return text

# Função que converte uma unordered list de md para html
def convert_uList(text):
    lista_ul = re.findall(r'^- .*', text, flags=re.MULTILINE)
    lista_ul[0] = '<ul>\n' + lista_ul[0]
    lista_ul[-1] = lista_ul[-1] + '\n</ul>'
    for elem in lista_ul:
        elem = re.sub(r'^- (.+)$', r'   <li>\1</li>', elem, flags=re.MULTILINE)
        text = re.sub(r'^- .*$', elem, text, count=1, flags=re.MULTILINE)
    return text

# Função que converte um link de md para html
def convert_link(text):
    return re.sub(r'^\[(.*)\]\((.*)\)', r'<a href="\2">\1</a>', text, flags=re.MULTILINE)

# Função que converte uma imagem de md para html
def convert_img(text):
    return re.sub(r'^!\[(.*)\]\((.*)\)', r'<img src="\2" alt="\1"/>', text, flags=re.MULTILINE)

# Função que converte paragrafos de md para html
def convert_paragraph(text):
    return re.sub(r'^(\w.*)', r'<p>\1</p>', text, flags=re.MULTILINE)

# Função que concatena todas as funções acima de
# forma a podermos utilizar tudo de forma mais fácil
def converterAll(text):
    newText = text
    newText = convert_title(newText)
    newText = convert_bold(newText)
    newText = convert_italico(newText)
    newText = convert_blockquote(newText)
    newText = convert_oList(newText)
    newText = convert_uList(newText)
    newText = convert_link(newText)
    newText = convert_img(newText)
    newText = convert_paragraph(newText)
    return newText
