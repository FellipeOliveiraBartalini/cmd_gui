from classes.FileManager import FileManager

class ContextManager:
    path = './src/contexts/';
    fm = FileManager();

    def create(self, name):
        capitalized_name = name[0].upper() + name[1:];
        create_file = self.fm.createFile(self.path, name + 'Context.tsx', 'rcontext');

