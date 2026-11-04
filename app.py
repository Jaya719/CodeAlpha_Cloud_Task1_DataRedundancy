from flask import Flask, render_template, request, redirect, flash
from database import get_connection
from validation import validate_student

app = Flask(__name__)
app.secret_key = "task1_secret_key"


@app.route("/")
def home():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students ORDER BY id DESC")
    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("index.html", students=students)


@app.route("/add", methods=["POST"])
def add_student():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    department = request.form.get("department", "").strip()

    valid, message = validate_student(name, email, department)

    if not valid:
        flash(message)
        return redirect("/")

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO students (name, email, department) VALUES (%s, %s, %s)",
            (name, email, department)
        )

        conn.commit()
        flash("Student added successfully!")

    except Exception as e:
        flash(f"Error: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)