eats(tiger,meat).
eats(cow,vegetables).
eats(human,meat).
eats(human,vegetables).
eats(carnivorous,meat).
eats(herbivorous,vegetables).
carnivorous(X) :- eats(X, meat).
omnivorous(X):- eats(X, meat), eats(X, vegetables).
herbivorous(X):- eats(X, vegetables).

