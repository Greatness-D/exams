from fastapi import APIRouter 
from schema.doctor import DoctorCreate
from services.doctor import DoctorService


doctor_router = APIRouter()

@doctor_router.post('', status_code=201)
def create_doctor(payload: DoctorCreate):
  data=DoctorService.create_dcotor(payload)
  return data

