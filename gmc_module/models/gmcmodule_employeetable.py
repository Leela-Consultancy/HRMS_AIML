from odoo import models, fields

class GmcModuleEmployeeTable(models.Model):
	_name = 'gmcmodule.employeetable'	

	cardno = fields.Char('Card No', required=True)
	name = fields.Char('Title', required=True)	
	dateofjoining = fields.Date('Date of joining', required=True)
	poltype_id = fields.Many2one('gmcmodule.policytable', ondelete='set null', string='Policy Type', index=True)
	suminsured = fields.Float('Sum Insured(in Lac)', required=True)
	proratapremium = fields.Float('Prorata Premium in Rs.', required=True)
	coveringdays = fields.Integer('Covering Days', required=True)
	strdate = fields.Date('Start Date', related='poltype_id.startdate', store=True)
	enddate = fields.Date('End Date', related='poltype_id.enddate', store=True)

