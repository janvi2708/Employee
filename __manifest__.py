# __manifest__.py

{
    'name': 'Attendance',
    'version': '17.0',
    'category': 'employee',
    'summary' : 'Manage the Attendance',
    'description': 'A simple employee attendance management ',
    'depends': ['hr','mail'],
    'data': [
        'security/attendance_group.xml',
        'security/ir.model.access.csv',
        'views/attendance_report.xml',
        'data/email_template.xml',
        'data/ir_cron.xml',
        'views/hr_attendance_view.xml',
        'views/attendance_view.xml',
        'views/menu_view.xml',
          
        
    ],
    'installable': True,
    'license': 'LGPL-3',

}
