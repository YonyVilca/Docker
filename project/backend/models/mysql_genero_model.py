from backend.models.mysql_connection_pool import MySQLPool

class GeneroModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def crear_genero(self, nombre_genero):
        data = {'nombre_genero': nombre_genero}
        query = "INSERT INTO generos (nombre_genero) VALUES (%(nombre_genero)s)"
        try:
            self.mysql_pool.execute(query, data, commit=True)
            return {"result": "Género creado exitosamente"}
        except Exception as e:
            print(f"Error al crear género: {e}")
            return {"result": "Error al crear género"}

    def obtener_generos(self):
        query = "SELECT * FROM generos"
        try:
            rv = self.mysql_pool.execute(query)
            return [{"genero_id": result[0], "nombre_genero": result[1]} for result in rv]
        except Exception as e:
            print(f"Error al obtener géneros: {e}")
            return []

    def obtener_genero(self, genero_id):
        params = {'genero_id': genero_id}
        query = "SELECT * FROM generos WHERE genero_id = %(genero_id)s"
        try:
            rv = self.mysql_pool.execute(query, params)
            return {"genero_id": rv[0][0], "nombre_genero": rv[0][1]} if rv else None
        except Exception as e:
            print(f"Error al obtener género: {e}")
            return None

    def actualizar_genero(self, genero_id, nuevo_nombre):
        data = {'genero_id': genero_id, 'nuevo_nombre': nuevo_nombre}
        query = "UPDATE generos SET nombre_genero = %(nuevo_nombre)s WHERE genero_id = %(genero_id)s"
        try:
            self.mysql_pool.execute(query, data, commit=True)
            return {"result": "Género actualizado exitosamente"}
        except Exception as e:
            print(f"Error al actualizar género: {e}")
            return {"result": "Error al actualizar género"}

    def eliminar_genero(self, genero_id):
        params = {'genero_id': genero_id}
        query = "DELETE FROM generos WHERE genero_id = %(genero_id)s"
        try:
            self.mysql_pool.execute(query, params, commit=True)
            return {"result": "Género eliminado exitosamente"}
        except Exception as e:
            print(f"Error al eliminar género: {e}")
            return {"result": "Error al eliminar género"}

if __name__ == "__main__":
    genero_model = GeneroModel()
    print(genero_model.crear_genero('Ficción'))
    print(genero_model.actualizar_genero(1, 'Ficción Actualizada'))
    print(genero_model.obtener_generos())
    print(genero_model.eliminar_genero(1))