from django import forms

class loginInfo(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput)
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder":"enter email"
        }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"enter password"})
    )
class deletePatientData(forms.Form):
    patientId=forms.IntegerField(widget=forms.NumberInput)
class deletepatientContData(forms.Form):
    patientcontactId=forms.IntegerField(widget=forms.NumberInput)
class deleteEmerInfoPat(forms.Form):
    patientemercontactId=forms.IntegerField(widget=forms.NumberInput)
class deletePatientMedInfo(forms.Form):
    patientMedInfo=forms.IntegerField(widget=forms.NumberInput)
class DeleteNurseData(forms.Form):
    NurseId=forms.IntegerField(widget=forms.NumberInput)
class deleteNurseConInfo(forms.Form):
    NurseCOnId=forms.IntegerField(widget=forms.NumberInput)
class DeleteNuseEmpInfos(forms.Form):
    NurseEmId=forms.IntegerField(widget=forms.NumberInput)
class DeleteNurseWorksInfo(forms.Form):
    NurseWorkId=forms.IntegerField(widget=forms.NumberInput)
class deleteBeds(forms.Form):
    bedsId=forms.IntegerField(widget=forms.NumberInput)
class deleteApp(forms.Form):
    appId=forms.IntegerField(widget=forms.NumberInput)
class deleteRooms(forms.Form):
    roomId=forms.IntegerField(widget=forms.NumberInput)
class deleteFloorsInfo(forms.Form):
    floorId=forms.IntegerField(widget=forms.NumberInput)
class delRecepInformation(forms.Form):
    recepId=forms.IntegerField(widget=forms.NumberInput)
class deleterecepEmpInfo(forms.Form):
    continfoId=forms.IntegerField(widget=forms.NumberInput)
class delRecepEmpInfo(forms.Form):
    empId=forms.IntegerField(widget=forms.NumberInput)
class deleteAmbulance(forms.Form):
    ambId=forms.IntegerField(widget=forms.NumberInput)
class deleteDep(forms.Form):
    depId=forms.IntegerField(widget=forms.NumberInput)
class DeleteDoc(forms.Form):
    docId=forms.IntegerField(widget=forms.NumberInput)
class deleteMeds(forms.Form):
    medId=forms.IntegerField(widget=forms.NumberInput)
class checkPass(forms.Form):
    username=forms.CharField(max_length=200,widget=forms.TextInput)
    password=forms.CharField(max_length=200,widget=forms.PasswordInput)
class ptientInfo(forms.Form):
    name=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"placeholder":"enter your name"}))    
    date_of_birth=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    age=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"enter your age"}))
    gender=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":"enter your gender"}))#instead of input ,make it optin    
    blood_group=forms.CharField(max_length=10,widget=forms.TextInput(attrs={"placholder":"enter your blood group"}))
    martial_status=forms.CharField(max_length=35,required=False,widget=forms.TextInput(attrs={"placeholder":"enter your martial status"}))#make it like if user dont wanna they can skip it
    nationality=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"placeholder":"enter your nationality"}))
class patientnorInfo(forms.Form):
    phone_number=forms.CharField(max_length=200,widget=forms.TextInput(attrs={"placeholder":"enter your phone number"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"enter your email"}))
    address=forms.CharField(max_length=300,widget=forms.TextInput(attrs={"placeholder":"enter your address"}))
    city=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"enter your city"}))
    country=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"enter your country"}))
    emergency_contact_name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"enter you emergency contact name"}))
    emergency_number=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"placeholder":"enter your emergency contact number"}))
    allergies=forms.CharField(max_length=150,required=False,widget=forms.TextInput(attrs={"placeholder":"entr allergies if you have you can also skip it"}))
    height=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":"enter your height in centimeters"}))
    weight=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"placeholder":"enter your weight"}))
class doctorPersonalInfo(forms.Form):
    name=forms.CharField(max_length=200,widget=forms.TextInput)
    specialization=forms.CharField(max_length=200,widget=forms.TextInput)
    gender=forms.CharField(max_length=50,widget=forms.TextInput)
    date_of_birth=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    nationality=forms.CharField(max_length=100,widget=forms.TextInput)
