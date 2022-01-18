# E-karta Tol Calen
System Tol Calen jest wyłączną własnością BTA Kompas. Logo systemu wykorzystane w oknie startowym aplikacji oraz jako ikona aplikacji jest wyłączną własnością BTA Kompas.
Elementy systemu oraz logo zostały wykorzystane jako elementy projektu w ramach przedmiotu Języki skryptowe napisanego wyłącznie na użytek indywidualny.
Mechanika karty postaci jest mechaniką systemu aktualną w latach 2018-2019.
-
Gry fabularne – inaczej gry RPG – to połączenie fabularnych gier komputerowych, gier planszowych oraz teatru improwizowanego. Podstawowymi atrybutami graczy są karta postaci i kości do gry. 
W systemie Tol Calen, którego dotyczy projekt, karta postaci zawiera następujące elementy: 
- koncept postaci, czyli jej imię, pochodzenie, klasę (dostępne klasy: Cwany, Uczony, Waleczny) oraz imię gracza wcielającego się w postać,
- 6 Atrybutów, z których każdy może mieć wartość pomiędzy 0 a 5, a dostępna liczba punktów do rozdzielenia w sumie to 15,
- 19 Umiejętności, z których każda może mieć wartość pomiędzy 0 a 5, a dostępna liczba punktów do rozdzielenia w sumie to 20,
- Ekwipunek, czyli wartości pancerza, tarczy oraz broni,
- Spokrewnienie, czyli czy postać jest spokrewniona z jakimś bogiem i w związku z tym może używać magii, Spokrewnienie zużywa jeden Punkt Atrybutów,
- wartości Zdrowia, Energii oraz inicjatywy,
	- Zdrowie wyliczane jest na podstawie Wytrzymałości – jeden punkt Wytrzymałości to 6 punktów Zdrowia,
	- Energia wyliczana jest na podstawie Charakteru, jeśli postać jest Cwana, Intelektu jeśli postać jest Uczona i Zręczności jeśli postać jest Waleczna; wartość Atrybutu mnożona razy 2 i sumowana z wartością Siły Woli, a jeśli postać jest Spokrewniona, otrzymuje jeden dodatkowy punkt Energii,
	- bazowa wartość inicjatywy to suma Zręczności i Spostrzegawczości.
- 3 Punkty Szczęścia, które pozwalają na automatyczne zdanie danego testu,
- Punkty Doświadczenia, które pozwalają na rozwój postaci.
W trakcie rozgrywki gracze dokonują następujących akcji:
- rzucają na parę Atrybut + Umiejętność – rzuca się trzema kośćmi dziesięciościennymi i każda kość, na której wypadła wartość mniejsza lub równa niż suma wartości wybranego Atrybutu i Umiejętności jest traktowana jako sukces, przy czym wartość 1 jest zawsze sukcesem, a wartość 10 jest zawsze porażką; jako wynik rzutu liczy się liczbę sukcesów (tzn. wynikiem rzutu są 0, 1, 2 lub 3 sukcesy),
	- np. postać jest medykiem i wykonuje test leczenia – rzuca na parę Intelekt + Leczenie, przy czym jej Intelekt ma wartość 3, a Leczenie 4, czyli próg sukcesu to 7,
	- na kościach wypadły 2, 7, 9,
	- zatem wynik rzutu to 2 sukcesy.
- rzucają przeciwko Śmierci – jest to rzut na parę Wytrzymałość + Przetrwanie,
- rzucają na obrażenia – rzuca się tyloma kośćmi sześciościennymi, jaką wartość broni ma postać, jeśli na kości wypadły wartości 1 lub 2 to traktuje się je jako jedno obrażenie, wartości 3 i 4 – zero obrażeń, wartości 5 i 6 – dwa obrażenia i sumuje się liczbę obrażeń,
	- np. postać jest wojownikiem i używa ciężkiego miecza oburęcznego, a zatem ma wartość broni 6, rzuca więc 6 kośćmi,
	- na kościach wypadły 1, 1, 5, 6, 5, 4,
	- zatem postać zadaje 9 obrażeń.
- rzucają na inicjatywę – rzuca się jedną kością dziesięciościenną i wynik rzutu dodaje do bazowej wartości inicjatywy,
	- np. postać ma Zręczność 2 i Spostrzegawczość 3, czyli bazowa wartość inicjatywy to 5,
	- na kości wypadło 2,
	- wartość inicjatywy to 7.
- przyjmują i leczą obrażenia oraz zużywają i odnawiają Energię – wartość przyjmowanych obrażeń i zużytej Energii jest ustalana przez Mistrza Gry, a przy leczeniu i odnawianiu Punktów Energii nie można uzyskać większej wartości Zdrowia lub Energii niż wartość bazowa; postać o zerowej Energii nie może rzucać zaklęć, a postać o zerowym Zdrowiu musi wykonać rzut przeciwko Śmierci,
- palą Punkty Szczęścia – spalenie PS pozwala na automatyczne zdanie danego testu niezależnie od wyniku rzutu lub nawet bez rzutu, ale spalonego PS nie można odzyskać,
- otrzymują i zużywają Punkty Doświadczenia – jeden PD zamienia się na jeden Punkt Atrybutów lub trzy Punkty Umiejętności.

Gracze mogą grać tymi samymi postaciami przez wiele kampanii – na początku każdej nowej kampanii mają 3 Punkty Szczęścia oraz tracą niewydane Punkty Doświadczenia, Atrybutów i Umiejętności. Wszystkie wartości Atrybutów, Umiejętności i Ekwipunku powinny zostać takie same.

Branch main zawiera dokumentację projektu. Implementacja aplikacji znajduje się w branchu app.
-
