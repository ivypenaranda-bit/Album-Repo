# Photo Album Management

Simple Django Photo Album Management app configured for PostgreSQL and Cloudinary.

Environment variables (set on Render):
- `SECRET_KEY`
- `DEBUG` (0 or 1)
- `ALLOWED_HOSTS` (comma separated)
- `DATABASE_URL` (Postgres URL provided by Render)
- `CLOUDINARY_STORAGE` settings: `CLOUDINARY_URL` or `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET`

Local PostgreSQL testing:
- To use PostgreSQL locally, set `DATABASE_URL` in a `.env` file at the project root. Example `.env`:

```
SECRET_KEY=you-should-change-this
DEBUG=1
DATABASE_URL=postgres://user:password@localhost:5432/photo_album_db
```

Then run migrations — the app will use the Postgres DB when `DATABASE_URL` is present.

Quick local setup:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Deploy: create a Render Web Service, select this repo, set `PYTHONUNBUFFERED=1` and the env vars above. Use the `Procfile` and `requirements.txt`.

Notes:
- Create a Django superuser and optionally a `AlbumAdmin` group to assign album administrator privileges.
- Ensure Cloudinary credentials are set on Render; do not commit secrets.