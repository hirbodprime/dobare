# Dobare

Dobare ("دوباره", "again") is a small Django website for a second-hand clothing project. Visitors can submit used clothes through a form on the home page (with photos), browse a product catalog, read each item's story, and open a public product page that can be reached through a generated QR code. The UI is in Persian.

## Features

- Home page with a clothing submission form (brand, size, damage notes, full/fabric/brand photos)
- Product catalog page (`/products/`)
- Product "story" endpoint returning JSON for a modal (`/products/<id>/story/`)
- Public product page by UUID (`/p/<uuid>/`)
- PNG QR code for each product's public page (`/p/<uuid>/qr.png`)
- Django admin for managing submissions and products

## Tech stack

- Python 3, Django
- SQLite
- Pillow (image fields), `qrcode` (QR generation)
- Passenger WSGI (`passenger_wsgi.py`) for shared-hosting deployment

## Project structure

```
dobare/          Django project settings and root URLs
mainapp/         Models (SubmittedCloth, Product), views, URLs
templates/       index.html (plus alternate home designs), products.html, product_detail.html
static/          Static assets
passenger_wsgi.py  Entry point for Passenger hosting
```

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install django pillow qrcode
python manage.py migrate
python manage.py createsuperuser
```

There is no `requirements.txt` in the repo; the packages above are what the code imports.

## Configuration

Settings are hard-coded in `dobare/settings.py`. Before deploying, review:

- `SECRET_KEY` – replace with your own value (ideally loaded from an environment variable)
- `DEBUG` – set to `False` in production
- `ALLOWED_HOSTS` – add your domain, e.g. `example.com`
- `STATIC_ROOT`, `MEDIA_URL`, `MEDIA_ROOT` – adjust paths to your server layout

## Running

```bash
python manage.py runserver
```

Then open http://127.0.0.1:8000/ and manage content at `/admin/`.
