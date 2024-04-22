from pydantic import BaseModel
from datetime import date
from schema.patient import Patients, patients

class Appointments(BaseModel):
  id: int
  patient: Patients
  doctor: Doctors[0]
  date: date

appointment: list[Apointments] = [
  Appointments(
    id= 0,
    patient=Patients[0],
    doctor=Doctors[0],
    date=date(2024, 4, 18)
  ),
  Appointments(
    id= 1,
    patient=Patients[0],
    doctor= Doctors[0],
    date=date(2024, 4, 18)
  )
]