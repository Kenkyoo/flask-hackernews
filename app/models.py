from app import db

class Author(db.Model):
    author_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    news = db.relationship("New", backref="author")

    def __repr__(self):
        return '<Author: {}>'.format(self.news)

class New(db.Model):
    new_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey("author.author_id"))
    title = db.Column(db.String)