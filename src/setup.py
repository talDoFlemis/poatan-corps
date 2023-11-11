from src.helper import create_connection


def create_tables(conn) -> None:
    cursor = conn.cursor()
    emb_query = """
    CREATE TABLE IF NOT EXISTS emb (
        id_emb SERIAL PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        tipo VARCHAR(50) NOT NULL
    );
    """
    cursor.execute(emb_query)

    trip_query = """
    CREATE TABLE IF NOT EXISTS trip (
        id_trp SERIAL PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        funcao VARCHAR(50) NOT NULL,
        data_nasc TIMESTAMPTZ NOT NULL,
        id_emb INTEGER NOT NULL REFERENCES emb(id_emb)
    );
    """
    cursor.execute(trip_query)

    emp_query = """
    CREATE TABLE IF NOT EXISTS emp (
        id_emp SERIAL PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        data_nasc TIMESTAMPTZ NOT NULL,
        funcao VARCHAR(50) NOT NULL
    );
    """
    cursor.execute(emp_query)

    mov_query = """
    CREATE TABLE IF NOT EXISTS mov (
        id_mov SERIAL PRIMARY KEY,
        data TIMESTAMPTZ NOT NULL,
        tipo VARCHAR(50) NOT NULL,
        id_emb INTEGER NOT NULL REFERENCES emb(id_emb)
    );
    """
    cursor.execute(mov_query)

    mov_emp_query = """
    CREATE TABLE IF NOT EXISTS mov_emp (
        id_mov INTEGER  REFERENCES mov(id_mov),
        id_emp INTEGER NOT NULL REFERENCES emp(id_emp),
        PRIMARY KEY (id_mov, id_emp)
    );
    """
    cursor.execute(mov_emp_query)

    conn.commit()
    cursor.close()


def seed_tables(conn) -> None:
    cursor = conn.cursor()

    emb_insert = """
    INSERT INTO emb (id_emb, nome, tipo) VALUES
    (1, 'Navio1', 'Cargueiro'),
    (2, 'Navio2', 'Passageiro'),
    (3, 'Navio3', 'Petroleiro'),
    (4, 'Navio4', 'Cargueiro');
    """
    cursor.execute(emb_insert)

    trip_insert = """
    INSERT INTO trip (id_trp, nome, data_nasc, funcao, id_emb) VALUES
    (1, 'Tripulante1', '1990-01-15', 'Oficial de Convés',  1),
    (2, 'Tripulante2', '1992-03-20', 'Engenheiro',  1),
    (3, 'Tripulante3', '1988-11-05', 'Comissário de Bordo',  2),
    (4, 'Tripulante4', '1995-06-30', 'Oficial de Convés',  3),
    (5, 'Tripulante5', '1991-07-10', 'Capitão',  4),
    (6, 'Tripulante6', '1994-09-25', 'Engenheiro',  4);
    """
    cursor.execute(trip_insert)

    emp_insert = """
    INSERT INTO emp (id_emp, nome, data_nasc, funcao) VALUES
    (1, 'Empregado1', '1985-05-12', 'Manutenção'),
    (2, 'Empregado2', '1993-02-28', 'Segurança'),
    (3, 'Empregado3', '1987-09-18', 'Logistica'),
    (4, 'Empregado4', '1990-12-05', 'Limpeza'),
    (5, 'Empregado5', '2001-08-30', 'Manutenção');
    """
    cursor.execute(emp_insert)

    mov_insert = """
    INSERT INTO mov (id_mov, data, tipo, id_emb) VALUES
    (1, '2023-09-01', 'Carga', 1),
    (2, '2023-09-02', 'Embarque de Passageiros', 2),
    (3, '2023-10-05', 'Abastecimento', 3),
    (4, '2023-10-05', 'Descarga', 1),
    (5, '2023-10-05', 'Manutenção', 4);
    """
    cursor.execute(mov_insert)

    mov_emp_insert = """
    INSERT INTO mov_emp (id_mov, id_emp) VALUES
    (1, 1),
    (1, 3),
    (2, 2),
    (3, 1),
    (3, 4),
    (4, 1),
    (4, 3),
    (5, 1);
    """
    cursor.execute(mov_emp_insert)

    conn.commit()
    cursor.close()


def main() -> None:
    conn = create_connection()

    create_tables(conn)
    seed_tables(conn)
    print("Tables created and seeded successfully.")


if __name__ == "__main__":
    main()
