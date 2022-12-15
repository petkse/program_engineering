study(dasha, troechnic, woman).
study(masha, horoshist, woman).
study(misha, troechnic, man).
study(pasha, otlichnic, man).

molodets(X):- study(X, horoshist, _).
molodets(X):- study(X, otlichnic, _).

/* Другой вариант записи правила:
molodets(X):- study(X, Y, _), Y = 'horoshist'.
molodets(X):- study(X, Y, _), Y = 'horoshist'.*/
