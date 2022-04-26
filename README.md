# matura2020
Repozytorium zawierające programy obliczeniowe w pythonie do zadań maturalnych z Matury z Informatyki - Maj 2020

# zadanie 1

Treść:
_Niech n będzie dodatnią liczbą całkowitą, a A[1..n] i B[1..n] będą n-elementowymi tablicami
liczb całkowitych.
Dla nieujemnej liczby całkowitej k, gdzie k < n, powiemy, że tablice A i B są k-podobne, gdy
A[1..k] = B[n-k+1..n] oraz A[k+1..n] = B[1..n-k].
Liczbę k nazywamy świadectwem podobieństwa.
Uwaga: dla k = 0 przyjmujemy, że prawdziwe jest A[1..0]=B[n+1..n]._

**1.1**
_Uzupełnij tabelę – wpisz w pustych kratkach odpowiednie wartości. W wierszu piątym
i siódmym wpisz słowo PRAWDA, jeśli tablice A i B są k-podobne przy podanym k, albo FAŁSZ
w przeciwnym przypadku. W wierszu szóstym wpisz takie k, dla którego tablice A i B są
k-podobne._ 

Lp. n Tablica A Tablica B k Odpowiedź
1. 3 [5, 7, 9] [5, 7, 9] 0 PRAWDA
2. 5 [4, 7, 1, 4, 5] [1, 4, 5, 4, 7] 2 PRAWDA
3. 5 [10, 9, 12, 10, 9] [10, 10, 9, 9, 12] 3 FAŁSZ
4. 5 [3, 6, 5, 1, 8] [5, 1, 8, 3, 6] 4 FAŁSZ
5. 5 [1, 2, 3, 4, 5] [3, 4, 5, 1, 2] 2 ?
6. 9 [1,1,1,1,3,1,1,1,1] [3,1,1,1,1,1,1,1,1] PRAWDA
7. 6 [4, 2, 4, 4, 2, 6] [4, 4, 2, 6, 4, 2] 1 ?

Wiersze o indexach 5 i 7 znajdują się w listingu do zadania 1.2.py

**1.2**
_Zapisz w wybranej przez siebie notacji (w postaci pseudokodu, listy kroków lub w wybranym
języku programowania) funkcję czy_k_podobne(n, A, B, k), gdzie A i B są n-elementowymi
tablicami liczb całkowitych. Wynikiem funkcji jest PRAWDA, jeśli tablice A i B są k-podobne
dla zadanego parametru k, natomiast FAŁSZ – w przeciwnym przypadku.
Uwaga: w zapisie możesz wykorzystać tylko operacje arytmetyczne (dodawanie,
odejmowanie, mnożenie, dzielenie, dzielenie całkowite, reszta z dzielenia), odwoływanie się
do pojedynczych elementów tablicy, porównywanie liczb, instrukcje sterujące i przypisania do
zmiennych lub samodzielnie napisane funkcje zawierające wyżej wymienione operacje.
_

**1.3**
_Zapisz w wybranej przez siebie notacji funkcję czy_podobne(n, A, B), która dla danych tablic
A i B daje odpowiedź PRAWDA, jeśli istnieje takie k, dla którego tablice A i B są k-podobne,
natomiast FAŁSZ – w przeciwnym przypadku.
Uwaga: w zapisie możesz skorzystać jedynie z operacji wymienionych w zadaniu 1.2. oraz
funkcji czy_k_podobne(n, A, B, k) opisanej w zadaniu 1.2. _

# zadanie 2


Argumentami procedury sym (a, b) są dwie nieujemne liczby całkowite 𝑎 i 𝑏. Wywołanie tej
procedury spowoduje wypisanie pewnego ciągu liczb całkowitych.
sym(a,b)
  jeżeli a ≠ 0
    sym(a – 1, b + 1)
    wypisz a * b
    sym(a – 1, b + 1)
    
    
 W tym zadania mamy do czynienia z rekurencją dla dowlonych a i b możemy ustalić wzór 2^a - 1;

**2.1**

Uzupełnij tabelę – podaj wynik działania procedury sym (a, b) dla wskazanych argumentów
𝑎 i 𝑏.

a b sym (a, b)
3 1 3 4 3 3 3 4 3
4 2 5 8 5 9 5 8 5 8 5 8 5 9 5 8 5
3 3
4 1 

**2.2**

Uzupełnij tabelę – podaj długość ciągu liczbowego otrzymanego w wyniku wywołania
procedury sym (a, b) dla wskazanych argumentów a i b. 




