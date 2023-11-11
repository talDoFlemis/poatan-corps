from helper import create_connection


def drop_tables(conn) -> None:
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS emb;")
    cursor.execute("DROP TABLE IF EXISTS trip;")
    cursor.execute("DROP TABLE IF EXISTS emp;")
    cursor.execute("DROP TABLE IF EXISTS mov;")
    cursor.execute("DROP TABLE IF EXISTS mov_emp;")
    cursor.commit()


def main() -> None:
    conn = create_connection()

    drop_tables(conn)


if __name__ == "__main__":
    main()
