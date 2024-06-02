from passwordmanagement.bruteforce import BruteForceMiddleware
from django.contrib import admin
from django.urls import path
from password import views
from django.contrib.auth.views import LoginView, LogoutView


# -------------FOR ADMIN RELATED URLS
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_view, name=""),
    path("aboutus", views.aboutus_view),
    path("contactus", views.contactus_view),
    path("adminclick", views.adminclick_view),
    path("managerclick", views.doctorclick_view),
    path("userclick", views.patientclick_view),
    path("adminsignup", views.admin_signup_view),
    path("managersignup", views.doctor_signup_view, name="doctorsignup"),
    path("usersignup", views.patient_signup_view),
    path("adminlogin", views.CustomLoginView.as_view(), name="adminlogin"),
    path("adminlogin", LoginView.as_view(template_name="password/adminlogin.html")),
    path("managerlogin", LoginView.as_view(template_name="password/doctorlogin.html")),
    path("userlogin", LoginView.as_view(template_name="password/patientlogin.html")),
    path("afterlogin", views.afterlogin_view, name="afterlogin"),
    path(
        "logout", LogoutView.as_view(template_name="password/index.html"), name="logout"
    ),
    path("admin-dashboard", views.admin_dashboard_view, name="admin-dashboard"),
    path("admin-manager", views.admin_doctor_view, name="admin-doctor"),
    path("admin-view-manager", views.admin_view_doctor_view, name="admin-view-doctor"),
    path(
        "delete-doctor-from-hospital/<int:pk>",
        views.delete_doctor_from_hospital_view,
        name="delete-doctor-from-hospital",
    ),
    path("update-manager/<int:pk>", views.update_doctor_view, name="update-doctor"),
    path("admin-add-manager", views.admin_add_doctor_view, name="admin-add-doctor"),
    path(
        "admin-approve-manager",
        views.admin_approve_doctor_view,
        name="admin-approve-doctor",
    ),
    path("approve-doctor/<int:pk>", views.approve_doctor_view, name="approve-doctor"),
    path("reject-doctor/<int:pk>", views.reject_doctor_view, name="reject-doctor"),
    path(
        "admin-view-manager-country",
        views.admin_view_doctor_specialisation_view,
        name="admin-view-doctor-specialisation",
    ),
    path("admin-user", views.admin_patient_view, name="admin-patient"),
    path("admin-view-user", views.admin_view_patient_view, name="admin-view-patient"),
    path(
        "delete-patient-from-hospital/<int:pk>",
        views.delete_patient_from_hospital_view,
        name="delete-patient-from-hospital",
    ),
    path("update-user/<int:pk>", views.update_patient_view, name="update-patient"),
    path("admin-add-user", views.admin_add_patient_view, name="admin-add-patient"),
    path(
        "admin-approve-user",
        views.admin_approve_patient_view,
        name="admin-approve-patient",
    ),
    path(
        "approve-patient/<int:pk>", views.approve_patient_view, name="approve-patient"
    ),
    path("reject-patient/<int:pk>", views.reject_patient_view, name="reject-patient"),
    path(
        "admin-discharge-user",
        views.admin_discharge_patient_view,
        name="admin-discharge-patient",
    ),
    path(
        "discharge-user/<int:pk>",
        views.discharge_patient_view,
        name="discharge-patient",
    ),
    path("download-pdf/<int:pk>", views.download_pdf_view, name="download-pdf"),
    path("admin-appointment", views.admin_appointment_view, name="admin-appointment"),
    path(
        "admin-view-appointment",
        views.admin_view_appointment_view,
        name="admin-view-appointment",
    ),
    path(
        "admin-add-appointment",
        views.admin_add_appointment_view,
        name="admin-add-appointment",
    ),
    path(
        "admin-approve-appointment",
        views.admin_approve_appointment_view,
        name="admin-approve-appointment",
    ),
    path(
        "approve-appointment/<int:pk>",
        views.approve_appointment_view,
        name="approve-appointment",
    ),
    path(
        "reject-appointment/<int:pk>",
        views.reject_appointment_view,
        name="reject-appointment",
    ),
]


# ---------FOR DOCTOR RELATED URLS-------------------------------------
urlpatterns += [
    path("manager-dashboard", views.doctor_dashboard_view, name="doctor-dashboard"),
    path("search", views.search_view, name="search"),
    path("manager-user", views.doctor_patient_view, name="doctor-patient"),
    path(
        "manager-view-user",
        views.doctor_view_patient_view,
        name="doctor-view-patient",
    ),
    path(
        "manager-view-discharge-user",
        views.doctor_view_discharge_patient_view,
        name="doctor-view-discharge-patient",
    ),
    path(
        "manager-appointment", views.doctor_appointment_view, name="doctor-appointment"
    ),
    path(
        "manager-view-appointment",
        views.doctor_view_appointment_view,
        name="doctor-view-appointment",
    ),
    path(
        "manager-delete-appointment",
        views.doctor_delete_appointment_view,
        name="doctor-delete-appointment",
    ),
    path(
        "delete-appointment/<int:pk>",
        views.delete_appointment_view,
        name="delete-appointment",
    ),
]


# ---------FOR USER RELATED URLS-------------------------------------
urlpatterns += [
    path("user-dashboard", views.patient_dashboard_view, name="patient-dashboard"),
    path(
        "user-appointment",
        views.patient_appointment_view,
        name="patient-appointment",
    ),
    path(
        "user-book-appointment",
        views.patient_book_appointment_view,
        name="patient-book-appointment",
    ),
    path(
        "user-view-appointment",
        views.patient_view_appointment_view,
        name="patient-view-appointment",
    ),
    path(
        "user-view-manager",
        views.patient_view_doctor_view,
        name="patient-view-doctor",
    ),
    path(
        "user_generate",
        views.patient_generate_view,
        name="patient_generate",
    ),
    path(
        "all_data",
        views.all_data_view,
        name="all_data",
    ),
    path("delete-task/<str:name>/", views.DeleteTask, name="delete"),
    path("update/<str:name>/", views.Update, name="update"),
    path("searchmanager", views.search_doctor_view, name="searchdoctor"),
    path("user-discharge", views.patient_discharge_view, name="patient-discharge"),
]
