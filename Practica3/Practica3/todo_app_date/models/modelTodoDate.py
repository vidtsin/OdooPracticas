# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TodoDate(models.Model):
    _inherit = "todo.task" #Modulo del que se hereda

    task_date = fields.Date(string="Expected realization date")
