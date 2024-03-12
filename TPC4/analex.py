import ply.lex as lex

reserved = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
}

tokens = [
   'ID',
   'OP',
   'INT',
   'VIRGULA'
] + list(reserved.values())


t_OP = r'==|<=|>=|!=|>|<|='
t_VIRGULA = r','

def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value.lower(), 'ID')
    return t
    

def t_INT(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()

data = 'Select id, nome, salario From empregados Where salario >= 820'

lexer.input(data)

for token in lexer:
    print(token)