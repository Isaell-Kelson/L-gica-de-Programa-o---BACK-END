class Editor:
    def __init__(self, nome):
        self.nome = nome



class TextEditor:
    
    def __init__(self):
        self.editores = []  # <<== 
    
    def adic_editor(self, editor):
        
        self.editores.append(editor)

    def enviar_msg(self, mensagem):
        for editor in self.editores:
            
            print( f'|{editor.nome} recebeu | {mensagem}' )


observ = Editor('TextEditor')


edito = TextEditor()
edito.adic_editor(observ)


edito.enviar_msg('Texto editado')