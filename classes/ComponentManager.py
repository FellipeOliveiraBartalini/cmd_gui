from classes.FileManager import FileManager

class ComponentManager:
    path = './src/components/';
    fm = FileManager();

    def createComponent(self, name):
        create_file = self.fm.createFile(self.path, name + '.tsx', 'rcomponent');

    def createCss(self, name):
        create_file = self.fm.createFile(self.path, name + '.module.css');

    def create(self, name, has_css = True):
        create_component_folder = self.fm.createFolder(self.path, name);
        if create_component_folder == False:
            return

        self.path = self.path + name;
        capitalized_name = name[0].upper() + name[1:];

        self.createComponent(capitalized_name);
        if has_css:
            self.createCss(capitalized_name);
        return True;

