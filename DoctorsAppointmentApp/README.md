
# DoctorsAppointmentApp

## Run locally
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Swagger:
http://127.0.0.1:8000/docs

## Test
pytest
