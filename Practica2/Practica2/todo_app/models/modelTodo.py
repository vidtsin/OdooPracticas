# * -*- coding: utf-8 -*-

from odoo import models, fields


class TodoTask(models.Model):
    _name = "todo.task"
    _description = "To-do Task"

    name = fields.Char("Description", required=True)
    is_done = fields.Boolean("Done?")
    active = fields.Boolean("Active?", default=True)
    owner_ids = fields.Many2many(comodel_name="todo.owner",
                            relation="task_owner_rel",
                            column1="taskid",
                            colum2="ownerid",
                            string="Owner"
                                )


class TodoOwner(models.Model):
    _name = "todo.owner"
    _description = "To-do Owner"

    name = fields.Char("Nombre", required=True)
    age = fields.Integer("Edad", required=True)
    apellidos = fields.Char("Apellidos")
    task_ids = fields.Many2many(comodel_name="todo.task",
                            relation="owner_task_rel",
                            column1="ownerid",
                            colum2="taskid",
                            string="Task"
                                )

