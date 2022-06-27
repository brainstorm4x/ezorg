from django.db import models

# Create your models here.
class Candidate(models.Model):
    gender_choice = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Unknown", "Unknown"),
    )
    
    US_state_choice = (
        ('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')
        )
    
    title = models.CharField(max_length=50)
    candidate_first_name = models.CharField(max_length=50)
    candidate_middle_name = models.CharField(max_length=50, null=True, blank=True)
    candidate_last_name = models.CharField(max_length=50)
    candidate_gender = models.CharField(max_length=10, choices=gender_choice, default="Unknown")
    candidate_date_of_birth = models.DateField()
    candidate_SSN = models.PositiveIntegerField()
    candidate_street_address = models.CharField(max_length=225)
    candidate_city = models.CharField(max_length=50)
    candidate_state = models.CharField(max_length=100, choices=US_state_choice)
    candidate_zipcode = models.IntegerField()
    candidate_alt_zipcode = models.IntegerField()