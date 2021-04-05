from flask import Flask
from flask import request
import json
from connection import connect_to_database

app = Flask(__name__)

conn = connect_to_database()
cur = conn.cursor()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/cars", methods=["GET", "POST"])
def cars() -> str:
    if request.method == "GET":
        try:
            cur.execute("SELECT * FROM cars")
            rows = cur.fetchall()
            cars = [{"id": row[0], "model": row[1], "color": row[2]} for row in rows]
            return json.dumps({"cars": cars})
        except:
            return json.dumps({"error": "CANNOT RETRIEVE CARS"}), 500

    if request.method == "POST":
        try:
            car_data = json.loads(request.data)
            cur.execute(f"INSERT INTO cars(model, color) VALUES('{car_data['car']['model']}', '{car_data['car']['color']}')")
            cur.execute("SELECT * FROM cars")
            rows = cur.fetchall()
            return json.dumps({"car": {"id": rows[-1][0], "model": rows[-1][1], "color": rows[-1][2]}})
        except:
            return json.dumps({"error": "CANNOT RETRIEVE USERS"}), 500

    else:
        return json.dumps({"error": "BAD REQUEST"}), 400


@app.route("/cars/<car_id>", methods=["GET", "PUT", "DELETE"])
def car(car_id: str) -> str:
    if request.method == "GET":
        try:
            cur.execute(f"SELECT * FROM cars WHERE id={car_id}")
            row = cur.fetchone()
            car = {"id": row[0], "model": row[1], "color": row[2]}
            return json.dumps({"car": car})
        except:
            return json.dumps({"error": "CANNOT RETRIEVE CAR"}), 500

    if request.method == "PUT":
        try:
            car_data = json.loads(request.data)
            if "car" in car_data and "model" in car_data['car'] and "color" in car_data['car']:
                cur.execute(f'''UPDATE cars
                SET model = '{car_data['car']['model']}', color='{car_data['car']['color']}'
                WHERE id={car_id}
                RETURNING *;''')
                row = cur.fetchone()
                car = {"id": row[0], "model": row[1], "color": row[2]}
                return json.dumps({"car": car})
            else:
                return json.dumps({"error": "BAD REQUEST"}), 400
        except:
            return json.dumps({"error": "CANNOT RETRIEVE CAR"}), 500

    if request.method == "DELETE":
        try:
            cur.execute(f'''DELETE FROM cars
            WHERE id = {car_id};''')
            return json.dumps({"message": "CAR WAS DELETED"})
        except:
            return json.dumps({"error": "CANNOT RETRIEVE CAR"}), 500

    else:
        return json.dumps({"error": "BAD REQUEST"}), 400


if __name__ == '__main__':
    app.run()
