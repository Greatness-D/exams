from pydantic import BaseModel


class Doctors(BaseModel):
  id: int
  name: str
  specialization: str
  phone: int
  is_available: bool = True

class DoctorCreate(BaseModel):
  name: str
  specialization: str
  phone: int
  is_available: bool = True



doctors: dict[int, doctors] = {
  0: Doctors(
    id= 0,
    name='Boss World',
    specialization= 'Dentist',
    phone= 444,
    is_available = True


  ), 
  
 1: Doctors(
    id= 1,
    name= 'May Day',
    specialization= 'Surgeon',
    phone= 999,
    is_available = True

  ),
   
  2: Doctors(
    id= 2,
    name= 'Look Me',
    specialization= 'Admin',
    phone= 999,
    is_available = True
   )


}
