import converter
import sys
import textwrap

def main():
    ficheiro = input("Introduza o nome do ficheiro a converter -> ")
    ficheiro = "../" + ficheiro
    print("\n") 
    
    sys.stdin = open(ficheiro, 'r')
    md = sys.stdin.read()
    convertido = converter.converterAll(md)
    
    sys.stdin = sys.__stdin__
    
    html = """
<!DOCTYPE html>
<html>
<head>
    <title>Markdown</title>
    <meta charset="UTF-8">
</head>
<body>
"""
    convertido_indentado = textwrap.indent(convertido, '    ')
    html += convertido_indentado
    html += """
</body>
</html>
"""
    
    print(html)
    return convertido
    
    
if __name__ == "__main__":
    main()