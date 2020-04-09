class CGXFormatter:
    def __init__(self):
        self.BASE_INDENT = 4
        self.inside_string = False
        self.total_indent = 0
        self.new_line = True

    def read_lines(self):
        self.nb_lines = int(input())
        for _ in range(self.nb_lines):
            line = input()
            for char in line:
                self.read_char(char)

    def read_char(self, char):
        if self.inside_string:
            if char == '\'':
                self.inside_string = False
            self.print_char(char)
        else:
            self.read_char_outside_string(char)

    def read_char_outside_string(self, char):
        if char == ' ' or char == '\t':
            return
        if char == '\'':
            self.inside_string = True
            self.print_char(char)
        elif char == '(':
            if not self.new_line:
                self.print_new_line()
            self.print_char(char)
            self.print_new_line()
            self.total_indent += self.BASE_INDENT
        elif char == ')':
            self.total_indent -= self.BASE_INDENT
            if not self.new_line:
                self.print_new_line()
            self.print_char(char)
        elif char == ';':
            self.print_char(char)
            self.print_new_line()
        else:
            self.print_char(char)

    def print_char(self, char):
        if self.new_line:
            for _ in range(self.total_indent):
                print(' ', end='')
            self.new_line = False
        print(char, end='')

    def print_new_line(self):
        print()
        self.new_line = True


if __name__ == "__main__":
    formatter = CGXFormatter()
    formatter.read_lines()
