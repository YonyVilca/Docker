from backend.models.mysql_connection_pool import MySQLPool

class LibroModel:
    def __init__(self):
        self.mysql_pool = MySQLPool()

    def crear_libro(self, titulo_libro, genero_id, autor_ids):
        # Validar existencia del género
        genero_check = self.mysql_pool.execute(
            "SELECT COUNT(*) FROM generos WHERE genero_id = %s", (genero_id,))
        if genero_check[0][0] == 0:
            return {"error": "Género no existe"}

        # Validar existencia de todos los autores
        for autor_id in autor_ids:
            autor_check = self.mysql_pool.execute(
                "SELECT COUNT(*) FROM autores WHERE autor_id = %s", (autor_id,))
            if autor_check[0][0] == 0:
                return {"error": f"El autor con ID {autor_id} no existe"}

        data = {'titulo_libro': titulo_libro, 'genero_id': genero_id}
        query = "INSERT INTO libros (titulo_libro, genero_id) VALUES (%(titulo_libro)s, %(genero_id)s)"
        try:
            lastrowid = self.mysql_pool.execute(query, data, commit=True)
            for autor_id in autor_ids:
                self.agregar_autor_a_libro(lastrowid, autor_id)
            return {"result": "Libro creado exitosamente", "libro_id": lastrowid}
        except Exception as e:
            print(f"Error al crear libro: {e}")
            return {"result": "Error al crear libro"}

    def agregar_autor_a_libro(self, libro_id, autor_id):
        data = {'libro_id': libro_id, 'autor_id': autor_id}
        query = "INSERT INTO libro_autores (libro_id, autor_id) VALUES (%(libro_id)s, %(autor_id)s)"
        self.mysql_pool.execute(query, data, commit=True)

    def obtener_libros(self):
        query = """
            SELECT L.libro_id, L.titulo_libro, G.nombre_genero 
            FROM libros L 
            INNER JOIN generos G ON L.genero_id = G.genero_id 
            WHERE L.eliminado = FALSE
        """
        try:
            rv = self.mysql_pool.execute(query)
            return [{"libro_id": r[0], "titulo_libro": r[1], "nombre_genero": r[2]} for r in rv]
        except Exception as e:
            print(f"Error al obtener libros: {e}")
            return []

    def obtener_libro(self, libro_id):
        params = {'libro_id': libro_id}
        query = "SELECT * FROM libros WHERE libro_id = %(libro_id)s AND eliminado = FALSE"
        try:
            rv = self.mysql_pool.execute(query, params)
            return {"libro_id": rv[0][0], "titulo_libro": rv[0][1], "genero_id": rv[0][2]} if rv else None
        except Exception as e:
            print(f"Error al obtener libro: {e}")
            return None

    def actualizar_libro(self, libro_id, nuevo_titulo, nuevo_genero_id):
        data = {'libro_id': libro_id, 'nuevo_titulo': nuevo_titulo, 'nuevo_genero_id': nuevo_genero_id}
        query = "UPDATE libros SET titulo_libro = %(nuevo_titulo)s, genero_id = %(nuevo_genero_id)s WHERE libro_id = %(libro_id)s"
        try:
            self.mysql_pool.execute(query, data, commit=True)
            return {"result": "Libro actualizado exitosamente"}
        except Exception as e:
            print(f"Error al actualizar libro: {e}")
            return {"result": "Error al actualizar libro"}

    def eliminar_libro(self, libro_id):
        params = {'libro_id': libro_id}
        query = "UPDATE libros SET eliminado = TRUE WHERE libro_id = %(libro_id)s"
        try:
            self.mysql_pool.execute(query, params, commit=True)
            return {"result": "Libro eliminado lógicamente"}
        except Exception as e:
            print(f"Error al eliminar libro: {e}")
            return {"result": "Error al eliminar libro"}

    def obtener_libros_por_autor(self, autor_id):
        query = """
            SELECT L.libro_id, L.titulo_libro 
            FROM libros L 
            JOIN libro_autores LA ON L.libro_id = LA.libro_id 
            WHERE LA.autor_id = %s AND L.eliminado = FALSE
        """
        try:
            rv = self.mysql_pool.execute(query, (autor_id,))
            return [{"libro_id": r[0], "titulo_libro": r[1]} for r in rv]
        except Exception as e:
            print(f"Error al obtener libros por autor: {e}")
            return []

    def obtener_autores_de_libro(self, libro_id):
        query = """
            SELECT A.autor_id, A.nombre_autor 
            FROM autores A 
            JOIN libro_autores LA ON A.autor_id = LA.autor_id 
            WHERE LA.libro_id = %s
        """
        try:
            rv = self.mysql_pool.execute(query, (libro_id,))
            return [{"autor_id": r[0], "nombre_autor": r[1]} for r in rv]
        except Exception as e:
            print(f"Error al obtener autores del libro: {e}")
            return []
