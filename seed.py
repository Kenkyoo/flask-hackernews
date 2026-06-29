from app import app, db
from app.models import Author, New

with app.app_context():
    db.drop_all()
    db.create_all()

    # --- Autores ---
    authors_data = [
        "pg",
        "tptacek",
        "dang",
        "franco",
        "patio11",
        "jacquesm",
        "throw_away_dev",
        "xyzzy_hn",
    ]

    authors = [Author(name=name) for name in authors_data]
    db.session.add_all(authors)
    db.session.flush()

    # Referencia rápida por nombre
    a = {author.name: author for author in authors}

    # --- Noticias ---
    stories = [
        # Tecnología / dev
        New(title="Ask HN: What's your favorite underrated command-line tool?", author=a["franco"]),
        New(title="SQLite is not a toy database (2024)", author=a["tptacek"]),
        New(title="How I built a side project with Flask and deployed it for free", author=a["franco"]),
        New(title="Show HN: I made a HN clone with Flask and SQLite", author=a["franco"]),
        New(title="Why I stopped using ORMs and went back to raw SQL", author=a["jacquesm"]),
        New(title="Understanding Python's GIL once and for all", author=a["patio11"]),
        New(title="Docker is overengineering for most side projects", author=a["throw_away_dev"]),
        New(title="Ask HN: How do you manage dotfiles across machines?", author=a["xyzzy_hn"]),

        # Startups / negocios
        New(title="The surprisingly high cost of 'free' cloud tiers", author=a["patio11"]),
        New(title="Lessons from 10 years of running a bootstrapped SaaS", author=a["patio11"]),
        New(title="Ask HN: Is it worth getting an MBA if you want to found a startup?", author=a["xyzzy_hn"]),

        # Seguridad
        New(title="A deep dive into SQL injection: still relevant in 2025", author=a["tptacek"]),
        New(title="Why your password hashing is probably wrong", author=a["tptacek"]),
        New(title="Show HN: Open-source tool to audit Flask routes for common vulns", author=a["throw_away_dev"]),

        # Cultura / misc HN
        New(title="Ask HN: What book changed how you think about software?", author=a["dang"]),
        New(title="The myth of the 10x developer", author=a["jacquesm"]),
        New(title="In defense of boring technology", author=a["jacquesm"]),
        New(title="Ask HN: What do you do when you're burned out?", author=a["throw_away_dev"]),
        New(title="Paul Graham: How to do great work", author=a["pg"]),
        New(title="The unreasonable effectiveness of just starting", author=a["pg"]),
    ]

    db.session.add_all(stories)
    db.session.commit()

    print(f"Seed OK: {Author.query.count()} autores, {New.query.count()} noticias.")