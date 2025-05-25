class Language():
#_________________CORREGIR TERCERA LINEA_________#
    def __init__(self, id, name)->None:
        self.id=id
        self.name=name

    def to_json(self):
        return{
            'id': self.id,
            'name': self.name
        }