from odoo import models, fields



class GMCModulePolicyTable(models.Model):
	_name = 'gmc module.policy table'	
	name = fields.Char('Title', required=True)	
	