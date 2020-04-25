/*Hechos*/
gobierna(presidente, chapines).

/*Todos son chapines*/
esChapin(pedro).
esChapin(juan).
esChapin(maria).

/*Todos los chapines tienen un animal*/
tienePerro(pedro).
tienePerro(juan).
tieneGato(maria).

/*Hechos de perros*/
esPerro(boby).
esPerro(spike).
esPerro(duke).

/*Hechos de gatos*/
esGato(michi).
esGato(lilo).

/* Hechos de vacunas*/
esVacuna(rabia).
esVacuna(parvovirus).

/*Hechos de es enfermedad*/
esEnfermedad(rabia).
esEnfermedad(parvovirus).



/*Relacion tiene animal con tiene perro y tiene gato*/
tieneAnimal(X) :- tienePerro(X) ; tieneGato(X).


/*Regla debe vacunar*/
debeVacunar(X,Y,Z) :- tieneAnimal(X), esPerro(Y), esEnfermedad(Z), esVacuna(Z), write('Debe vacunar a su perro').

/*Ejemplo
    debeVacunar(pedro, boby, rabia).
*/





