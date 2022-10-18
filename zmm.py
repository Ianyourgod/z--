class Error:
    def __init__(self,name,info) -> None:
        self.name = name
        self.info = info
    def __repr__(self) -> str:
        if self.info: return f'{self.name}: {self.info}'
        return f'{self.name} error'

class Token:
    def __init__(self,type_,value=None) -> None:
        self.type = type_
        self.value = value
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return self.type
class Lexer:
    def __init__(self,line,ln) -> None:
        self.text = line
        self.pos = -1
        self.current_char = None
        self.ln = ln
        self.advance()
    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None
    def make_tokens(self):
        tokens = []
        CHARS = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        NUMBS = "1234567890"

        while self.current_char != None:
            if self.current_char in " \t":
                self.advance()
            elif self.current_char in CHARS:
                item = ""
                while self.current_char in CHARS:
                    item += self.current_char
                    self.advance()
                    if not self.current_char:
                        break
                if self.current_char == "(":
                    openp = 1
                    txt = ""
                    while openp > 0:
                        self.advance()
                        if self.current_char == "(":
                            openp += 1
                        elif self.current_char == ")":
                            openp -= 1
                        elif not self.current_char:
                            return Error("Unfinished Parenthasies Error",f"did not close parenthasies on character {self.pos} in line {self.ln}")
                        else:
                            txt += self.current_char
                    tokens.append(Token("RUNFUNC",(item,txt)))
                    self.advance()
                else:
                    tokens.append(Token("IDENTIFIER",item))
                    self.advance()
            elif self.current_char in NUMBS:
                n = ""
                dm = 0
                while self.current_char in NUMBS + ".":
                    if self.current_char == ".":
                        dm += 1
                        if dm > 1:
                            break
                    n += self.current_char
                    self.advance()
                    if self.pos >= len(self.text):
                        break
                tokens.append(Token("NUMB",n))
            elif self.current_char == "+":
                if self.current_char == "=":
                    tokens.append(Token("ADDTO"))
                else:tokens.append(Token("PLUS"))
                self.advance()
            elif self.current_char == "-":
                if self.current_char == "=":
                    tokens.append(Token("MINTO"))
                else:tokens.append(Token("MINUS"))
                self.advance()
            elif self.current_char == "*":
                if self.current_char == "=":
                    tokens.append(Token("MULTO"))
                tokens.append(Token("MULT"))
                self.advance()
            elif self.current_char == "/":
                if self.current_char == "=":
                    tokens.append(Token("DIVTO"))
                tokens.append(Token("DIV"))
                self.advance()
            elif self.current_char == "(":
                tokens.append(Token("LPAREN"))
                self.advance()
            elif self.current_char == ")":
                tokens.append(Token("RPAREN"))
                self.advance()
            elif self.current_char == "=":
                self.advance()
                if self.current_char == "=":
                    tokens.append(Token("ISEQU"))
                else:
                    tokens.append(Token("SETVAR"))

        return tokens
    
class Parser:
    def __init__(self,tokens) -> None:
        self.tokens = tokens
    def parse(self):
        tree = []
        for i in self.tokens:
            if i.type == "RUNFUNC":
                pass
            elif i.type == "IDENTIFIER":
                pass
            elif i.type == "NUMB":
                pass
            elif i.type == "ADDTO":
                pass
            elif i.type == "PLUS":
                pass
            elif i.type == "MINTO":
                pass
            elif i.type == "MINUS":
                pass
            elif i.type == "MULTO":
                pass
            elif i.type == "MULT":
                pass
            elif i.type == "DIVTO":
                pass
            elif i.type == "DIV":
                pass
            elif i.type == "LPAREN":
                pass
            elif i.type == "RPAREN":
                pass
            elif i.type == "ISEQ":
                pass
            elif i.type == "SETVAR":
                pass
        
        return tree
class Interpreter:
    def __init__(self) -> None:
        pass
    def run(self,txt,line):
        lexer = Lexer(txt,line)
        print(lexer.make_tokens())