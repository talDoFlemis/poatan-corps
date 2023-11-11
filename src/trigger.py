from src.helper import create_connection

# 1. Implemente um gatilho no banco de dados que dispara toda vez que um Tripulante  ́e cadastrado ou quando
# o atributo “funcao” tem seu valor modificado. O gatilho deve garantir que somente um dos tripulantes
# tenha a fun ̧c ̃ao “Capit ̃ao”.
# 2. Crie um segundo gatilho que restrinja que somente empregados da manuten ̧c ̃ao possam ser escolhidos para
# executar movimenta ̧c ̃oes do tipo “Manuten ̧c ̃ao”.


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
            UPDATE trip SET funcao = 'Oficial de Convés' WHERE funcao = 'Capitão';
            RETURN NEW;
        END IF;
    END;
    $$;
    """
    cursor.execute(create_function)

    create_trigger = """
    CREATE OR REPLACE TRIGGER tripulante_capitao
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
    BEGIN
        IF SELECT tipo FROM mov WHERE id_mov = NEW.id_mov AND tipo = 'Manutenção' THEN
            IF SELECT funcao FROM emp where id_emp = NEW.id_emp AND NOT funcao = 'Manutenção' THEN
                RETURN;
            END IF;
        END IF;
        RETURN NEW;
    END;
    $$;
    """

    cursor.execute(create_function)
    create_trigger = """
    CREATE OR REPLACE TRIGGER empregado_manutencao
    BEFORE INSERT OR UPDATE OF funcao ON mov_emp
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


def insert_capitao(conn):
    print("\nRunning Insert Capitao")
    cursor = conn.cursor()

    cursor.close()
    conn.commit()


def main():
    conn = create_connection()

    create_trigger_tripulante_capitao(conn)
    create_trigger_empregado_manutencao(conn)
    insert_mov_emp(conn)
    # insert_capitao(conn)

    conn.commit()

    print("Done Trigger")
    conn.close()


if __name__ == "__main__":
    main()
