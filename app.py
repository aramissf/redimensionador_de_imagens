import sys
from aplicativo.design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import  QPixmap

class Redimensiona(QMainWindow, Ui_MainWindow):
    #Inicializando o contrutor
    def __init__(self, parent=None):
        #apontando o init da classe mae1
        super().__init__(parent)
        #apontando o init da classe mae2
        super().setupUi(self)

        #Atribuindo ao botão a função abrir imagem
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)

        #Atribuindo ao botão a função redimensionar
        self.btnRedimensionar.clicked.connect(self.redimensionar)


        # Atribuindo ao botão a função salvar
        self.btnSalvar.clicked.connect(self.salvar)

    # Criando um metodo para atribuir função ao botão abrir imagem
    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem',
            r'C:\Users\Public\Pictures',
           # options = QFileDialog.DontUseNativeDialog
        )

        #Atribuindo ao LineEdit o valor "Endereço da imagem"
        self.inputAbrirArquivo.setText(imagem)

        #Atribuindo ao Qpixmap o parametro imagem
        self.original_img = QPixmap(imagem)

        #Atribuindo ao Label a variavel que recebeu  o QPixmap
        self.labelImg.setPixmap(self.original_img)

        #Atribuindo ao LineEdit o valor "Largura da imagem"
        self.inputLargura.setText(str(self.original_img.width()))

        #Atribuindo ao LineEdit o valor "Altura da imagem"
        self.inputAltura.setText(str(self.original_img.height()))

    #Criando um metodo para atribuir função ao botão redimensionar
    def redimensionar(self, redimensionou = False):

        #Criando uma variaver para capturar a largura inserida na editline
        largura = int(self.inputLargura.text())

        #Criando uma nova imagem usando a variavel acima
        self.nova_imagem = self.original_img.scaledToWidth(largura)

        #Atribuindo ao pixmax a nova imagem
        self.labelImg.setPixmap(self.nova_imagem)

        #Atribuindo ao LineEdit a nova largura
        self.inputLargura.setText(str(self.nova_imagem.width()))

        #Atribuindo ao LineEdit a nova altura
        self.inputAltura.setText(str(self.nova_imagem.height()))

        redimensionou = True

    #Criando um medoto para atribuir função ao botão de salvar
    def salvar(self):

            imagem, _ = QFileDialog.getSaveFileName(

                self.centralwidget,
                'Salvar Imagem'
                 r'C:\Users\Public\Pictures'

            )
            self.nova_imagem.save(imagem, 'PNG')

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    redimensiona = Redimensiona()
    redimensiona.show()
    qt.exec()



