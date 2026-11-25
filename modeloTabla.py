from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtCore import QAbstractTableModel, Qt
from PyQt6.QtGui import QColor


class ModeloTabla(QAbstractTableModel):

    # Inicializa el modelo y guarda los encabezados y los datos.
    def __init__(self, cabeceras, datos):
        super().__init__()

        self.cabeceras = cabeceras
        self.datos = datos

    # Devuelve el número de filas que tiene la tabla.
    def rowCount(self, indice):
        return len(self.datos)

    # Devuelve el número de columnas que tiene la tabla.
    def columnCount(self, indice):
        return len(self.cabeceras)

    # Devuelve el contenido, el estado del checkbox y el color de cada celda.
    def data(self, indice, rol):

        if not indice.isValid():
            return None

        fila = indice.row()
        columna = indice.column()

        dato = self.datos[fila][columna]

        # Devuelve el color de fondo de toda la fila.
        if rol == Qt.ItemDataRole.BackgroundRole:

            # Es resto de 2 ya que en cuanto a indices son los pares ya que empieza en 0, pero en cuanto a vista son los impares
            if indice.column() % 2 != 0:
                return QColor("lightgray")

            return QColor("white")

        # Muestra el contenido como texto, excepto en la columna checkbox.
        if rol == Qt.ItemDataRole.DisplayRole:
                return dato

        return None

    # Guarda los cambios realizados al editar texto o marcar un checkbox.
    def setData(self, indice, valor, rol):

        if not indice.isValid():
            return False

        fila = indice.row()
        columna = indice.column()

        # Guarda el texto nuevo en la primera columna.
        if rol == Qt.ItemDataRole.EditRole:

            if columna == 0:
                self.datos[fila][columna] = valor

                self.dataChanged.emit(indice, indice)

                return True

        # Guarda el nuevo estado de la tabla
        if rol == Qt.ItemDataRole.CheckStateRole:

                # Notifica a Qt que ha cambiado toda la fila.
                primera_celda = self.index(fila, 0)
                ultima_celda = self.index(fila, self.columnCount(indice) - 1)

                self.dataChanged.emit(
                    primera_celda,
                    ultima_celda,
                    [
                        Qt.ItemDataRole.CheckStateRole,
                        Qt.ItemDataRole.BackgroundRole
                    ]
                )

                return True

        return False

    # Define qué acciones están permitidas en cada celda.
    def flags(self, indice):

        if not indice.isValid():
            return Qt.ItemFlag.NoItemFlags

        # Todas las celdas se pueden activar y seleccionar.
        condiciones = (
                Qt.ItemFlag.ItemIsEnabled |
                Qt.ItemFlag.ItemIsSelectable
        )
        return condiciones

    # Devuelve el texto de los encabezados de las columnas.
    def headerData(self, seccion, orientacion, rol):

        if rol == Qt.ItemDataRole.DisplayRole:
            if orientacion == Qt.Orientation.Horizontal:
                return self.cabeceras[seccion]

        if rol == Qt.ItemDataRole.BackgroundRole:
            # Color de fondo de la cabecera
            return QColor("lightgray")

        return None