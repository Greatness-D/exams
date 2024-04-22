from pydantic import BaseModel
from typing import List


class Patients(BaseModel):
  id: int
  name: str
  age: int
  sex: str
  weight: int
  height: int
  phone: int




class PatientsCreate(BaseModel):
  name: str
  age: int
  sex: str
  weight: int
  height: int
  phone: int

patients: dict[int, Patients] = {

  0: Patients(
    id= 0,
    name= 'John Doe',
    age= 18,
    sex= 'Male',
    weight= 30,
    height= 25,
    phone= 0000

  ),
   1: Patients(
    id= 1,
    name= 'User User',
    age= 21,
    sex= 'Male',
    weight= 30,
    height= 30,
    phone= 1111,

   ),
   2: Patients(
    id= 2,
    name= 'Look Me',
    age= 20,
    sex= 'Female',
    weight= 30,
    height= 45,
    phone= 2222

   )
}

