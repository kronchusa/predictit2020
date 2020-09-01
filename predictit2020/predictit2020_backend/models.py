from django.db import models

from django.contrib.auth.models import User


class Prediction(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='prediction')

    electoral_votes_dem = models.IntegerField(default=0)
    electoral_votes_rep = models.IntegerField(default=0)
    AL = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    AK = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    AZ = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    AR = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    CA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    CO = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    CT = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    DC2 = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    DE = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    FL = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    GA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    HI = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    IDA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    IL = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    IN = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    IA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    KS = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    KY = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    LA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    ME = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    MD = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    MA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    MI = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    MN = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    MS = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    MO = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    MT = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    NE = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    NV = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    NH = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    NJ = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    NM = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    NY = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    NC = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    ND = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    OH = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    OK = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    OR = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    PA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    RI = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    SC = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    SD = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    TN = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    TX = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    UT = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    VT = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    VA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    WA = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    WV = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    WI = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)
    WY = models.CharField(max_length=1, choices=(('d', 'Democrat'), ('r', 'Republican')), null=True, blank=True)

    number_correct = models.IntegerField(default=0, null=True)

    excluded_fields = ['user', 'electoral_votes_dem', 'electoral_votes_rep', 'id', 'number_correct']

    @staticmethod
    def remove_all_non_state_fields(all_fields: set):
        all_fields.remove('id')
        all_fields.remove('electoral_votes_rep')
        all_fields.remove('electoral_votes_dem')
        all_fields.remove('user')
        all_fields.remove('number_correct')

    @staticmethod
    def modify_state_names(all_fields: dict):
        all_fields['DC'] = all_fields.pop('DC2')
        all_fields['ID'] = all_fields.pop('IDA')

    @staticmethod
    def state_percentages(state: str) -> dict:
        all_predictions = Prediction.objects.all()
        state_democrat = 0
        state_republican = 0
        for prediction in all_predictions:
            if not hasattr(prediction, state):
                return None

            attr = getattr(prediction, state)
            if attr == "d":
                state_democrat += 1
            if attr == "r":
                state_republican += 1

        total = state_democrat + state_republican
        return {'d': (state_democrat / total) * 100, 'r': (state_republican / total) * 100}

    @staticmethod
    def all_state_percentages():
        all_fields = set(p.name for p in Prediction._meta.get_fields())

        Prediction.remove_all_non_state_fields(all_fields)

        all_states = {}

        all_democrat_percentages = 0.0
        all_republican_percentages = 0.0

        for field in all_fields:
            all_states[field] = Prediction.state_percentages(field)
            all_democrat_percentages += all_states[field]['d']
            all_republican_percentages += all_states[field]['r']

        Prediction.modify_state_names(all_states)
        sorted_all_states = sorted(all_states.items(), key=lambda state: state[0])

        return {
            'all_states': sorted_all_states,
            'total_democrat': all_democrat_percentages / 51,
            'total_republican': all_republican_percentages / 51
        }

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

