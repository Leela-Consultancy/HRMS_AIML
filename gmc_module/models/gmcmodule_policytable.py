from gmc_module import models, fields



class GMCModulePolicyTable(models.Model):
	_name = 'GMC Module'	
	name = fields.Char('Title', required=True)	
	