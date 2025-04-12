from backend.models.mysql_connection_pool import MySQLPool

class AutorModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def crear_autor(self, nombre_autor):
        data = {'nombre_autor': nombre_autor}
        query = "INSERT INTO autores (nombre_autor) VALUES (%(nombre_autor)s)"
        try:
            self.mysql_pool.execute(query, data, commit=True)
            return {"result": "Autor creado exitosamente"}
        except Exception as e:
            print(f"Error al crear autor: {e}")
            return {"result": "Error al crear autor"}

    def obtener_autores(self):
        query = "SELECT * FROM autores"
        try:
            rv = self.mysql_pool.execute(query)
            return [{"autor_id": result[0], "nombre_autor": result[1]} for result in rv]
        except Exception as e:
            print(f"Error al obtener autores: {e}")
            return []

    def obtener_autor(self, autor_id):
        params = {'autor_id': autor_id}
        query = "SELECT * FROM autores WHERE autor_id = %(autor_id)s"
        try:
            rv = self.mysql_pool.execute(query, params)
            return {"autor_id": rv[0][0], "nombre_autor": rv[0][1]} if rv else None
        except Exception as e:
            print(f"Error al obtener autor: {e}")
            return None

    def actualizar_autor(self, autor_id, nuevo_nombre):
        data = {'autor_id': autor_id, 'nuevo_nombre': nuevo_nombre}
        query = "UPDATE autores SET nombre_autor = %(nuevo_nombre)s WHERE autor_id = %(autor_id)s"
        try:
            self.mysql_pool.execute(query, data, commit=True)
            return {"result": "Autor actualizado exitosamente"}
        except Exception as e:
            print(f"Error al actualizar autor: {e}")
            return {"result": "Error al actualizar autor"}

    def eliminar_autor(self, autor_id):
        params = {'autor_id': autor_id}
        query = "DELETE FROM autores WHERE autor_id = %(autor_id)s"
        try:
            self.mysql_pool.execute(query, params, commit=True)
            return {"result": "Autor eliminado exitosamente"}
        except Exception as e:
            print(f"Error al eliminar autor: {e}")
            return {"result": "Error al eliminar autor"}

if __name__ == "__main__":
    autor_model = AutorModel()
    print(autor_model.crear_autor('Nuevo Autor'))
    print(autor_model.obtener_autores())
    print(autor_model.actualizar_autor(1, 'Autor Actualizado'))
    print(autor_model.obtener_autor(1))
    print(autor_model.eliminar_autor(1))