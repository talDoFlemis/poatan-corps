from src.helper import create_connection


def drop_tables(conn) -> None:
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS emb CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS trip CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS emp CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS mov CASCADE;")
    cursor.execute("DROP TABLE IF EXISTS mov_emp CASCADE;")
    cursor.execute("DROP FUNCTION IF EXISTS empregado_do_mes;")
    cursor.execute("DROP FUNCTION IF EXISTS tripulante_capitao;")
    cursor.execute("DROP FUNCTION IF EXISTS empregado_manutencao;")
    cursor.execute("DROP TRIGGER IF EXISTS tripulante_capitao ON trip CASCADE;")
    cursor.execute("DROP TRIGGER IF EXISTS empregado_manutencao ON mov_emp CASCADE")
    conn.commit()
    cursor.close()


def main() -> None:
    conn = create_connection()

    drop_tables(conn)
    print("Tables dropped successfully!")
    conn.close()


if __name__ == "__main__":
    main()
