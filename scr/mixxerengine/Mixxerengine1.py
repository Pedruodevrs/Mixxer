class MixxerEngine:
    def __init__(self):
        self.mode = "OBJECT"
        
    def apply_transform(self, object, type):
        if type == "EXTRUDE":

            new_face = object.selected_face.copy()
            new_face.translate(z=1.0)
            print("Mixxer: Face expelida com sucesso!")

    def render_view(self):

        pass
      
