from src.helper import create_connection


def stored_procedure(conn):
    print("\nRunning Stored Procedure")
    cursor = conn.cursor()

    create_proc = """
    CREATE OR REPLACE FUNCTION empregado_do_mes(data_mov TIMESTAMPTZ)
    RETURNS TABLE (id_emp INTEGER, nome VARCHAR(50))
    LANGUAGE plpgsql
    AS $$
    BEGIN
        RETURN QUERY
        SELECT e.id_emp, e.nome FROM emp e
        JOIN mov_emp me ON e.id_emp = me.id_emp
        JOIN mov m ON m.id_mov = me.id_mov
        WHERE m.data >= data_mov AND m.data < data_mov + INTERVAL '1 month'
        GROUP BY e.id_emp, e.nome
        ORDER BY COUNT(*) DESC
        LIMIT 1;
    END;
    $$
    """
    cursor.execute(create_proc)

    call_proc = """
    SELECT id_emp, nome FROM empregado_do_mes('2023-10-01');
    """
    cursor.execute(call_proc)
    resp = cursor.fetchone()
    print(f"The employee of the month is {resp[1]} with id {resp[0]}")

    conn.commit()
    cursor.close()


def main():
    conn = create_connection()

    stored_procedure(conn)

    print("Done Stored Procedure")
    conn.close()


if __name__ == "__main__":
    main()
