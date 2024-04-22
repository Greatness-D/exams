from schema.patient import patients, PatientsCreate

class PatientService:


  @staticmethod
  def parse_patients(patient_data):
    data = []
    for patien in patients:
      data.append(patient_data[patien])
    return{'message': 'successful', 'data': data}

  @staticmethod
  def get_patient_by_id(patient_id):
    return patients[patient_id]

  @staticmethod
  def create_patient(patient_data):
    id = len(patients) 
    patient = Patients(
      id=id,
      **patient_data.model_duump()

    )
    patients[id] = patient
    return patient