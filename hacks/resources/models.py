# coding: utf-8

from apis import db
from datetime import datetime


#{=> resources|model <=}

    id = db.Column(db.Integer, primary_key=True)
    create_at = db.Column(db.DateTime, default=datetime.utcnow())
    name = db.Column(db.String(164))

    def __init__(self, kwargs):
        self.name = kwargs.get('name')

    def to_json(self):
        return {
            'id': self.id,
            'create_at': self.create_at.strftime("%Y-%m-%d %H:%M:%S"),
            'name': self.name,
        }