class DoctorsData(forms.Form):
    phone_number=forms.CharField(max_length=200,widget=forms.TextInput)
    email=forms.EmailField(widget=forms.EmailInput)
    address=forms.CharField(max_length=150,widget=forms.TextInput)
    city=forms.CharField(max_length=50,widget=forms.TextInput)
    department=forms.CharField(max_length=200,widget=forms.TextInput)
    country=forms.CharField(max_length=100,widget=forms.TextInput)
    medical_lincense_num=forms.CharField(max_length=200,widget=forms.TextInput)
    qualification=forms.CharField(max_length=100,widget=forms.TextInput)
    university=forms.CharField(max_length=150,widget=forms.TextInput)
    years_of_experience=forms.IntegerField(widget=forms.NumberInput(attrs={"placeholder":"years of experience in numbers"}))
    biography=forms.CharField(widget=forms.Textarea)
class adminForms(forms.Form):
    name=forms.CharField(max_length=200,widget=forms.TextInput)
    email=forms.EmailField(widget=forms.EmailInput)
    password=forms.CharField(widget=forms.PasswordInput)
class DepartmentForms(forms.Form):
    dep_name=forms.CharField(max_length=200,widget=forms.TextInput)
    dep_code=forms.CharField(max_length=100,widget=forms.TextInput)
    dep_head=forms.CharField(max_length=200,widget=forms.TextInput)
    description=forms.CharField(widget=forms.Textarea)
    location=forms.CharField(max_length=250,widget=forms.TextInput)
    opening_time=forms.TimeField(widget=forms.TimeInput(attrs={"type":'time'}))
    closing_time=forms.TimeField(widget=forms.TimeInput(attrs={"type":'time'}))
    status=forms.CharField(max_length=150,initial='open',widget=forms.TextInput(attrs={"value":"open"}))
class docInfoForms(forms.Form):
    joining_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    employment_type=forms.CharField(max_length=200,widget=forms.TextInput)
    office_num=forms.IntegerField(widget=forms.NumberInput)
    status=forms.CharField(max_length=50,widget=forms.TextInput(attrs={"value":"active"}))
    workingDays=forms.IntegerField(widget=forms.NumberInput)
    start_time=forms.TimeField(widget=forms.TimeInput(attrs={"type":"time"}))
    end_time=forms.TimeField(widget=forms.TimeInput(attrs={"type":"time"}))
class recep_perInfo(forms.Form):
    name=forms.CharField(max_length=200,widget=forms.TextInput)
    date_of_birth=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    gender=forms.CharField(max_length=50,widget=forms.TextInput)
    nationality=forms.CharField(max_length=100,widget=forms.TextInput)
class recep_contact(forms.Form):
    phone_number=forms.CharField(max_length=200,widget=forms.TextInput)
    email=forms.EmailField(widget=forms.EmailInput)
    address=forms.CharField(max_length=200,widget=forms.TextInput)
    city=forms.CharField(max_length=200,widget=forms.TextInput)
    country=forms.CharField(max_length=200,widget=forms.TextInput)
    emergency_contact_name=forms.CharField(max_length=200,widget=forms.TextInput)
    emergency_contact_number=forms.CharField(max_length=200,widget=forms.TextInput)
    joining_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    salary=forms.FloatField(widget=forms.NumberInput)
    status=forms.CharField(max_length=150,widget=forms.TextInput(attrs={"placeholder":"e.g active"}))
    desk_number=forms.IntegerField(widget=forms.NumberInput)
    shift_start_time=forms.TimeField(widget=forms.TimeInput(attrs={"type":"time"}))
    shift_end_time=forms.TimeField(widget=forms.TimeInput(attrs={"type":"time"}))
class ambulanceInfo(forms.Form):
    ambulance_num=forms.CharField(max_length=200,widget=forms.TextInput)
    vehicle_model=forms.CharField(max_length=200,widget=forms.TextInput)
    registration_number=forms.CharField(max_length=200,widget=forms.TextInput)
    manufacturing_year=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    capacity=forms.CharField(max_length=200,widget=forms.TextInput)
class ambdriverAndmainInfo(forms.Form):
    assigned_hospital=forms.CharField(max_length=200,widget=forms.TextInput)
    assigned_staff=forms.CharField(max_length=200,widget=forms.TextInput)
    availability_status=forms.CharField(max_length=100,widget=forms.TextInput)
    service_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    next_service_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    maintenance_notes=forms.CharField(widget=forms.Textarea)
    fuel_status=forms.CharField(widget=forms.TextInput)
