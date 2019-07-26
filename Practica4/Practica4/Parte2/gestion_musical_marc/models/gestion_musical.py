# -*- coding: utf-8 -*-

from odoo import fields, models


class Author(models.Model):
    # Modulo del que heredamos
    _inherit = 'author'

    lugar_nacimiento = fields.Char(string='Lugar de nacimiento')


class Disc(models.Model):
    # Modulo del que heredamos
    _inherit = 'disc'

    # Importante poner las letras de cadad opcion en orden
    genere = fields.Selection([('a', 'Rock'), ('b', 'Pop'), ('c', 'Pop-Rock'), ('d', 'Heavy')], string="Genero")


class Gira(models.Model):
    _name = 'gira'

    any = fields.Integer('Año')
    ciudades = fields.Char('Ciudades')
    author_id = fields.Many2one(comodel_name='author', string='Autor')
    disc_id = fields.Many2one(comodel_name='disc', string='Disco')
    top_song_ids = fields.Many2many(comodel_name='song',
                                    relation='gira_song_rel',
                                    column1='gira_id',
                                    column2='song_id',
                                    string="Top Songs")
