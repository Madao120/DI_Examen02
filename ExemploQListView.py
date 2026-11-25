import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

from modeloTabla import ModeloTabla


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Fiesta Principal")

        self.setMinimumSize(800, 200)
        self.setMaximumSize(1200, 1200)

        gridPrincipal = QGridLayout()
        
        self.codigoProduto = QComboBox()


        self.codigoProduto.currentIndexChanged.connect(self.mostrarDatos)

        self.artigo = QLineEdit()
        self.prezoUnitario = QLineEdit()
        self.cantidade = QLineEdit()
        self.ive = QLineEdit()
        self.prezoTotal = QLineEdit()

        gridPrincipal.addWidget(QLabel("Albará"), 0, 0, 1, 1)
        gridPrincipal.addWidget(self.artigo, 1, 0, 1, 2)
        gridPrincipal.addWidget(QLabel("Codigo Produto"), 1, 0, 1, 2)
        gridPrincipal.addWidget(self.codigoProduto, 1, 1, 1, 3)

        gridPrincipal.addWidget(QLabel("Artigo"), 1, 4, 1, 2)
        gridPrincipal.addWidget(self.artigo, 1, 5, 1, 3)

        gridPrincipal.addWidget(QLabel("Prezo Unitario"), 2, 0, 1, 2)
        gridPrincipal.addWidget(self.prezoUnitario, 2, 1, 1, 3)

        gridPrincipal.addWidget(QLabel("Cantidade"), 2, 4, 1, 2)
        gridPrincipal.addWidget(self.cantidade, 2, 5, 1, 3)

        gridPrincipal.addWidget(QLabel("Ive"), 3, 0, 1, 2)
        gridPrincipal.addWidget(self.ive, 3, 1, 1, 7)

        gridPrincipal.addWidget(QLabel("Prezo Total"), 4, 0, 1, 2)
        gridPrincipal.addWidget(self.prezoTotal, 4, 1, 1, 7)

        self.cabeceras = ["Cod producto","Articulo","Cantidade","Prezo Unitario", "Ive", "Prezo Total"]

        self.datos = [["1", "Vespa 150", "1", "10000.0", "2100.0", "12100.0"],
                 ["2", "Seat 600", "2", "20000.0", "4200.0", "24200.0"],
                 ["3", "Citroën 2 CV", "2", "15000.0", "3150.0", "18150.0"]]

        self.modelo = ModeloTabla(self.cabeceras, self.datos)

        self.tvwTaboa = QTableView()
        self.tvwTaboa.setModel(self.modelo)

        gridPrincipal.addWidget(self.tvwTaboa, 5, 0, 6, 7)

        self.btnEngadir = QPushButton("Engadir")
        self.btnEditar = QPushButton("Editar")
        self.btnBorrar = QPushButton("Borrar")

        gridPrincipal.addWidget(self.btnEngadir, 5, 7, 1, 1)
        gridPrincipal.addWidget(self.btnEditar, 6, 7, 1, 1)
        gridPrincipal.addWidget(self.btnBorrar, 7, 7, 1, 1)

        self.btnCancelar = QPushButton("Cancelar")
        self.btnAceptar = QPushButton("Aceptar")
        self.btnAceptar.clicked.connect(self.insertarDatos)

        gridPrincipal.addWidget(self.btnCancelar, 11, 6, 1, 1)
        gridPrincipal.addWidget(self.btnAceptar, 11, 7, 1, 1)

        self.btnCancelar.setEnabled(False)

        contenedor = QWidget()
        contenedor.setLayout(gridPrincipal)
        self.setCentralWidget(contenedor)

        for dato in self.datos:
            self.codigoProduto.addItem((dato[0]))

        ##### Aquí vamos a setear el contenido de la tabla según el select
        self.codigoProduto.setCurrentIndex(0)

        self.artigo.setText(self.datos[self.codigoProduto.currentIndex()][1])
        self.cantidade.setText(self.datos[self.codigoProduto.currentIndex()][2])
        self.prezoUnitario.setText(self.datos[self.codigoProduto.currentIndex()][3])
        self.ive.setText(self.datos[self.codigoProduto.currentIndex()][4])
        self.prezoTotal.setText(self.datos[self.codigoProduto.currentIndex()][5])

        self.show()


    def insertarDatos(self):
        codigo = self.datos[-1][0]

        codigoProducto = int(codigo) + 1

        codigoTexto = str(codigoProducto)

        artigo = self.artigo.text()
        precioUnitario = self.prezoUnitario.text()
        cantidade = self.cantidade.text()
        ive = self.ive.text()
        prezoTotal = self.prezoTotal.text()

        if artigo == "":
            self.artigo.setText("ARTIGO NO VACÍO")
        elif precioUnitario == "":
            self.prezoUnitario.setText("PREZO NO VACÍO")
        elif cantidade == "":
            self.cantidade.setText("CANTIDADE NO VACÍA")
        elif ive == "":
            self.ive.setText("IVE NO VACíA")
        elif prezoTotal == "":
            self.prezoTotal.setText("PREXO NO VACÍO")
        else:
            self.datos.append([codigoTexto,  artigo, precioUnitario, cantidade, ive, prezoTotal])
            self.codigoProduto.addItem(codigoTexto)

            self.artigo.clear()
            self.prezoUnitario.clear()
            self.cantidade.clear()
            self.ive.clear()
            self.prezoTotal.clear()

            self.modelo.layoutChanged.emit()

    def mostrarDatos(self):
        self.artigo.setText(self.datos[self.codigoProduto.currentIndex()][1])
        self.cantidade.setText(self.datos[self.codigoProduto.currentIndex()][2])
        self.prezoUnitario.setText(self.datos[self.codigoProduto.currentIndex()][3])
        self.ive.setText(self.datos[self.codigoProduto.currentIndex()][4])
        self.prezoTotal.setText(self.datos[self.codigoProduto.currentIndex()][5])


if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()