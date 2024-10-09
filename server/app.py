#!/usr/bin/env python3

from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from sqlalchemy import desc

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
    bakeries = Bakery.query.all()
    bakeries_dict = [bakery.to_dict() for bakery in bakeries]
    return make_response(bakeries_dict, 200)

@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery = Bakery.query.filter_by(id = id).first()
    bakery_dict = bakery.to_dict()
    return make_response(bakery_dict, 200)

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    # Get all baked goods from the db
    # Order them price descending
    # Loop through the goods converting each to dict
    # Create a response
    baked_goods = BakedGood.query.order_by(desc(BakedGood.price)).all()
    baked_goods_list = [baked_good.to_dict() for baked_good in baked_goods]
    return make_response(baked_goods_list, 200)

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    baked_good = BakedGood.query.order_by(desc(BakedGood.price)).first()
    baked_good_dict = baked_good.to_dict()
    return make_response(baked_good_dict, 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
