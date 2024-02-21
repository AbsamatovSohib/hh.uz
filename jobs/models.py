from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
class District(BaseModel):
    title = models.CharField(max_length=63)
    neighbour = models.ManyToManyField("self")


class Experience(BaseModel):
    NOEX = "NOEX","No experience"
    ONETHREE = "Onethree","One untill three"
    THREESIX = "Threesix","three untill six"
    MORESIX = "Moresix", "More than six"


class Speciality(models.Model):
    title = models.CharField()


class SpecialityTypes(models.Model):
    title = models.CharField(max_length=63)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE)


class Company(models.Model):
    title = models.CharField(max_length=127)
    image = models.ImageField(upload_to="images/company")


class EmploymentType(models.TextChoices):
    FE = "FE", "Full employment"
    PE = "PE", "Part-time employment"
    PS = "PS", "Project based salary"
    VL = "VL", "Voluntorior"
    IN = "IN", "Internship"


class Education(models.TextChoices):
    NOTREQ = "NOTREQ", "Not required"
    HIGHER = "HIGHER", "Higher"
    SECONVAC = "SECONVAC","secondary vacational"


class PartTimeJob(BaseModel):
    title = models.CharField(max_length=128, default="evenings")


class Schedule(BaseModel):
    title = models.CharField(max_length=127, default="Full day")


class JobOffer(BaseModel):
    title = models.CharField(max_length=64)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name="district")

    from_price = models.PositiveIntegerField(null=True, blank=True)
    to_price = models.PositiveIntegerField(null=True, blank=True)

    experince = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name="expirence")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="company")

    speciality = models.ForeignKey(SpecialityTypes, models.CASCADE, related_name="speciality")
    education = models.ForeignKey(Education.choices, default="NR", related_name="education")
    employment_type = models.ForeignKey(EmploymentType.choices, default="FE")

    part_time_job = models.ForeignKey(PartTimeJob, models.CASCADE, related_name="part_time")
