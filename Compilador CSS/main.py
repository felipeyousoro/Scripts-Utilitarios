class CSSCompiler:

    def __init__(self):
        self.classes = []

    def add_class(self, class_name):
        for c in self.classes:
            if c.name == class_name:
                return c

        css_class = self.CSSClass(class_name)
        self.classes.append(css_class)
        return css_class

    def parse_file(self, file):
        for line in file:
            line = line.strip()
            if line.startswith("."):
                class_name = line.split(".", 1)[1].split("{")[0]
                css_class = self.add_class(class_name)

                while True:
                    line = file.readline()
                    line = line.strip()
                    if line == "}":
                        break
                    css_class.add_property(line)

    def write_file(self, file):
        self.classes.sort(key=lambda x: x.name)
        for css_class in self.classes:
            css_class.properties.sort()
            file.write("." + css_class.name + "{\n")
            for property in css_class.properties:
                file.write("\t" + property + "\n")
            file.write("}\n")

    class CSSClass:

        def __init__(self, name):
            self.name = name
            self.properties = []

        def add_property(self, property):
            if property not in self.properties:
                self.properties.append(property)


if __name__ == "__main__":
    arquivo1 = open("arquivo1.css", "r")
    arquivo2 = open("arquivo2.css", "r")

    compilador = CSSCompiler()
    compilador.parse_file(arquivo1)
    compilador.parse_file(arquivo2)
    compilador.write_file(open("arquivo1_compilado.css", "w"))

