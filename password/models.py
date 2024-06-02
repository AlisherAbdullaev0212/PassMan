from django.db import models
from django.contrib.auth.models import User


departments = [
    ("Kazakhstan", "Kazakhstan"),
    ("Kyrgyzstan", "Kyrgyzstan"),
    ("Tajikistan", "Tajikistan"),
    ("Turkmenistan", "Turkmenistan"),
    ("Uzbekistan", "Uzbekistan"),
    ("Russian Federation", "Russian Federation"),
]


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to="profile_pic/DoctorProfilePic/", null=True, blank=True
    )
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    department = models.CharField(
        max_length=50, choices=departments, default="Kazakhstan"
    )
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return "{} ({})".format(self.user.first_name, self.department)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to="profile_pic/PatientProfilePic/", null=True, blank=True
    )
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)
    symptoms = models.CharField(max_length=100, null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

    @property
    def get_id(self):
        return self.user.id

    def __str__(self):
        return self.user.first_name + " (" + self.symptoms + ")"


class Appointment(models.Model):
    patientId = models.PositiveIntegerField(null=True)
    doctorId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=40, null=True)
    doctorName = models.CharField(max_length=40, null=True)
    appointmentDate = models.DateField(auto_now=True)
    description = models.TextField(max_length=500)
    status = models.BooleanField(default=False)


class PatientDischargeDetails(models.Model):
    patientId = models.PositiveIntegerField(null=True)
    patientName = models.CharField(max_length=40)
    assignedDoctorName = models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=True)
    symptoms = models.CharField(max_length=100, null=True)

    admitDate = models.DateField(null=False)
    releaseDate = models.DateField(null=False)
    daySpent = models.PositiveIntegerField(null=False)

    roomCharge = models.PositiveIntegerField(null=False)
    medicineCost = models.PositiveIntegerField(null=False)
    doctorFee = models.PositiveIntegerField(null=False)
    OtherCharge = models.PositiveIntegerField(null=False)
    total = models.PositiveIntegerField(null=False)


class FailedLoginAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


from django.db import models
from django.contrib.auth.models import User


class PasswordEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    website = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.website


from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64


class MyEncryptedModel(models.Model):
    encrypted_field = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        key = b"secret_key123456"
        cipher = AES.new(key, AES.MODE_CBC)
        encrypted_data = cipher.encrypt(
            pad(self.encrypted_field.encode(), AES.block_size)
        )
        self.encrypted_field = base64.b64encode(encrypted_data).decode()
        super().save(*args, **kwargs)


# from django.db import models
# from passwordmanagement.neural_network import password_to_vector, label_to_onehot


# class Password(models.Model):
#     password = models.CharField(max_length=100)
#     complexity = models.IntegerField()  # Метка сложности пароля

#     def save(self, *args, **kwargs):
#         self.password_vector = password_to_vector(self.password, max_length=100)
#         self.complexity_onehot = label_to_onehot(self.complexity, num_classes=3)
#         super().save(*args, **kwargs)


# from django.db import models

# class myModel(models.Model):
#     area1 = models.CharField(max_length=100)
#     area2 = models.TextField()

#     def __str__(self):
#         return self.area1
# Create your models here.


class todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_name = models.CharField(max_length=1000)
    status = models.BooleanField(default=False)
    password = models.CharField(max_length=100, blank=True, null=True)
    icon = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.todo_name
