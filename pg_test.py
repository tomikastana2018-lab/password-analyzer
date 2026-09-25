import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password=""
    )
    cursor = connection.cursor()

    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()

    print("Successfully connected to PostgreSQL database")
    print(f"PostgreSQL version: {db_version}")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS test_users(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL
    );
    """)

    cursor.execute("""
    INSERT INTO test_users (name)
    VALUES (%s)
    """, ("polundra",))

    connection.commit()

    cursor.execute("SELECT * FROM test_users;")
    rows = cursor.fetchall()
    for user in rows:
        print(user)

    cursor.close()
    connection.close()

except Exception as error:
    print(f"Error: {error}")