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

    # Retorna la estructura exacta de la nueva fila de la tabla
    response = f"""
    <tr>
        <td class="ps-4 py-3 fw-medium text-dark">{title}</td>
        <td class="py-3 text-secondary">
            <span class="badge bg-secondary-subtle text-secondary-emphasis rounded-pill">
                @{author_name}
            </span>
        </td>
        <td class="text-end pe-4 py-3">
            <div class="btn-group btn-group-sm" role="group">
                <button class="btn btn-outline-primary"
                    hx-get="/get-edit-form/{global_new_object.new_id}">
                    Editar
                </button>
                <button hx-delete="/delete/{global_new_object.new_id}"
                    class="btn btn-outline-danger">
                    Borrar
                </button>
            </div>
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

    # Formulario inline con input estilizado para Bootstrap 5
    response = f"""
    <tr hx-trigger='cancel' class='editing table-warning' hx-get="/get-new-row/{id}">
        <td class="ps-4 py-2">
            <input type="text" class="form-control form-control-sm" name="title" value="{new.title}" required />
        </td>
        <td class="py-2 text-secondary">
            <span class="badge bg-secondary-subtle text-secondary-emphasis rounded-pill">
                @{author.name}
            </span>
        </td>
        <td class="text-end pe-4 py-2">
            <div class="btn-group btn-group-sm" role="group">
                <button class="btn btn-sm btn-secondary" hx-get="/get-new-row/{id}">
                    Cancelar
                </button>
                <button class="btn btn-sm btn-success" hx-put="/update/{id}" hx-include="closest tr">
                    Guardar
                </button>
            </div>
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
        <td class="ps-4 py-3 fw-medium text-dark">{new.title}</td>
        <td class="py-3 text-secondary">
            <span class="badge bg-secondary-subtle text-secondary-emphasis rounded-pill">
                @{author.name}
            </span>
        </td>
        <td class="text-end pe-4 py-3">
            <div class="btn-group btn-group-sm" role="group">
                <button class="btn btn-outline-primary"
                    hx-get="/get-edit-form/{id}">
                    Editar
                </button>
                <button hx-delete="/delete/{id}"
                    class="btn btn-outline-danger">
                    Borrar
                </button>
            </div>
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
        <td class="ps-4 py-3 fw-medium text-dark">{title}</td>
        <td class="py-3 text-secondary">
            <span class="badge bg-secondary-subtle text-secondary-emphasis rounded-pill">
                @{author.name}
            </span>
        </td>
        <td class="text-end pe-4 py-3">
            <div class="btn-group btn-group-sm" role="group">
                <button class="btn btn-outline-primary"
                    hx-get="/get-edit-form/{id}">
                    Editar
                </button>
                <button hx-delete="/delete/{id}"
                    class="btn btn-outline-danger">
                    Borrar
                </button>
            </div>
        </td>
    </tr>
    """
    return response