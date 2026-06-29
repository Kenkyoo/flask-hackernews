from app import app, db
from flask import render_template, request, jsonify
from app.models import Author, New

@app.route("/", methods=["GET"])
def home():
    news = db.session.query(New, Author).filter(New.author_id == Author.author_id).all()
    return render_template("index.html", news=news)

@app.route("/submit", methods=["POST"])
def submit():
    global_new_object = New()

    title = request.form["title"]
    author_name = request.form["author"]

    author_exists = db.session.query(Author).filter(Author.name == author_name).first()
    print(author_exists)
    # check if author already exists in db
    if author_exists:
        author_id = author_exists.author_id
        new = New(author_id=author_id, title=title)
        db.session.add(new)
        db.session.commit()
        global_new_object = new
    else:
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        new = New(author_id=author.author_id, title=title)
        db.session.add(new)
        db.session.commit()
        global_new_object = new

    response = f"""
    <tr>
        <td>{title}</td>
        <td>{author_name}</td>
        <td>
            <button class="btn btn-primary"
                hx-get="/get-edit-form/{global_new_object.new_id}">
                Edit Title
            </button>
        </td>
        <td>
            <button hx-delete="/delete/{global_new_object.new_id}"
                class="btn btn-primary">
                Delete
            </button>
        </td>
    </tr>
    """
    return response

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_new(id):
    new = New.query.get(id)
    db.session.delete(new)
    db.session.commit()

    return ""

@app.route("/get-edit-form/<int:id>", methods=["GET"])
def get_edit_form(id):
    new = New.query.get(id)
    author = Author.query.get(new.author_id)

    response = f"""
    <tr hx-trigger='cancel' class='editing' hx-get="/get-new-row/{id}">
  <td><input name="title" value="{new.title}"/></td>
  <td>{author.name}</td>
  <td>
    <button class="btn btn-primary" hx-get="/get-new-row/{id}">
      Cancel
    </button>
    <button class="btn btn-primary" hx-put="/update/{id}" hx-include="closest tr">
      Save
    </button>
  </td>
    </tr>
    """
    return response

@app.route("/get-new-row/<int:id>", methods=["GET"])
def get_new_row(id):
    new = New.query.get(id)
    author = Author.query.get(new.author_id)

    response = f"""
    <tr>
        <td>{new.title}</td>
        <td>{author.name}</td>
        <td>
            <button class="btn btn-primary"
                hx-get="/get-edit-form/{id}">
                Edit Title
            </button>
        </td>
        <td>
            <button hx-delete="/delete/{id}"
                class="btn btn-primary">
                Delete
            </button>
        </td>
    </tr>
    """
    return response

@app.route("/update/<int:id>", methods=["PUT"])
def update_new(id):
    db.session.query(New).filter(New.new_id == id).update({"title": request.form["title"]})
    db.session.commit()

    title = request.form["title"]
    new = New.query.get(id)
    author = Author.query.get(new.author_id)

    response = f"""
    <tr>
        <td>{title}</td>
        <td>{author.name}</td>
        <td>
            <button class="btn btn-primary"
                hx-get="/get-edit-form/{id}">
                Edit Title
            </button>
        </td>
        <td>
            <button hx-delete="/delete/{id}"
                class="btn btn-primary">
                Delete
            </button>
        </td>
    </tr>
    """
    return response