import base64

from odoo import fields,models,api
from datetime import datetime, timedelta
from odoo.tools import pdf

class Empattendance(models.Model):

    _name ="emp.attendance"
    _inherit=['mail.thread']
    _rec_name ="employee_name_id"
    _description ="employee attendance"
   

    employee_name_id = fields.Many2one("hr.employee",string="Employee",required=True)
    check_in_time = fields.Datetime(string="Check In",required=True)
    check_out_time = fields.Datetime(string="Check out")
    total_hours = fields.Float(string="Total hours",compute="_compute_total_hours",store=False)
    name=fields.Char(string="name")
  

    @api.depends('check_in_time', 'check_out_time')
    def _compute_total_hours(self):
        for record in self:
            if record.check_in_time and record.check_out_time:
                time_diff = record.check_out_time - record.check_in_time
                record.total_hours = time_diff.total_seconds() / 3600
                
            # else:
            #     record.total_hours = 0.0

  
    # server action method 
    def action_check_out(self):
        # for rec in self:
        #     if not rec.check_out_time : 
        #         today = datetime.today()
        #         rec.check_out_time = today
           
       
        # [setattr(rec, 'check_out_time', datetime.today()) for rec in self if not rec.check_out_time]
        # data_ids = [rec.id for rec in self if not rec.check_out_time]
        # self.browse(data_ids).check_out_time = datetime.today()
        # ptint(self)
        #self = emp.attendance(1, 2, )
        #emp.attendance(1, )
        #emp.attendance(2, )
        print(self)

        self.filtered(lambda attendance: not attendance.check_out_time ).check_out_time = datetime.today()


    
    def _send_attendance_report_email(self):
        checkin_time = datetime.now() - timedelta(seconds=7200)
        check_attendance = self.env['emp.attendance'].search([('check_out_time', '=', False),('check_in_time', '>=', checkin_time)])
        template_id = self.env.ref('emp_attendance.email_template_data_display')
        attendance_report = self.env.ref('emp_attendance.report_attendance')
        data_record = base64.b64encode(self.env['ir.actions.report']._render_qweb_pdf(attendance_report.id, check_attendance.ids)[0])
        
        # Create the attachment
        attachment_vals = {
            'datas': data_record,
            'name': "Attendance Report",
            'mimetype': 'application/pdf',
        }
        attachment_id = self.env['ir.attachment'].create(attachment_vals)              
        template_id.attachment_ids = [(6, 0, [attachment_id.id])]
        # template_id.attachment_ids=[(5,0,0)] unlink
        # template_id.attachment_ids = [(3, 0, [attachment_id.id])] 
        print("check_attendance[0].id",check_attendance[0].id)
        template_id.send_mail(check_attendance[0].id, force_send=True)





    # def _send_attendance_report_email(self):
    #         if not self.check_out_time:
               
    #             template_id = self.env.ref('emp_attendance.email_template_data_display')
    #             template_id.attachment_ids = [(5,0,0)]
    #             attendance_report = self.env.ref('emp_attendance.report_attendance')
    #             data_record = base64.b64encode(self.env['ir.actions.report']._render_qweb_pdf(attendance_report, [self.id], data=None)[0])
    #             attchment_vals = {
    #                 'datas': data_record,
    #                 'name': "Attendance Report",
    #                 'mimetype': 'application/pdf',
    #                 'res_model': 'emp_attendance',
    #                 'res_id': self.id,
    #             }
    #             attechment_id = self.env['ir.attachment'].create(attchment_vals)
    #             print("////\n\n\n//////////////tmaile",attechment_id )            
    #             template_id.attachment_ids = [(6, 0, [attechment_id.id])]
    #             template_id.send_mail(self.id, force_send=True)





























                