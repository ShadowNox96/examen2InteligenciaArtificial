/*
Hechos
*/
quiere(martin, ximena).
quiere(martin,fidelia).
quiere(carlos,ximena).
quiere(fidelia,martin).

/*Todos quieren a juan*/
quiere(martin, juan).
quiere(fidelia, juan).
quiere(carlos, juan).
quiere(ximena, juan).

/*todos quieren a fidelia*/
quiere(ximena, fidelia).
quiere(carlos, fidelia).
quiere(juan, fidelia).

/*Todos se quieren a si mismos*/
quiere(martin,martin).
quiere(juan, juan).
quiere(carlos, carlos).
quiere(ximena, ximena).
quiere(fidelia, fidelia).

/*Alguien quiere a juan y martin*/
alguienjuan_martin() :- quiere(X, juan), quiere(X,martin), write(X + "quiere a juan y martin").


/*Alguien quiere a fidelia*/
quierefidelia() :- quiere(X, fidelia), write(X + "quiere a fidelia").

/*Alguien quiere a todos*/

quieretodos() :- quiere(X, carlos), quiere(X, ximena), quiere(X, juan), quiere(X, martin), quiere(X, fidelia), write(X + "quiere a todos").

/*Reglas */

/*Se quieren mutuamente */
mutuamente(X,Y) :- quiere(X,Y), quiere(Y,X).

/*Quiere carlos a fidelia y martin*/
quierecarlos() :- quiere(carlos,fidelia), quiere(carlos, martin).

/*Quiere carlos a alguien*/
quierecarlosalguien() :- quiere(carlos, X), write("Carlos quiere a "+ X).

/*Quienes son los que se quieren a si mismos*/
quieresimismo() :- quiere(X,X) , write(X + "se quiere a si mismo").


/*Se quiere carlos a si mismo*/
carlossimismo() :- quiere(carlos,carlos).

/*Hay alguien que quiere a fidelia*/
/*Ya se creo la regla anteriormente*/

/*Alguien que quiera a alguien*/
alguienquiere(X) :- quiere(Y,X), write( Y + "quiere a " + X).

/*Quiere carlos a fidelia */
quierecarlosfidelia() :- quiere(carlos,fidelia), write('Carlos quiere a fidelia').

/*Quienes son los que quieren a fidelia*/
quienesquierenfidelia()  :- quiere(X, fidelia), write(X +' quiere a fidelia').


/*Quienes son los que quieren a martin*/
quienesquierenmartin()  :- quiere(X, martin), write(X +' quiere a martin').