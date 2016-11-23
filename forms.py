from django import forms
from django.core import validators

class EmpForm(forms.Form):
    employee_number = forms.IntegerField(required=False)
    employee_id = forms.IntegerField(required=True)
    user_name = forms.CharField()
    staff_fname = forms.CharField()
    staff_lname = forms.CharField()
    staff_email = forms.EmailField()
    staff_alternate_email = forms.EmailField()
    roster_id = forms.IntegerField(required=True)
    desig_id = forms.IntegerField()
    swstaff_id = forms.IntegerField()
    staff_resource_type = forms.IntegerField()
    is_admin = forms.IntegerField()
    is_ad_admin = forms.IntegerField()
    nocid = forms.IntegerField()
    manupulate_staff_roster = forms.IntegerField()
    alltickets_acess = forms.IntegerField()
    is_active = forms.IntegerField()
    is_found = forms.IntegerField()
    reporting_manager_id = forms.IntegerField()
    date_of_join = forms.DateField()
    phone_number = forms.CharField()
    skype_id = forms.CharField()
    escalation_adm = forms.IntegerField()
    is_tb_admin = forms.IntegerField()
    is_ic_admin = forms.IntegerField()
    total_exp = forms.FloatField()
    is_mngr_dboard_access = forms.IntegerField()

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        if not user_name:
            raise forms.ValidationError('Please fill the Username.')
        return user_name

    def clean_employee_id(self):
        employee_id = self.cleaned_data.get('employee_id')
        if not employee_id:
            raise forms.ValidationError('Please fill')
        return employee_id



