# valchrom_backend

## Requirements

- Python 3.x

## Start application

- Create a virtual environment

```sh
pip -m venv events-service
```

- Activate virtual environment

```sh
events-service\Scripts\activate
```

- Install dependencies

```sh
pip install -r requirements.txt
```

- Move to project directory

```sh
cd events_service
```

- Run migrations to sync up the database

```sh
python manage.py migrate
```

- Start development server

```sh
python manage.py runserver
```

Application should be available at [`localhost:8000`](http://localhost:8000)

## Available Endpoints

- Events [`localhost:8000/api/v1/events/`](http://localhost:8000/api/v1/events/)
- Venues [`localhost:8000/api/v1/venues/`](http://localhost:8000/api/v1/venues/)
- Seats [`localhost:8000/api/v1/venues/:id/seats`](http://localhost:8000/api/v1/venues/:id/seats)
- Dates [`localhost:8000/api/v1/dates/`](http://localhost:8000/api/v1/dates/)
- Ticket Types [`localhost:8000/api/v1/dates/:id/ticket-types`](http://localhost:8000/api/v1/dates/:id/ticket-types)
- Ticket Type Seats [`localhost:8000/api/v1/dates/:id/ticket-types/:slug/tickets`](http://localhost:8000/api/v1/dates/:id/ticket-types/:slug/seats)