from odoo import models, fields



class GMCModulePolicyTable(models.Model):
	_name = 'GMCModule.PolicyTable'	
	name = fields.Char('Title', required=True)	
	