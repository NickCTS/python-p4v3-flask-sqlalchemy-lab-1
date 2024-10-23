from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Earthquake

app = Flask(__name__)

# Configure your database (replace with your actual configuration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake_by_id(id):
    earthquake = Earthquake.query.filter_by(id=id).first()
    if earthquake:
        return jsonify(earthquake.to_dict()), 200
    else:
        return jsonify({"message": f"Earthquake {id} not found."}), 404

@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    quakes_data = [quake.to_dict() for quake in quakes]
    
    return jsonify({
        "count": len(quakes_data),
        "quakes": quakes_data
    }), 200

if __name__ == '__main__':
    app.run(port=5555)
