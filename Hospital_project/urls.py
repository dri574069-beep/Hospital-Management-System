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
from Hospital_app.views import user_login,savePass,patientData,getData,patientdataForms,importantPatientData,home,doctorsInfoForms,savingDoctorPerData,makingDoctorsForms,saveDoctorInfos,create_admin,getAdminData,check_data,show_docData,dep_forms,savingDepInfo,ShowDocsInfo,showDepartmentInfo,makeDoctorsForms,fetchRecapPerInfo,fetchnorrecepdata,saveSimrecepData,ShowReceoOerData,makeambforms,addAmNorInfo,saveamNorInfo,getAmbukancesInfo,enterNurseInfo,showNurseInfo,makeNurseEmployForms,FloorInfo,showFloorInfo,bedsInfoForms,showbedsInfo,AppointmentForms,showappointinfo,medInfoForms,checkpass,roomsForm,showroomInfo,patient,showappointmentforadmin,showdocsinfo,patientinfotpadmin,showhospital
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',user_login,name="user_login"),
    path('savePass/',savePass,name="savePass"),
    path('home/',home,name="home"),
    path('getAdminData/',getAdminData,name="getAdminData"),
    path('check_data/',check_data,name="check_data"),
    path('show_docData/',show_docData,name="show_docData"),
    path('doctorsInfoForms/',doctorsInfoForms,name="doctorsInfoForms"),
    path('saveDoctorInfos/',saveDoctorInfos,name="saveDoctorInfos"),
    path('makingDoctorsForms/',makingDoctorsForms,name="makingDoctorsForms"),
    path('savingDoctorPerData/',savingDoctorPerData,name="savingDoctorPerData"),
    path('dep_forms/',dep_forms,name="dep_forms"),
    path('savingDepInfo/',savingDepInfo,name="savingDepInfo"),
    path('ShowDocsInfo/<int:id>/',ShowDocsInfo,name="ShowDocsInfo"),
    path('makeDoctorsForms/',makeDoctorsForms,name="makeDoctorsForms"),
    path('showDepartmentInfo/<str:department_name>/',showDepartmentInfo,name="showDepartmentInfo"),
    path('fetchRecapPerInfo/',fetchRecapPerInfo,name="fetchRecapPerInfo"),
    path('fetchnorrecepdata/',fetchnorrecepdata,name="fetchnorrecepdata"),
    path('saveSimrecepData/',saveSimrecepData,name="saveSimrecepData"),
    path('ShowReceoOerData/',ShowReceoOerData,name="ShowReceoOerData"),
    path('makeambforms/',makeambforms,name="makeambforms"),
    path('addAmNorInfo/',addAmNorInfo,name="addAmNorInfo"),
    path('saveamNorInfo/',saveamNorInfo,name="saveamNorInfo"),
    path('getAmbukancesInfo/',getAmbukancesInfo,name="getAmbukancesInfo"),
    path('enterNurseInfo/',enterNurseInfo,name="enterNurseInfo"),
    path('showNurseInfo/',showNurseInfo,name="showNurseInfo"),
    path('makeNurseEmployForms/',makeNurseEmployForms,name="makeNurseEmployForms"),
    path('FloorInfo/',FloorInfo,name="FloorInfo"),
    path('showFloorInfo/',showFloorInfo,name="showFloorInfo"),
    path('bedsInfoForms/',bedsInfoForms,name="bedsInfoForms"),
    path('showbedsInfo/',showbedsInfo,name="showbedsInfo"),
    path('AppointmentForms/',AppointmentForms,name="AppointmentForms"),
    path('showappointinfo/',showappointinfo,name="showappointinfo"),
    path('medInfoForms/',medInfoForms,name="medInfoForms"),
    path('checkpass/',checkpass,name="checkpass"),
    path('roomsForm/',roomsForm,name="roomsForm"),
    path('showroomInfo/',showroomInfo,name="showroomInfo"),
    path('patientData/',patientData,name="patientData"),
    path('getData/',getData,name="getData"),
    path('patientdataForms/',patientdataForms,name="patientdataForms"),
    path('importantPatientData/',importantPatientData,name="importantPatientData"),
    path('create_admin/',create_admin,name="create_admin"),
    path('patient/',patient,name="patient"),
    path('showappointmentforadmin/',showappointmentforadmin,name='showappointmentforadmin'),
    path('showdocsinfo/',showdocsinfo,name="showdocsinfo"),
    path('patientinfotpadmin/',patientinfotpadmin,name="patientinfotpadmin"),
    path('showhospital/',showhospital,name="showhospital"),
    ]




