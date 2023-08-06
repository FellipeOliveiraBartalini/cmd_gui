import os;

class FileManager():
    def createFile(self, path: str, name: str, content: str = ''):
        try:
            with open(os.path.join(path, name), 'w') as file:
                if len(content) > 0:
                    file.write(content);
                file.close();
            print("File created with success!");
        except FileNotFoundError:
            print("The directory does not exists");

    def createFolder(self, path: str, name: str):
        try:
            os.mkdir(os.path.join(path, name));
        except:
            print("There was an error creating the directory: " + path + name);
            return False;

