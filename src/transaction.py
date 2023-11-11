from src.helper import create_connection


# Escreva um novo script em Python que realize as seguintes opera ̧c ̃oes em uma  ́unica transa ̧c ̃ao:
# 1. Inserir nova Movimenta ̧c ̃ao: (6, ‘2023-10-05’, ‘Manuten ̧c ̃ao’, 1)
# 2. Inserir nova Movimenta ̧c ̃ao Empregado: (6, 1)
# 3. Retornar a quantidade de movimenta ̧c ̃oes que envolvem embarca ̧c ̃oes do tipo “Cargueiro”.

def transaction(conn):
    print("\nRunning transaction")
    cursor = conn.cursor()

    insert_mov = """
    INSERT INTO mov (id_mov, data, tipo, id_emb) VALUES
    (6, '2023-10-05', 'Manutenção', 1);
    """
    cursor.execute(insert_mov)

    insert_mov_emp = """
    INSERT INTO mov_emp (id_mov, id_emp) VALUES
    (6, 1);
    """
    cursor.execute(insert_mov_emp)


    query = """
    SELECT COUNT(*) as quant FROM mov m
    JOIN emb e ON m.id_emb = e.id_emb
    WHERE e.tipo = 'Cargueiro';
    """
    cursor.execute(query)

    response = cursor.fetchone()
    print(f"The number of movements involving cargo ships is {response[0]}")

    conn.commit()

def main():
    conn = create_connection()

    transaction(conn)

    print("Done Transaction")
    conn.close()


if __name__ == "__main__":
    main()
