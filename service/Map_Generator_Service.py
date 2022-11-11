from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import FileLoader

class Map_Generator_Service:
    def __init__(self, json_data):
        self.json_data = json_data
        self.template_path = './repository/templates'
        self.template_name = 'mapping_template.txt'
        self.template = None
        self.variables_to_render = {
            "json" : str(self.json_data)
        }

    def load_template(self):
            """
            Loads the template to create TDs
            """
            searchpath = [self.template_path] # search path
            engine = Engine(
                loader=FileLoader(searchpath),
                extensions=[CoreExtension()]
            ) # generate engine
            self.template = engine.get_template(self.template_name) # load template

    def render_template(self):
        """
        Render the template
        """
        self.load_template()
        return self.template.render(self.variables_to_render)