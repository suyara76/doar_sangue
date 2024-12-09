% Fatos sobre compatibilidade dos tipos sanguíneos
compativel(a_mais, a_mais).
compativel(a_mais, ab_mais).
compativel(a_menos, a_mais).
compativel(a_menos, a_menos).
compativel(a_menos, ab_mais).
compativel(a_menos, ab_menos).
compativel(b_mais, b_mais).
compativel(b_mais, ab_mais).
compativel(b_menos, b_mais).
compativel(b_menos, b_menos).
compativel(b_menos, ab_mais).
compativel(b_menos, ab_menos).
compativel(ab_mais, ab_mais).
compativel(ab_menos, ab_mais).
compativel(ab_menos, ab_menos).
compativel(o_mais, a_mais).
compativel(o_mais, b_mais).
compativel(o_mais, ab_mais).
compativel(o_mais, o_mais).
compativel(o_menos, a_mais).
compativel(o_menos, a_menos).
compativel(o_menos, b_mais).
compativel(o_menos, b_menos).
compativel(o_menos, ab_mais).
compativel(o_menos, ab_menos).
compativel(o_menos, o_mais).
compativel(o_menos, o_menos).

% Fatos sobre compatibilidade do fator RH
rhcomp(positivo, positivo).
rhcomp(negativo, positivo).
rhcomp(negativo, negativo).

% Fatos sobre as características dos doadores
tiposanguineo(joao,a).
tiposanguineo(davi,a).
tiposanguineo(maria,a).
tiposanguineo(ana,a).
tiposanguineo(julia,o).
tiposanguineo(alice,a).
tiposanguineo(pedro,a).
tiposanguineo(laura,b).
tiposanguineo(manuela,b).
tiposanguineo(vitoria,b).
tiposanguineo(manuel,o).
tiposanguineo(jose,ab).
tiposanguineo(carlos,ab).
tiposanguineo(telma,o).

fatorrh(joao,positivo).
fatorrh(davi,positivo).
fatorrh(maria,negativo).
fatorrh(ana,negativo).
fatorrh(julia,positivo).
fatorrh(alice,positivo).
fatorrh(pedro,negativo).
fatorrh(laura,positivo).
fatorrh(manuela,negativo).
fatorrh(vitoria,positivo).
fatorrh(manuel,positivo).
fatorrh(jose,positivo).
fatorrh(carlos,negativo).
fatorrh(telma,negativo).

peso(joao,75.7).
peso(davi,50).
peso(maria,49).
peso(ana,80).
peso(julia,47).
peso(alice,30).
peso(pedro,20).
peso(laura,54).
peso(manuela,61).
peso(vitoria,70).
peso(manuel,130).
peso(jose,65).
peso(carlos,48).
peso(telma,79).

idade(joao,41).
idade(davi,24).
idade(maria,51).
idade(ana,17).
idade(julia,15).
idade(alice,56).
idade(pedro,10).
idade(laura,18).
idade(manuela,66).
idade(vitoria,12).
idade(manuel,56).
idade(jose,100).
idade(carlos,67).
idade(telma,48).

% Regra para verificar compatibilidade entre doador e receptor
doacao_valida(Doador, Receptor, RhDoador, RhReceptor) :-
    compativel(Doador, Receptor),
    rhcomp(RhDoador, RhReceptor).

% Regra principal para determinar se um indivíduo pode doar para outro
podedoar(Doador, Receptor) :-
    tiposanguineo(Doador, TipoDoador),
    tiposanguineo(Receptor, TipoReceptor),
    fatorrh(Doador, RhDoador),
    fatorrh(Receptor, RhReceptor),
    peso(Doador, PesoDoador),
    idade(Doador, IdadeDoador),
    compativel(TipoDoador, TipoReceptor),
    rhcomp(RhDoador, RhReceptor),
    PesoDoador > 50,
    IdadeDoador >= 18,
    IdadeDoador =< 65.
