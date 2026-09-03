"""
URL configuration for Hospital_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Hospital_app.views import user_login,patientData,getData,patientdataForms,importantPatientData,home,doctorsInfoForms,savingDoctorPerData,makingDoctorsForms,saveDoctorInfos,getAdminData,show_docData,dep_forms,savingDepInfo,ShowDocsInfo,showDepartmentInfo,fetchRecapPerInfo,fetchnorrecepdata,saveSimrecepData,ShowReceoOerData,makeambforms,addAmNorInfo,saveamNorInfo,getAmbukancesInfo,enterNurseInfo,showNurseInfo,makeNurseEmployForms,FloorInfo,showFloorInfo,bedsInfoForms,showbedsInfo,AppointmentForms,showappointinfo,medInfoForms,checkpass,roomsForm,showroomInfo,patient,showappointmentforadmin,showdocsinfo,patientinfotpadmin,showhospital,deletePatient,deletePatientContactInfo,deleteEmPatient,deletePatientMedInfos,deleteNursesData,deleteBurseCOntactInfo,deleteNurseEmpInfo,deleteNursesWorkInfo,deleteBedsInfo,deleteAppointmentsInfo,deleteRoomsInfos,delFloorsInfo,delRecepInfo,delRecepConInfo,deleteRecepEmpInfo,delAmb,delDep,delDoctor,showMeds,showroomInfo,recephome,ambHome,NurseHome,floorsHome,bedhome,medsHome,roomshome,hospitalHistory,deletemeds,create_admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_login,name="user_login"),
    # path('savePass/',savePass,name="savePass"),
    path('home/',home,name="home"),
    path('getAdminData/',getAdminData,name="getAdminData"),
    path('hospitalHistory',hospitalHistory,name="hospitalHistory"),
    path('show_docData/',show_docData,name="show_docData"),
    path('doctorsInfoForms/',doctorsInfoForms,name="doctorsInfoForms"),
    path('saveDoctorInfos/',saveDoctorInfos,name="saveDoctorInfos"),
    path('makingDoctorsForms/<int:id>/',makingDoctorsForms,name="makingDoctorsForms"),
    path('savingDoctorPerData/',savingDoctorPerData,name="savingDoctorPerData"),
    path('create_admin/',create_admin,name="create_admin"),
    path('dep_forms/',dep_forms,name="dep_forms"),
    path('savingDepInfo/',savingDepInfo,name="savingDepInfo"),
    path('ShowDocsInfo/<int:id>/',ShowDocsInfo,name="ShowDocsInfo"),
    path('showDepartmentInfo/<str:department_name>/',showDepartmentInfo,name="showDepartmentInfo"),
    path('fetchRecapPerInfo/',fetchRecapPerInfo,name="fetchRecapPerInfo"),
    path('fetchnorrecepdata/<int:id>/',fetchnorrecepdata,name="fetchnorrecepdata"),
    path('saveSimrecepData/',saveSimrecepData,name="saveSimrecepData"),
    path('ShowReceoOerData/<int:id>/',ShowReceoOerData,name="ShowReceoOerData"),
    path('makeambforms/',makeambforms,name="makeambforms"),
    path('addAmNorInfo/<int:id>/',addAmNorInfo,name="addAmNorInfo"),
    path('saveamNorInfo/',saveamNorInfo,name="saveamNorInfo"),
    path('getAmbukancesInfo/<int:id>/',getAmbukancesInfo,name="getAmbukancesInfo"),
    # path('allAmb/',allAmb,name="allAmb"),
    path('enterNurseInfo/',enterNurseInfo,name="enterNurseInfo"),
    path('showNurseInfo/<int:id>/',showNurseInfo,name="showNurseInfo"),
    path('makeNurseEmployForms/<int:id>/',makeNurseEmployForms,name="makeNurseEmployForms"),
    # path('allNurses/',allNurses,name="allNurses"),
    path('FloorInfo/',FloorInfo,name="FloorInfo"),
    path('showFloorInfo/<int:id>/',showFloorInfo,name="showFloorInfo"),
    path('bedsInfoForms/',bedsInfoForms,name="bedsInfoForms"),
    path('showbedsInfo/<int:id>/',showbedsInfo,name="showbedsInfo"),
    path('AppointmentForms/',AppointmentForms,name="AppointmentForms"),
    path('showappointinfo/',showappointinfo,name="showappointinfo"),
    path('medInfoForms/',medInfoForms,name="medInfoForms"),
    path('checkpass/',checkpass,name="checkpass"),
    path('roomsForm/',roomsForm,name="roomsForm"),
    path('showroomInfo/<int:id>/',showroomInfo,name="showroomInfo"),
    path('patientData/',patientData,name="patientData"),
    path('getData/',getData,name="getData"),
    path('patientdataForms/<int:id>/',patientdataForms,name="patientdataForms"),
    path('patient/',patient,name="patient"),
    path('showappointmentforadmin/',showappointmentforadmin,name='showappointmentforadmin'),
    path('showdocsinfo/',showdocsinfo,name="showdocsinfo"),
    path('patientinfotpadmin/',patientinfotpadmin,name="patientinfotpadmin"),
    path('showhospital/',showhospital,name="showhospital"),
    path('deletePatient/',deletePatient,name="deletePatient"),
    path('deletePatientContactInfo/',deletePatientContactInfo,name="deletePatientContactInfo"),
    path('deleteEmPatient/',deleteEmPatient,name="deleteEmPatient"),
    path('deletePatientMedInfos/',deletePatientMedInfos,name="deletePatientMedInfos"),
    path('deleteNursesData/',deleteNursesData,name="deleteNursesData"),
    path('deleteBurseCOntactInfo/',deleteBurseCOntactInfo,name="deleteBurseCOntactInfo"),
    path("deleteNurseEmpInfo/",deleteNurseEmpInfo,name="deleteNurseEmpInfo"),
    path('deleteNursesWorkInfo/',deleteNursesWorkInfo,name='deleteNursesWorkInfo'),
    path('deleteBedsInfo/',deleteBedsInfo,name="deleteBedsInfo"),
    path('deleteAppointmentsInfo/',deleteAppointmentsInfo,name="deleteAppointmentsInfo"),
    path('deleteRoomsInfos/',deleteRoomsInfos,name="deleteRoomsInfos"),
    path('delFloorsInfo/',delFloorsInfo,name="delFloorsInfo"),
    path('delRecepInfo/',delRecepInfo,name="delRecepInfo"),
    path('delRecepConInfo/',delRecepConInfo,name="delRecepConInfo"),
    path('deleteRecepEmpInfo/',deleteRecepEmpInfo,name="deleteRecepEmpInfo"),
    path('delAmb/',delAmb,name="delAmb"),
    path('delDep/',delDep,name="delDep"),
    path('delDoctor/',delDoctor,name="delDoctor"),
    path('showMeds/<int:id>/',showMeds,name="showMeds"),
    path('showroomInfo/<int:id>/',showroomInfo,name="showroomInfo"),
    path('recephome/',recephome,name="recephome"),
    path('ambHome/',ambHome,name="ambHome"),
    path('NurseHome/',NurseHome,name="NurseHome"),
    path('floorsHome/',floorsHome,name="floorsHome"),
    path('bedhome/',bedhome,name="bedhome"),
    path('medsHome/',medsHome,name="medsHome"),
    path('roomshome/',roomshome,name="roomshome"),
    path('deletemeds/',deletemeds,name="deletemeds"),
    ]




