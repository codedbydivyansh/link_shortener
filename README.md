# 🔗 Link Shortener

A simple URL Shortener built using Flask that converts long URLs into short, shareable links.

## Features

- Generate unique short URLs
- Redirect users to original URLs
- Track click count for each shortened link
- Dashboard to view all URLs and statistics
- Custom 404 page for invalid short links
- JSON-based data storage

## Tech Stack

- Python
- Flask
- HTML5
- CSS3
- JSON

## Project Structure

```
link_shortener/
│
├── static/
│   └── style.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── dashboard.html
│   └── 404.html
│
├── app.py
├── urls.json
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository

```bash
git clone https://github.com/codedbydivyansh/link_shortener.git
```

Move into the project

```bash
cd link_shortener
```

Create virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the app

```bash
python app.py
```

Visit

```
http://127.0.0.1:5000
```

---

## Screenshots

### Homepage

(Add screenshot here)

### Dashboard

(Add screenshot here)

---

## Future Improvements

- SQLite Database
- User authentication
- QR Code generation
- Link expiration
- Copy-to-clipboard button
- Analytics graphs

---

## Author

Divyansh