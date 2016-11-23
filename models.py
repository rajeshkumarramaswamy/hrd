from __future__ import unicode_literals

from django.db import models

from django.db import models

class NrDepartments(models.Model):
    dept_name = models.CharField(unique=True, max_length=50)
    dept_desc = models.CharField(max_length=45, blank=True, null=True)
    nocid = models.IntegerField()
    is_roster = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = 'nr_departments'


class NrGroups(models.Model):
    grp_name = models.CharField(unique=True, max_length=10)
    grp_desc = models.CharField(max_length=50)
    nocid = models.IntegerField()

    class Meta:
        db_table = 'nr_groups'


class NrStaff(models.Model):
    employee_number = models.SmallIntegerField(blank=True, null=True)
    employee_id = models.CharField(max_length=10, blank=True, null=True)
    user_name = models.CharField(unique=True, max_length=150, blank=True, null=True)
    pwd = models.CharField(max_length=100, blank=True, null=True)
    staff_fname = models.CharField(max_length=25)
    staff_lname = models.CharField(max_length=25)
    staff_email = models.CharField(unique=True, max_length=82)
    staff_alternate_email = models.CharField(max_length=82, blank=True, null=True)
    dept = models.ForeignKey(NrDepartments, models.DO_NOTHING)
    roster_id = models.IntegerField(blank=True, null=True)
    grp = models.ForeignKey(NrGroups, models.DO_NOTHING)
    desig_id = models.IntegerField(blank=True, null=True)
    swstaff_id = models.IntegerField(blank=True, null=True)
    staff_resource_type = models.IntegerField()
    is_admin = models.IntegerField()
    is_ad_admin = models.IntegerField(blank=True, null=True)
    nocid = models.IntegerField()
    manupulate_staff_roster = models.IntegerField(blank=True, null=True)
    alltickets_acess = models.IntegerField(blank=True, null=True)
    is_active = models.SmallIntegerField(blank=True, null=True)
    is_found = models.SmallIntegerField(blank=True, null=True)
    reporting_manager_id = models.IntegerField(blank=True, null=True)
    date_of_join = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    skype_id = models.CharField(max_length=50, blank=True, null=True)
    escalation_adm = models.IntegerField(blank=True, null=True)
    is_tb_admin = models.IntegerField(blank=True, null=True)
    is_ic_admin = models.IntegerField(blank=True, null=True)
    total_exp = models.FloatField(blank=True, null=True)
    is_mngr_dboard_access = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'nr_staff'
