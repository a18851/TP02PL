
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'left+-left*ALEATORIO ATRIBUICAO COMENTARIO COMENTARIO_MULTILINHA ELIPSIS EM ENQUANTO ENTRADA ESCREVER FAZER FIM IDENTIFICADOR INCREMENTO NUMERO PARA STRING VAR\n        instrucao : declaracao\n                  | atribuicao\n                  | escrita\n                  | ENTRADA\n                  | ALEATORIO\n                  | ciclo\n                  | comentario\n        declaracao : VAR lista_variaveislista_variaveis : IDENTIFICADORlista_variaveis : lista_variaveis "," IDENTIFICADORatribuicao : IDENTIFICADOR ATRIBUICAO expressaoatribuicao : IDENTIFICADOR ATRIBUICAO ENTRADAatribuicao : IDENTIFICADOR ATRIBUICAO ALEATORIO\n        expressao : NUMERO\n                  | STRING\n                  | IDENTIFICADOR\n                  | expressao \'+\' expressao\n                  | expressao \'-\' expressao\n                  | expressao \'*\' expressao\n                  | expressao \'/\' expressao\n         escrita : ESCREVER STRING lista_argumentos : argumentolista_argumentos : lista_argumentos argumento\n        argumento : expressao\n                  | STRING\n        ciclo : PARA IDENTIFICADOR EM "[" NUMERO ELIPSIS NUMERO "]" FAZER instrucao FIM\n        comentario : COMENTARIO\n                   | COMENTARIO_MULTILINHA\n        '
    
_lr_action_items = {'ENTRADA':([0,17,42,],[5,23,5,]),'ALEATORIO':([0,17,42,],[6,24,6,]),'VAR':([0,42,],[9,9,]),'IDENTIFICADOR':([0,9,12,17,20,29,30,31,32,42,],[10,16,19,21,28,21,21,21,21,10,]),'ESCREVER':([0,42,],[11,11,]),'PARA':([0,42,],[12,12,]),'COMENTARIO':([0,42,],[13,13,]),'COMENTARIO_MULTILINHA':([0,42,],[14,14,]),'$end':([1,2,3,4,5,6,7,8,13,14,15,16,18,21,22,23,24,25,26,28,34,35,36,37,44,],[0,-1,-2,-3,-4,-5,-6,-7,-27,-28,-8,-9,-21,-16,-11,-12,-13,-14,-15,-10,-17,-18,-19,-20,-26,]),'FIM':([2,3,4,5,6,7,8,13,14,15,16,18,21,22,23,24,25,26,28,34,35,36,37,43,44,],[-1,-2,-3,-4,-5,-6,-7,-27,-28,-8,-9,-21,-16,-11,-12,-13,-14,-15,-10,-17,-18,-19,-20,44,-26,]),'ATRIBUICAO':([10,],[17,]),'STRING':([11,17,29,30,31,32,],[18,26,26,26,26,26,]),',':([15,16,28,],[20,-9,-10,]),'NUMERO':([17,29,30,31,32,33,39,],[25,25,25,25,25,38,40,]),'EM':([19,],[27,]),'+':([21,22,25,26,34,35,36,37,],[-16,29,-14,-15,-17,-18,-19,29,]),'-':([21,22,25,26,34,35,36,37,],[-16,30,-14,-15,-17,-18,-19,30,]),'*':([21,22,25,26,34,35,36,37,],[-16,31,-14,-15,31,31,-19,31,]),'/':([21,22,25,26,34,35,36,37,],[-16,32,-14,-15,-17,-18,-19,32,]),'[':([27,],[33,]),'ELIPSIS':([38,],[39,]),']':([40,],[41,]),'FAZER':([41,],[42,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'instrucao':([0,42,],[1,43,]),'declaracao':([0,42,],[2,2,]),'atribuicao':([0,42,],[3,3,]),'escrita':([0,42,],[4,4,]),'ciclo':([0,42,],[7,7,]),'comentario':([0,42,],[8,8,]),'lista_variaveis':([9,],[15,]),'expressao':([17,29,30,31,32,],[22,34,35,36,37,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> instrucao","S'",1,None,None,None),
  ('instrucao -> declaracao','instrucao',1,'p_instrucao','grammar.py',18),
  ('instrucao -> atribuicao','instrucao',1,'p_instrucao','grammar.py',19),
  ('instrucao -> escrita','instrucao',1,'p_instrucao','grammar.py',20),
  ('instrucao -> ENTRADA','instrucao',1,'p_instrucao','grammar.py',21),
  ('instrucao -> ALEATORIO','instrucao',1,'p_instrucao','grammar.py',22),
  ('instrucao -> ciclo','instrucao',1,'p_instrucao','grammar.py',23),
  ('instrucao -> comentario','instrucao',1,'p_instrucao','grammar.py',24),
  ('declaracao -> VAR lista_variaveis','declaracao',2,'p_declaracao','grammar.py',29),
  ('lista_variaveis -> IDENTIFICADOR','lista_variaveis',1,'p_lista_variaveis','grammar.py',34),
  ('lista_variaveis -> lista_variaveis , IDENTIFICADOR','lista_variaveis',3,'p_lista_variaveis_multiple','grammar.py',39),
  ('atribuicao -> IDENTIFICADOR ATRIBUICAO expressao','atribuicao',3,'p_atribuicao','grammar.py',44),
  ('atribuicao -> IDENTIFICADOR ATRIBUICAO ENTRADA','atribuicao',3,'p_atribuicao_leitura','grammar.py',49),
  ('atribuicao -> IDENTIFICADOR ATRIBUICAO ALEATORIO','atribuicao',3,'p_atribuicao_aleatorio','grammar.py',54),
  ('expressao -> NUMERO','expressao',1,'p_expressao','grammar.py',60),
  ('expressao -> STRING','expressao',1,'p_expressao','grammar.py',61),
  ('expressao -> IDENTIFICADOR','expressao',1,'p_expressao','grammar.py',62),
  ('expressao -> expressao + expressao','expressao',3,'p_expressao','grammar.py',63),
  ('expressao -> expressao - expressao','expressao',3,'p_expressao','grammar.py',64),
  ('expressao -> expressao * expressao','expressao',3,'p_expressao','grammar.py',65),
  ('expressao -> expressao / expressao','expressao',3,'p_expressao','grammar.py',66),
  ('escrita -> ESCREVER STRING','escrita',2,'p_escrita','grammar.py',72),
  ('lista_argumentos -> argumento','lista_argumentos',1,'p_lista_argumentos','grammar.py',77),
  ('lista_argumentos -> lista_argumentos argumento','lista_argumentos',2,'p_lista_argumentos_multiple','grammar.py',82),
  ('argumento -> expressao','argumento',1,'p_argumento','grammar.py',88),
  ('argumento -> STRING','argumento',1,'p_argumento','grammar.py',89),
  ('ciclo -> PARA IDENTIFICADOR EM [ NUMERO ELIPSIS NUMERO ] FAZER instrucao FIM','ciclo',11,'p_ciclo','grammar.py',94),
  ('comentario -> COMENTARIO','comentario',1,'p_comentario','grammar.py',100),
  ('comentario -> COMENTARIO_MULTILINHA','comentario',1,'p_comentario','grammar.py',101),
]
