from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#admin
class adminInfo(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    password=models.CharField(max_length=450)
    def __str__(self):
        return self.name
# #user login info
class users_login(models.Model):
      username=models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
      password=models.CharField(max_length=300)
      def __str__(self):
         return self.email
#doctor info database
class doctor_perinfo(models.Model):
    full_name=models.CharField(max_length=200)
    specialization=models.CharField(max_length=200,default=None)
    gender=models.CharField(max_length=50)
    date_of_birth=models.DateField(null=True,blank=True)
    nationality=models.CharField(max_length=100)
    def __str__(self):
        return self.full_name
#floor_info info database
class floor_info(models.Model):
    floor_name=models.CharField(max_length=200)
    floor_num=models.IntegerField()
    floor_description=models.TextField()
#nurse DataBase
class Nurse_Personal_info(models.Model):
    full_name=models.CharField(max_length=200)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=50)
    blood_group=models.CharField(max_length=50)
    nationality=models.CharField(max_length=100)
    def __str__(self):
        return self.full_name
class nurse_contact_info(models.Model):
    nurse_id=models.ForeignKey(Nurse_Personal_info,on_delete=models.CASCADE,null=True,blank=True)
    phone_number=models.CharField(max_length=150)
    email=models.EmailField()
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=150)
    country=models.CharField(max_length=150)
    def __str__(self):
        return self.country
class Department(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    department_name=models.CharField(max_length=200)
    department_code=models.CharField(max_length=100,null=True)
    department_head=models.CharField(max_length=200)
    description=models.TextField()
    location=models.CharField(max_length=250)
    contact_number=models.CharField(max_length=150,null=True,blank=True)
    opening_time=models.TimeField(null=True)
    closing_time=models.TimeField(null=True)
    total_doctors=models.IntegerField(null=True)
    total_nurses=models.IntegerField(null=True)
    status=models.CharField(max_length=150,null=True)
    def __str__(self):
        return self.department_name
#patient Info database
class patient_info(models.Model):
    full_name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=50)
    blood_group=models.CharField(max_length=10)
    martial_status=models.CharField(max_length=35)
    nationality=models.CharField(max_length=200)
    def __str__(self):
        return self.full_name
#beds info database
class beds_info(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    bed_number=models.IntegerField()
    room_no=models.IntegerField()
    bed_type=models.CharField(max_length=200)
    floor_number=models.IntegerField()
    bed_status=models.CharField(max_length=200)
    patient=models.CharField(max_length=200,null=True,blank=True)
    assigned_date=models.DateField()
    discharge_date=models.DateField()
    def __str__(self):
        return self.bed_type  
#room info database
class room_info(models.Model):
    room_number=models.IntegerField()
    room_type=models.CharField(max_length=200)
    floor_number=models.IntegerField()
    department=models.CharField(max_length=200,null=True,blank=True)
    capacity=models.CharField(max_length=200)
    occupied_beds=models.IntegerField()
    available_beds=models.CharField(max_length=200,null=True,blank=True)
    room_status=models.CharField(max_length=200)
    daily_charge=models.IntegerField()
    def __str__(self):
        return self.room_type
#nurse info database
class nurse_employee_info(models.Model):
    nu_id=models.ForeignKey(Nurse_Personal_info,on_delete=models.CASCADE,null=True,blank=True)
    department=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)
    nursing_license_number=models.CharField(max_length=200)
    years_of_experience=models.CharField(max_length=50)
    joining_date=models.DateField()
    employment_type=models.CharField(max_length=200)
    salary=models.FloatField()
    status=models.CharField(max_length=200)
    def __str__(self):
        return self.status
class nurse_work_info(models.Model):
    se_id=models.ForeignKey(Nurse_Personal_info,on_delete=models.CASCADE,null=True,blank=True)
    assigned_room=models.ForeignKey(room_info,on_delete=models.CASCADE,null=True,blank=True)
    assigned_doctor=models.ForeignKey(doctor_perinfo,on_delete=models.CASCADE,null=True,blank=True)
    shift_start=models.TimeField()
    shift_end=models.TimeField()
#appointments info database
class appointments(models.Model):
    patient =models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    doctor=models.CharField(max_length=200)
    appointment_date=models.DateField()
    appointment_time=models.TimeField()
    reason_for_visit=models.CharField(max_length=300)
    booked_date=models.DateField(null=True,blank=True)
    def __str__(self):
        return self.patient.username
#doctor info database
class Doctors_contact_info(models.Model):
    per_id=models.ForeignKey(doctor_perinfo,on_delete=models.CASCADE,null=True,blank=True)
    phone_number=models.CharField(max_length=200)
    email=models.EmailField()
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=50)
    country=models.CharField(max_length=100)
    def __str__(self):
        return self.phone_number
class DoctorsProfessionInfo(models.Model):
    pro_id=models.ForeignKey(doctor_perinfo,on_delete=models.CASCADE,null=True,blank=True)
    department=models.CharField(max_length=200,blank=True,null=True)#✔
    medical_lincense_num=models.CharField(max_length=200,blank=True,null=True)
    qualification=models.CharField(max_length=100)
    university=models.CharField(max_length=150)
    years_of_experience=models.IntegerField()
    consultation_fee=models.CharField(max_length=200,blank=True,null=True)
    biography=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.qualification
