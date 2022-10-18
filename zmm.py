class Token:
    def __init__(self,type_,value=None) -> None:
        self.type = type_
        self.value = value
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return self.type
class Lexer:
    def __init__(self,line) -> None:
        self.text = line
        self.pos = -1
        self.current_char = None
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
                if self.current_char == "(":
                    openp = 1
                    txt = ""
                    while openp > 0:
                        self.advance()
                        if self.current_char == "(":
                            openp += 1
                        elif self.current_char == ")":
                            openp -= 1
                        else:
                            txt += self.current_char
                    tokens.append(Token("runFunc",(item,txt)))
                    self.advance()
                else:
                    tokens.append(Token("IDENTIFYER",item))
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
                tokens.append(Token("PLUS"))
                self.advance()
            elif self.current_char == "-":
                tokens.append(Token("MINUS"))
                self.advance()
            elif self.current_char == "*":
                tokens.append(Token("MULT"))
                self.advance()
            elif self.current_char == "/":
                tokens.append(Token("DIV"))
                self.advance()
            elif self.current_char == "(":
                tokens.append(Token("LPAREN"))
                self.advance()
            elif self.current_char == ")":
                tokens.append(Token("RPAREN"))
                self.advance()

        return tokens

class Interpreter:
    def __init__(self) -> None:
        pass
    def run(self,txt):
        lexer = Lexer(txt)
        print(lexer.make_tokens())