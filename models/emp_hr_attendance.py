from odoo import fields,models,api
from datetime import datetime

class Hrattendance(models.Model):

    # _name ="emp.attendance"
    _inherit = "hr.employee"
    _description ="employee attendance"
   

    emp_attendance_ids = fields.One2many("emp.attendance","employee_name_id",string="Attendance")
    


   #button method for add
    def add_attendance_button(self):
        for employee in self:
            
            self.add_attendance(employee.id, fields.Datetime.now())

    #button method for update 
    def update_attendance_button(self):
        for employee in self:
            if employee.emp_attendance_ids:
               
                attendance_record = employee.emp_attendance_ids[0] #first record updated
                self.update_attendance(employee.id, attendance_record.id, fields.Datetime.now())

    #method for delete record
    def delete_attendance_button(self):
         for employee in self:
              if employee.emp_attendance_ids:
                   
                   attendance_record = employee.emp_attendance_ids[0]
                   self.unlink_attendance(employee.id,attendance_record.id)

    
    def add_attendance(self, employee_id, check_in_time):       
        employee = self.env['hr.employee'].browse(employee_id)
        new_attendance = {
            'employee_name_id': employee_id,
            'check_in_time': check_in_time
        }
        employee.emp_attendance_ids = [(0, 0, new_attendance)]
        print("Attendance record added for employee <<<<<<<<<<")



    def update_attendance(self, employee_id, attendance_id, check_in_time):
            employee = self.env['hr.employee'].browse(employee_id)
            print("employee update attendance<<<<<<,",employee)
            updated_attendance = {
                'check_in_time': check_in_time
            }
            employee.emp_attendance_ids = [(1, attendance_id, updated_attendance)]
            print("Attendance record updated for employee ")
            

    def unlink_attendance(self,employee_id,attendance_id):
         
         employee = self.env['hr.employee'].browse(employee_id)
         print("unlink attendance<<<<<<<<<",employee)

         employee.emp_attendance_ids = [3,attendance_id]