from src.helper import create_connection


def query1(conn):
    print("\nQuery 1")

    cursor = conn.cursor()

    query = """
    SELECT e.nome, COUNT(t.id_trp) AS num_tripulantes
    FROM emb e
    LEFT JOIN trip t ON e.id_emb = t.id_emb
    GROUP BY e.nome;
    """
    cursor.execute(query)
    responses = cursor.fetchall()

    for emb, quant in responses:
        print(
            f"The name of the ship is {emb} and the number of crew members is {quant}"
        )


def query2(conn):
    print("\nQuery 2")
    cursor = conn.cursor()

    query = """
    SELECT e.nome FROM emp e
    JOIN mov_emp me ON e.id_emp = me.id_emp
    WHERE me.id_mov = 1;
    """

    cursor.execute(query)
    responses = cursor.fetchall()
    for name in responses:
        print(f"The name of the employee is {name[0]}")


def query3(conn):
    print("\nQuery 3")
    cursor = conn.cursor()

    query = """
    SELECT COUNT(*) as quant FROM mov m
    JOIN emb e ON m.id_emb = e.id_emb
    WHERE e.tipo = 'Cargueiro';
    """

    cursor.execute(query)
    response = cursor.fetchone()
    print(f"The number of movements involving cargo ships is {response[0]}")


def main():
    conn = create_connection()

    query1(conn)
    query2(conn)
    query3(conn)

    print("\nDone Consults")
    conn.close()


if __name__ == "__main__":
    main()