class doctors_statistics(models.Model):
    total_patients=models.ForeignKey(patient_info,on_delete=models.CASCADE)
    total_appointments=models.IntegerField()
    def __str__(self):
        self.total_patients
class doctors_hos_infp(models.Model):
    res_id=models.ForeignKey(doctor_perinfo,on_delete=models.CASCADE,null=True,blank=True)
    joining_date=models.DateField()
    employment_type=models.CharField(max_length=200,null=True,blank=True)
    office_num=models.IntegerField()
    status=models.CharField(max_length=50,default="active")
    def __str__(self):
        return self.status
class doctors_schedule(models.Model):
    doc_id=models.ForeignKey(doctor_perinfo,on_delete=models.CASCADE,null=True,blank=True)
    working_days=models.IntegerField(null=True,blank=True)
    start_time=models.TimeField()
    end_time=models.TimeField()
#patient info database
class patient_contact_info(models.Model):
    pat_id=models.ForeignKey(patient_info,on_delete=models.CASCADE,null=True,blank=True)
    phone_number=models.CharField(max_length=200)
    email=models.EmailField()
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    def __str__(self):
        return self.phone_number
class patient_emergency_con(models.Model):
    pat_id=models.ForeignKey(patient_info,on_delete=models.CASCADE,null=True,blank=True)
    emergency_con_name=models.CharField(max_length=100)
    emergency_number=models.CharField(max_length=100)
    def __str__(self):
        return self.emergency_number
class patient_Medical_info(models.Model):
    pat_id=models.ForeignKey(patient_info,on_delete=models.CASCADE,null=True,blank=True)
    allergies=models.CharField(max_length=150,blank=True)
    medical_history=models.TextField(null=True,blank=True)
    current_medication=models.CharField(max_length=250,null=True,blank=True)
    height=models.CharField(max_length=50)
    weight=models.CharField(max_length=50)
    def __str__(self):
        return self.allergies
class patient_hopital_info(models.Model):
    registeration_date=models.DateField()
    patient_type=models.CharField(max_length=50)
    assisgned_doctor=models.ForeignKey(doctor_perinfo,on_delete=models.CASCADE)
    department=models.ForeignKey(Department,on_delete=models.CASCADE)
    room_number=models.ForeignKey(room_info,on_delete=models.CASCADE)
    bed_number=models.ForeignKey(beds_info,on_delete=models.CASCADE)
    addmission_date=models.DateField()
    discharge_date=models.DateField()
    patient_status=models.CharField(max_length=50)
    def __str__(self):
        return self.assisgned_doctor
class patient_insurance(models.Model):
    insurance_provider=models.CharField(max_length=200)
    insurance_policy_number=models.CharField(max_length=200)
    insuarance_expiry=models.DateField()
    def __str__(self):
        return self.insurance_provider

#receptionist info database
class recep_person_info(models.Model):
    full_name=models.CharField(max_length=200)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=50)
    nationality=models.CharField(max_length=100)
    def __str__(self):
        return self.full_name
class recep_contact_info(models.Model):
    recep_id=models.ForeignKey(recep_person_info,on_delete=models.CASCADE,null=True,blank=True)
    phone_number=models.CharField(max_length=200)
    email=models.EmailField()
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    emergency_contact_name=models.CharField(max_length=200)
    emergency_contact_number=models.CharField(max_length=200)
    def __str__(self):
        return self.phone_number
class recep_employ_info(models.Model):
    sec_id=models.ForeignKey(recep_person_info,on_delete=models.CASCADE,null=True,blank=True)
    joining_date=models.DateField()
    department=models.CharField(max_length=200,null=True,blank=True)
    salary=models.FloatField()
    status=models.CharField(max_length=150)
    desk_number=models.IntegerField() 
    shift_start_time=models.TimeField()
    shift_end_time=models.TimeField()
    def __str__(self):
        return self.status
class ambulance_info(models.Model):
    ambulance_number=models.CharField(max_length=200)
    vehicle_model=models.CharField(max_length=200)
    registration_number=models.CharField(max_length=200)
    manufacturing_year=models.DateField(0)
    capacity=models.CharField(max_length=200)
    def __str__(self):
        return self.vehicle_model
class driver_info(models.Model):
    ambu_id=models.ForeignKey(ambulance_info,on_delete=models.CASCADE,null=True,blank=True)
    assigned_department=models.ForeignKey(Department,on_delete=models.CASCADE,null=True,blank=True)
    assigned_hospital=models.CharField(max_length=200)
    assigned_staff=models.CharField(max_length=200)
    availability_status=models.CharField(max_length=100)
class maintenance_info(models.Model):
    amser_id=models.ForeignKey(ambulance_info,on_delete=models.CASCADE,null=True,blank=True)
    service_date=models.DateField()
    next_service_date=models.DateField()
    maintenance_notes=models.TextField()
    fuel_status=models.CharField(max_length=150)
    def __str__(self):
        return self.fuel_status
#medicine info database
class medicine(models.Model):
    medicine_name=models.CharField(max_length=200)
    generic_name=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    dosage_form=models.CharField(max_length=200)
    strength=models.CharField(max_length=200)
    manufacturer=models.CharField(max_length=200)
    quantity_in_stock=models.CharField(max_length=200)
    unit_price=models.FloatField()
    expiry_date=models.DateField()
    prescription_required=models.TextField()
    status=models.CharField(max_length=200)
    def __str__(self):
        return self.medicine_name