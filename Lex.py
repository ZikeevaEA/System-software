
# coding: utf-8

# # Лексер 

# In[6]:


import sys
import re

def lex(characters, token_exprs):
    pos = 0
    tokens = []
    while pos < len(characters):
        match = None
        for token_expr in token_exprs:
            pattern, tag = token_expr
            regex = re.compile(pattern) #Собирает регулярное выражение в отдельный объект, который может быть использован для поиска
            match = regex.match(characters, pos) #Этот метод ищет по заданному шаблону в начале строки.
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag)
                    tokens.append(token)
                break
        if not match:
            sys.stderr.write('Illegal character: %s\n' % characters[pos])
            sys.exit(1)
        else:
            pos = match.end(0)
    return tokens


# In[7]:


VAR = 'VAR'
DIGIT = 'DIGIT'
OP = 'OP'
ASS_OP = 'ASS_OP'


# In[8]:


token_exprs = [
    (r'\+|-|/|\*',  OP),
    (r'=',  ASS_OP),
    (r'[0-9]+', DIGIT),
    (r'[a-z]+',  VAR)]


# In[9]:


def imp_lex(characters):
    return lex(characters, token_exprs)


# In[12]:


file = open('hello.imp')
characters = file.read()
file.close()
tokens = imp_lex(characters)
for token in tokens:
    print (token)

