from src.helper import create_connection


def create_trigger_tripulante_capitao(conn):
    print("\nRunning Tripulante Capitao Trigger")
    cursor = conn.cursor()

    create_function = """
    CREATE OR REPLACE FUNCTION tripulante_capitao()
    RETURNS TRIGGER
    LANGUAGE plpgsql
    AS
    $$
    BEGIN
        IF NEW.funcao = 'Capitão' THEN
            UPDATE trip SET funcao = 'Oficial de Convés' WHERE funcao = 'Capitão' AND id_emb = NEW.id_emb;
        END IF;
        RETURN NEW;
    END;
    $$;
    """
    cursor.execute(create_function)

    create_trigger = """
    CREATE TRIGGER tripulante_capitao
    BEFORE INSERT OR UPDATE OF funcao ON trip
    FOR EACH ROW
    EXECUTE PROCEDURE tripulante_capitao();
    """
    cursor.execute(create_trigger)

    cursor.close()
    conn.commit()


def create_trigger_empregado_manutencao(conn):
    print("\nRunning Empregado Manutenção Trigger")
    cursor = conn.cursor()

    create_function = """
    CREATE OR REPLACE FUNCTION empregado_manutencao()
    RETURNS TRIGGER
    LANGUAGE plpgsql
    AS
    $$
    DECLARE mov_manu bool;
    DECLARE emp_manu bool;
    BEGIN
        mov_manu = EXISTS(SELECT * FROM mov WHERE tipo = 'Manutenção' AND id_mov = NEW.id_mov);
        emp_manu = EXISTS(SELECT * FROM emp WHERE id_emp = NEW.id_emp AND funcao = 'Manutenção');
        IF mov_manu = TRUE AND emp_manu = FALSE THEN
            RETURN NULL;
        END IF;
        RETURN NEW;
    END;
    $$;
    """

    cursor.execute(create_function)
    create_trigger = """
    CREATE TRIGGER empregado_manutencao
    BEFORE INSERT ON mov_emp
    FOR EACH ROW
    EXECUTE PROCEDURE empregado_manutencao();
    """
    cursor.execute(create_trigger)

    cursor.close()
    conn.commit()


def insert_mov_emp(conn):
    print("\nRunning Insert Mov Emp")
    cursor = conn.cursor()

    insert = """
    INSERT INTO mov_emp (id_mov, id_emp) VALUES
    (5, 5),
    (5, 2);
    """
    cursor.execute(insert)

    cursor.close()


def insert_other_caps(conn):
    print("\nRunning Insert Other Caps")
    cursor = conn.cursor()
    insert_others_caps = """
    INSERT INTO trip(id_trp, nome, data_nasc, funcao, id_emb) VALUES
    (7, 'Tripulante7', '1980-09-04', 'Capitão', 4),
    (8, 'Tripulante8', '1985-03-03', 'Capitão', 2);
    """
    cursor.execute(insert_others_caps)

    cursor.close()
    conn.commit()


def insert_capitao(conn):
    print("\nRunning Insert Capitao")
    cursor = conn.cursor()
    insert_others_caps = """
    UPDATE trip SET funcao = 'Capitão' WHERE nome = 'Tripulante3';
    """
    cursor.execute(insert_others_caps)

    cursor.close()
    conn.commit()


def main():
    conn = create_connection()

    create_trigger_tripulante_capitao(conn)
    create_trigger_empregado_manutencao(conn)
    insert_mov_emp(conn)
    insert_other_caps(conn)
    insert_capitao(conn)

    conn.commit()

    print("\nDone Trigger")
    conn.close()


if __name__ == "__main__":
    main()
