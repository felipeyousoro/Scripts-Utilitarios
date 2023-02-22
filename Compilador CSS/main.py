import os


class CSSCompiler:

    def __init__(self):
        self.classes = []

    def addClass(self, class_name):
        for c in self.classes:
            if c.name == class_name:
                return c

        css_class = self.CSSClass(class_name)
        self.classes.append(css_class)
        return css_class

    def parse_file(self, file):
        for line in file:
            line = line.strip()
            # get anything before {
            if "{" in line:
                class_name = line.split("{")[0].strip()
                css_class = self.addClass(class_name)
                while True:
                    line = file.readline()
                    line = line.strip()
                    if line == "}":
                        break
                    css_class.addProperty(line)

    def writeFile(self, file):
        self.classes.sort(key=lambda x: x.name)
        for css_class in self.classes:
            css_class.properties.sort()
            file.write(css_class.name + "{\n")
            for property in css_class.properties:
                file.write("\t" + property + "\n")
            file.write("}\n")
    class CSSClass:

        def __init__(self, name):
            self.name = name
            self.properties = []

        def addProperty(self, property):
            if property not in self.properties:
                self.properties.append(property)


def findCSSFiles(path):
    css_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".css"):
                css_files.append(os.path.join(root, file))
    return css_files


if __name__ == "__main__":
    folder_path = "C:/Users/Yousoro/Desktop/Projeto-FA/Projeto/public/css"
    css_files = findCSSFiles(folder_path)
    for file in css_files:
        if file.endswith("app.css"):
            css_files.pop(css_files.index(file))
            break

    compiler = CSSCompiler()
    for file in css_files:
        with open(file, "r") as f:
            compiler.parse_file(f)

    compiler.writeFile(open("arquivo_compilado.css", "w"))
