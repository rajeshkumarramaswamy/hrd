from django.shortcuts import render, render_to_response
from edata.forms import EmpForm
from . import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
import MySQLdb
import simplejson
from django.contrib import messages
from edata.models import *
from edata.tables import NrStaffTable
from django_tables2.config import RequestConfig


def index(request):
    total_nr_departments = []
    total_nr_groups = []
    total_nr_staff = []
    emp_list = []

    conn, cursor = mysql_connection()
    query1 = 'select count(*) from nr_departments'
    cursor.execute(query1)
    tnd = cursor.fetchall()
    total_nr_departments = tnd[0][0]

    query2 = 'select count(*) from nr_groups'
    cursor.execute(query2)
    tng = cursor.fetchall()
    total_nr_groups = tng[0][0]

    query3 = 'select count(*) from nr_staff'
    cursor.execute(query3)
    tns = cursor.fetchall()
    total_nr_staff = tns[0][0]

    query4 = 'select user_name from nr_staff'
    cursor.execute(query4)
    els = cursor.fetchall()
    #import pdb; pdb.set_trace()
    for name in els:
        emp_list.append(name[0])
    return render(request, 'index.html', { 'total_nr_departments': total_nr_departments, 'total_nr_groups': total_nr_groups,
                                           'total_nr_staff': total_nr_staff, 'emp_list' : emp_list })


def emp_form(request):
    form = forms.EmpForm()
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            employee_id = form.cleaned_data.get('employee_id')
            messages.add_message(request, messages.SUCCESS, "Employee Details successfully saved.")
            return HttpResponseRedirect(reverse('empform'))
        else:
            form = EmpForm()
    return render(request, 'employee_form.html', {'form': form})

def mysql_connection(db_name='empdata'):
    conn = MySQLdb.connect(db=db_name, host='localhost', user='root', passwd='python@123')
    cursor = conn.cursor()
    return conn, cursor

def mysearch(request):
    selected = request.GET.get('search')
    conn, cursor = mysql_connection()
    query = 'SELECT * from nr_staff WHERE user_name = %s;' % selected
    cursor.execute(query)
    cursor.fetchall()
    return HttpResponse(simplejson.dumps({'status': mysearch  }), content_type="application/json")


def employee_list(request):
    employee = request.GET.get('suggestion', '')
    conn, cursor = mysql_connection()
    query_emp = 'SELECT id, employee_number, employee_id, user_name, pwd, staff_fname, staff_lname, staff_email, staff_alternate_email, dept_id, roster_id, grp_id, desig_id, swstaff_id, staff_resource_type, is_admin, is_ad_admin, nocid, manupulate_staff_roster, alltickets_acess, is_active, is_found, reporting_manager_id, date_of_join, phone_number, skype_id, alternate_number, phone_priority, escalation_adm, is_ic_admin, is_tb_admin, total_exp, is_mngr_dboard_access, sdmtracker_access, hrdata_access FROM nr_staff WHERE user_name = %s' %(employee)
    cursor.execute(query_emp)
    emp_list = cursor.fetchall()
    return HttpResponse(simplejson.dumps({'dtable': emp_list}), content_type="application/json")

'''def table_emp_list(request):
    conn, cursor = mysql_connection()
    query = 'select id, employee_number, employee_id, user_name, staff_email, nocid, reporting_manager_id, date_of_join, phone_number, skype_id from nr_staff;'
    cursor.execute(query)
    emp = NrStaffTable(NrStaff.objects.only('user_name'))
    RequestConfig(request, paginate={'per_page': 10}).configure(emp)
    return render(request, 'employee-list.html', { 'emp' : emp })'''


def emp_edit_form(request, emp_id):
    if request.POST:
        form = EmpForm(request.POST)

    if form.is_valid():
        emp = NrStaff.objects.get(pk=emp_id)
        form = EmpForm(request.POST, instance = emp)
        form.save()
        return HttpResponseRedirect('/emp_form/')
    else:
        emp = NrStaff.objects.get(pk = emp_id)
        form = EmpForm(instance=emp)
        return render_to_response('edit_emp_form.html',{ 'form': form })



