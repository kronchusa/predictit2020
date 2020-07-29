from django.db import models

from django.contrib.auth.models import User


class Prediction(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='prediction')

    electoral_votes_dem = models.IntegerField()
    electoral_votes_rep = models.IntegerField()
    AL = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    AK = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    AZ = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    AR = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    CA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    CO = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    CT = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    DC2 = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    DE = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    FL = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    GA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    HI = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    IDA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    IL = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    IN = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    IA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    KS = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    KY = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    LA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    ME = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    MD = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    MA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    MI = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    MN = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    MS = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    MO = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    MT = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    NE = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    NV = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    NH = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    NJ = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    NM = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    NY = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    NC = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    ND = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    OH = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    OK = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    OR = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    PA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    RI = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    SC = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    SD = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    TN = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    TX = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    UT = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    VT = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    VA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    WA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    WV = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    WI = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))
    WY = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')))

    number_correct = models.IntegerField(default=0, null=True)

    excluded_fields = ['user', 'electoral_votes_dem', 'electoral_votes_rep', 'id', 'number_correct']

    def calculate_number_of_states_right(self):
        counter = 0
        actual = Prediction.objects.filter(user__username='actual').first()
        if not actual:
            self.number_correct = counter
            self.save()
            return

        self_all_fields = self._meta.fields
        actual_all_fields = actual._meta.fields

        for self_field, actual_field in zip(self_all_fields, actual_all_fields):
            if not self_field.name in self.excluded_fields:
                if getattr(self, self_field.name) == getattr(actual, actual_field.name):
                   counter += 1

        self.number_correct = counter
        self.save()

    def is_winner(self):
        if self.number_correct:
            return self.number_correct % 51 == 0
        else:
            return False

    def __str__(self):
        return f"{self.user.username}'s prediction"


class DeclareWinners(models.Model):
    pass

