import psycopg2

file_path = "query.txt"
out_path = "result.txt"
pgsql_parameter = {
    "host": "",
    "port": 0,
    "database": "",
    "user": "",
    "password": "",
}


def run_query(query, connection, out_file):
    with connection.cursor() as cursor:
        cursor.execute(f"explain analyze {query}")
        result = cursor.fetchall()
        for row in result:
            if "Planning Time" in str(row):
                print(str(row), end=" ")
                out_file.write(str(row) + " ")
            if "Execution Time" in str(row):
                print(str(row))
                out_file.write(str(row) + "\n")


with psycopg2.connect(**pgsql_parameter) as conn:
    with open(file_path, 'r', encoding='utf-8') as file, open(out_path, 'w') as out_file:
        for line_number, query in enumerate(file, start=1):
            query = query.strip()
            print(f"Query {line_number}: {query}")
            run_query(query, conn, out_file)

