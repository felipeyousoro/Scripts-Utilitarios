import re
import os
import shutil

SETTINGS_FILE_PATH = "config.txt"

class DirectoryOrganizer:
    def __init__(self, path_settings):
        self.dir_from = ""
        self.dir_to =   ""
        self.file_extensions = []
        self.moved_files = []

        with open(path_settings, "r") as file_settings:
            input = file_settings.read()

            self.dir_from = re.search("-dir_from[ ]*:[ ]*[^\n]*", input).group()
            self.dir_from = re.search("[\"][^\n]*[\"]", self.dir_from).group().strip("\"")

            self.dir_to = re.search("-dir_to[ ]*:[ ]*[^\n]*", input).group()
            self.dir_to = re.search("[\"][^\n]*[\"]", self.dir_to).group().strip("\"")

            extensions_list = re.search("-file_extensions[ ]*:[ ]*[^\]]*]", input).group()
            extensions_list = re.findall("[\"][^\"]*[\"]", extensions_list)
            for ext in extensions_list:
                self.file_extensions.append(ext.strip("\""))
           
    def move(self):
        unprocessed_files = os.listdir(self.dir_from)
        
        moving_files = []
        for f in unprocessed_files:
            for ext in self.file_extensions:
                if(f.endswith(ext)):
                    moving_files.append(f)
                    break

        for f in moving_files:
            destiny_file_name = f
            duplicate = 1
            while os.path.exists(f"{self.dir_to}/{destiny_file_name}"):
                destiny_file_name = f"{duplicate}_{f}"
                duplicate += 1

            shutil.move(f"{self.dir_from}/{f}", f"{self.dir_to}/{destiny_file_name}")
            self.moved_files.append(f)
        
if __name__ == "__main__":

    organizer = DirectoryOrganizer(SETTINGS_FILE_PATH)
    organizer.move()

    report = open("report.txt", "w")

    report.write(f"File origin: {organizer.dir_from}\n")
    report.write(f"File destiny: {organizer.dir_to}\n")
    report.write(f"File extensions: {organizer.file_extensions}\n")
    report.write(f"Total files moved: {len(organizer.moved_files)}\n")

    report.write(f"\nFiles moved:\n")
    for f in organizer.moved_files:
        report.write(f"\tFile moved:\t\t{f}\n")