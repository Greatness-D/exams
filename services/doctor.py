from schema.doctor import DoctorCreate, doctors
from schema.patient import patients

class DoctorService:

  @staticmethod
  def create_dcotor(payload: DoctorCreate):
    id = len(doctors)
    doctor = doctors[payload.doctor]
    doctor = doctors(
      id=id,
      name=name,
      specialization=payload.specialization,
      phone=payload.phone,
      is_available=payload.is_available

    )
    doctors.append(doctor)
    return doctor



