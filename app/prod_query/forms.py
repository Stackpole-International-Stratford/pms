import datetime
from django import forms
from django.core.exceptions import ValidationError

class MultiStringListField(forms.Field):
  def to_python(self, value):
    if not value:
      return []
    return value.split(',')

  def validate(self, value):
    pass


class ShiftLineForm(forms.Form):
  CHOICES = [
    ('50-8670', 'AB1V Reaction Gas'),
    ('50-5401', 'AB1V Input Gas'),
    ('50-5404', 'AB1V OverDrive Gas'),
    ('50-3214', '10R140 Gas'),
    ('50-5214', '10R140 Diesel'),
  ]
  line = forms.ChoiceField(choices=CHOICES)
  # start_date = DatePickerInput()
  # end_date = DatePickerInput(range_from="start_date")
  # start_time = TimePickerInput()
  # end_time = TimePickerInput(range_from="start_time")

class MachineInquiryForm(forms.Form):
  CHOICES = [
    (1, '10pm - 6am'),
    (2, '11pm - 7am'),
    (3, '6am - 2pm'),
    (4, '7am - 3pm'),
    (5, '2pm - 10pm'),
    (6, '3pm - 11pm'),
    (7, '6am - 6am'),
    (8, '7am - 7am'),
  ]

  machines = MultiStringListField(
    required=False,
    widget=forms.TextInput(attrs={"title":"A comma seperated list of Machine numbers"})
  )
  parts = MultiStringListField(
    required=False,
    widget=forms.TextInput(attrs={"title":"A comma seperated list of Asset numbers"})
  )
  inquiry_date = forms.DateField(initial=datetime.date.today)
  times = forms.ChoiceField(choices=CHOICES)

  def clean(self):
    cleaned_data = super().clean()
    machines = cleaned_data.get("machines")
    parts = cleaned_data.get("parts")

    if not parts and not machines:
      # Only do something if both fields are not present.
      raise ValidationError(
          "You need to specify at least one machine or part number"
      )