class nursePerInfo(forms.Form):
    name=forms.CharField(max_length=200,widget=forms.TextInput)
    date_of_birth=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    gender=forms.CharField(max_length=50,widget=forms.TextInput)
    blood_group=forms.CharField(max_length=50,widget=forms.TextInput)
    nationality=forms.CharField(max_length=100,widget=forms.TextInput)
    phone_number=forms.CharField(max_length=150,widget=forms.TextInput)
    email=forms.EmailField(widget=forms.EmailInput)
    address=forms.CharField(max_length=150,widget=forms.TextInput)
    city=forms.CharField(max_length=150,widget=forms.TextInput)
    country=forms.CharField(max_length=150,widget=forms.TextInput)
class NurseEmployInfo(forms.Form):
    department=forms.CharField(max_length=200,widget=forms.TextInput)
    qualification=forms.CharField(max_length=200,widget=forms.TextInput)
    nursing_license_number=forms.CharField(max_length=200,widget=forms.TextInput)
    years_of_experience=forms.CharField(max_length=50,widget=forms.TextInput)
    joining_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    employment_type=forms.CharField(max_length=200,widget=forms.TextInput)
    salary=forms.FloatField(widget=forms.NumberInput)
    status=forms.CharField(max_length=200,widget=forms.TextInput)
    shift_start=forms.TimeField(widget=forms.TimeInput(attrs={"type":"time"}))
    shift_end=forms.TimeField(widget=forms.TimeInput(attrs={"type":"time"}))
class floorsInfo(forms.Form):
    floor_name=forms.CharField(max_length=200,widget=forms.TextInput)
    floor_num=forms.IntegerField(widget=forms.NumberInput)
    floor_description=forms.CharField(widget=forms.Textarea)
class bedsInfo(forms.Form):
    bed_number=forms.IntegerField(widget=forms.NumberInput)
    room_no=forms.IntegerField(widget=forms.NumberInput)
    bed_type=forms.CharField(max_length=200,widget=forms.TextInput)
    floor_number=forms.IntegerField(widget=forms.NumberInput)
    bed_status=forms.CharField(max_length=200,widget=forms.TextInput)
    assigned_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    discharge_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
class appointment(forms.Form):
    patient=forms.CharField(max_length=200,widget=forms.TextInput)
    doctor=forms.CharField(max_length=200,widget=forms.TextInput)
    appointment_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
    appointment_time=forms.TimeField(widget=forms.TimeInput(attrs={"type":"time"}))
    reason_for_visit=forms.CharField(max_length=300,widget=forms.TextInput)
    booked_date=forms.DateField(widget=forms.DateInput(attrs={"type":"date"}))
class medForms(forms.Form):
    medicine_name=forms.CharField(max_length=200,widget=forms.TextInput)
    generic_name=forms.CharField(max_length=200,widget=forms.TextInput)
    category=forms.CharField(max_length=200,widget=forms.TextInput)
    dosage_form=forms.CharField(max_length=200,widget=forms.TextInput)
    strength=forms.CharField(max_length=200,widget=forms.TextInput)
    manufacturer=forms.CharField(max_length=200,widget=forms.TextInput)
    quantity_in_stock=forms.CharField(max_length=200,widget=forms.TextInput)
    unit_price=forms.FloatField(widget=forms.NumberInput)
    expiry_date=forms.CharField(max_length=200,widget=forms.TextInput)
    prescription_required=forms.CharField(widget=forms.Textarea)
    status=forms.CharField(max_length=200,widget=forms.TextInput)
class roomsInfo(forms.Form):
    room_number=forms.IntegerField(widget=forms.NumberInput)
    room_type=forms.CharField(max_length=200,widget=forms.TextInput)
    floor_number=forms.IntegerField(widget=forms.NumberInput)
    department=forms.CharField(max_length=200,widget=forms.TextInput)
    capacity=forms.CharField(max_length=200,widget=forms.TextInput)
    occupied_beds=forms.IntegerField(widget=forms.NumberInput)
    available_beds=forms.CharField(widget=forms.NumberInput)
    room_status=forms.CharField(max_length=200,widget=forms.TextInput)
    daily_charge=forms.CharField(widget=forms.NumberInput)