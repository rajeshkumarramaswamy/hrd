from models import NrStaff
from table import Table
from table.columns import Column
import django_tables2 as tables


class NrStaffTable(tables.Table):
    employee_number = tables.Column()
    employee_id = tables.Column()
    Employee = tables.Column()
    staff_fname = tables.Column()
    staff_lname = tables.Column()
    staff_email = tables.Column()
    staff_alternate_email = tables.Column()
    dept = tables.Column()
    roster_id = tables.Column()
    grp = tables.Column()
    desig_id = tables.Column()
    swstaff_id = tables.Column()
    staff_resource_type = tables.Column()
    is_admin = tables.Column()
    is_ad_admin = tables.Column()
    nocid = tables.Column()
    manupulate_staff_roster = tables.Column()
    alltickets_acess = tables.Column()
    is_active = tables.Column()
    is_found = tables.Column()
    reporting_manager_id = tables.Column()
    date_of_join = tables.Column()
    phone_number = tables.Column()
    skype_id = tables.Column()
    escalation_adm = tables.Column()
    is_tb_admin = tables.Column()
    is_ic_admin = tables.Column()
    total_exp = tables.Column()
    is_mngr_dboard_access = tables.Column()

    class Meta:
        model = NrStaff
        ajax = True
