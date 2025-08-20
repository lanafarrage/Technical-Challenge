# Women's Safety Reports API

Tracks reports of unsafe situations in public spaces.

## Endpoints

- `POST /reports` — Add a new report
- `GET /reports` — View all reports, optionally filter by severity

## Running

1. Install dependencies:

```bash
python3 -m pip install fastapi "uvicorn[standard]" pydantic
