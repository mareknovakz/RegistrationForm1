import sqlite3


def create_html_table_from_sql(database_file, table_name):
    try:
        conn = sqlite3.connect(database_file)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        if len(rows) == 0:
            return "<p>No data found in the table.</p>"

        html_output = "<table border='1'><tr>"
        # Add table headers
        for column_name in cursor.description:
            html_output += f"<th>{column_name[0]}</th>"
        html_output += "</tr>"

        # Add table rows
        for row in rows:
            html_output += "<tr>"
            for value in row:
                html_output += f"<td>{value}</td>"
            html_output += "</tr>"

        html_output += "</table>"
        return html_output

    except sqlite3.Error as e:
        return f"<p>Error accessing database: {e}</p>"
    finally:
        conn.close()


# Example usage:
if __name__ == "__main__":
    html_table = create_html_table_from_sql("DatabaseUser.db", "users")
    with open("users_table.html", "w") as file:
        file.write(html_table)
