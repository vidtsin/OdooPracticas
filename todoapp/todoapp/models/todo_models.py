# -*- coding: utf-8 -*-
from odoo import models,fields

class TodoTask(models.Model):
   _name = 'todo.task'
   _description = 'To-do Task'
   name = fields.Char('Description', required=True)
   is_done = fields.Boolean('Done')
   active = fields.Boolean('Active?', default=True)
   user_ids = fields.Many2many(comodel_name="todo.user",
                          relation="user_task_rel",
                          column1="taskid",
                          column2="userid",			
			  string="Usuari assignat a la tasca")


class TodoUser(models.Model):
   _name = 'todo.user'
   _description = 'To-do User'
   name = fields.Char('Nombre', required=True)
   age = fields.Integer('Edad', required=True)
   apellidos = fields.Char('Apellidos')
   task_ids = fields.Many2many(comodel_name="todo.task",
			 relation="user_task_rel",
			 column1="userid",
			 column2="taskid",
			 string="Tasques assignades a l'usuari")
