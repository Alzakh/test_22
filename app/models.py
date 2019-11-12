from app import db

class Client(db.Model):
    client_id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(20), unique=True, nullable=False)
    points = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Client {}>'.format(self.client_id)

class Client_Check(db.Model):
    check_id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(20), db.ForeignKey('client.card_number'))
    check_sum = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Check {}>'.format(self.check_id)

class Check_Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    check_id = db.Column(db.Integer, db.ForeignKey('client_check.check_id'))
    position_sum = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Check {}>'.format(self.id)