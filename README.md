# DDoS
Projekt ma na celu pokazanie metod ataków i obrony przed atakami DDoS

# Tasks

## Task 0 - Przygotowanie środowiska 
Do przeprowadzenia labolatorium będzie nam potrzebne osobne urządzenie na którym postawimy serwer. Dla wygody, lub z braku możliwości możemy kożystać z wirualnego środowiska. Wybór środowiska jak i systemu operacyjnego nie ma większego znaczenia dla naszego eksperymentu, ale w wypadku nie posiadania żadnego polecamy instalacje **VMware** oraz najnowszą wersje systemu **Ubuntu**.

> VMware: https://www.vmware.com/go/getplayer-win

> Ubuntu: https://sourceforge.net/projects/linuxvmimages/files/VMware/U/Ubuntu_23.10_VM.7z/download

### Configuracja środowiska
Przed uruchomieniem systemu należy zmienić opcje Adaptera Karty Sieciowej z *NAT* na *Bridged*. Dzięki temu VM bedzie zachowywało się jako osobne urządzenie w naszej sieci, a nie jako odwzwierciedlenie naszego komputera i jego IP.

![obraz](https://github.com/Nemezjusz/DDoS/assets/50834734/38a1d8c9-78cb-4bd2-a5e1-05aa2fbebeab)

### Pobranie i uruchomienie servera
Ostanim etapem przygotowawczym będzie skolonowanie i uruchomienie przygotowanego przez nas servera Flask. W dalszych etapach będziemy go modyfikować i wprowadzać dodatkowe zabezpieczenia. 
```
sudo apt install git
sudo apt install python3
sudo apt install python3-pip
sudo apt install python3-venv
sudo python3 -m -venv ddosvenv
source ddosvenv/bin/activate
sudo chmod -R a+rwx ddosvenv
pip3 install flask
git clone https://github.com/Nemezjusz/DDoS.git
cd DDos
flask –app server1 run --host=0.0.0.0
```
Po wpisaniu ostaniej komendy utowożymy serwer dostępny w naszej lokalnej sieci. Znajduje się on pod adresem: `http://<ip_virtualnej_maszyny>:5000`

## Task 1
W celu zrozumienia na jakiej zasadzie działają ataki dos w zadaniu pierwszym będziemy musieli napisać prosty atak dos w języku Python, który będzie symulował prosty atak DoS na serwer za pomocą zapytań GET lub POST. Chodzi o to aby za pomocą np metody GET powodować ciągłe i równoczesne wysyłanie zapytań na docelowy adres URL serwera, co może prowadzić do przeciążenia serwera i utraty dostępności. 
>Możesz wspomóc sie już zaimplementowanym atakiem dos którego używamy w programie.

>Link --> [dos.py](https://github.com/Nemezjusz/DDoS/blob/main/dos.py)


## Task 2 - Przeprowadzenie ataku i analiza 
W tym zadaniu przyda nam się również **Wireshark**. Dzieki niemu bedziemy w stanie obserwować wysyłane i odpierane przez nas pakiety.

Do aktaku możemy wykorzystać wcześniej napisany kod, lub gotowy program znajdujący się w pliku dos.py. Przed odpaleniem ataku należy przeanalizować kod i porównać go z napisanym przez siebie.
W przypadku używania gotowego programu poprosi on nas o wybranie typu ataku. 

### Atak GET
Zaczniemy od wyboru ataku typu **GET**. Kolejną zmienną jaką musimy wybrać jest ilość wątków. Tutaj sprawa nieco się komplikuje. 
Aby osiągnąć porządany efekt musimy wysłać do servera tyle zapytań aby nie było w stanie odpowiedzeć. Tutaj w zależności jakie parametry nadliśmy VMowi ilość wątków może być w tysiącach. Im więcej wybierzemy tym lepiej zauważmy wyniki w postaci wydłużenia czasu odpowidzi serwera.

![obraz](https://github.com/Nemezjusz/DDoS/assets/50834734/ed5ba84f-a3c2-4f7a-bb17-977728044dc7)

W Wiresharku możemy zaobserwować ogromne ilości pakietów GET wysyłanych do i z serwera. Informacje tę możemy również zobaczyć w terminalu serwera.
Wchodząc w *Statystyki* > *IPv4 Statistic* > *All Addresses* możemy zauważyć ilość, rate oraz burst wysyłanych i otrzymywanych danych.

![obraz](https://github.com/Nemezjusz/DDoS/assets/50834734/84bad358-8358-4697-b64d-2107aae12c2d)

### Atak POST
W podobny sposów możemy przeprowadzić atak **POST**. Potrzebne będą nam jedynie małe zmiany na serwerze, aby mógł on takie zapytania przyjmować. 
Wystarczy, wyłączymy pierwszy serwer za pomocą kombinacji klawiszy *Ctrl+C* i włączymy nowy za pomocą komendy: 

`flask –app server2 run --host=0.0.0.0`

### Pozostałe ataki
W ramach ćwiczenia możesz przetestować reszte dostępnych ataków. Każdy z nich różni się podejściem i rodzajem wysyłanych pakietów. Pamiętaj że najlepsze ataki są dobrane pod konkretny cel!

### TODO
W ramch zadania wyślij SSa Statystyk Wiresharka z dowlnego ataku.


## Task 3 - Zapezpieczenie serwera
W tej części zabezpieczymy serwer od strony aplikacji. Zabezpieczenia takie pozwalają załagodzić ataki a niektórych kompletnie uniknąć. Zabezpieczenia te możemy podzielić na trzy główne kategorie - Request Rate Limiting, Request Rate Limiting oraz Web Application Firewall. Skupimy się na pierwszym z nich.

### Request Rate Limiting

Ograniczanie liczby żądań (Request rate limiting) to istotny element skutecznej strategii obrony przed atakami DDoS. Polega to na ustawieniu limitu liczby żądań, jakie serwer może przyjąć w określonym czasie. Na przykład, zakładając, że normalny użytkownik nie może przesyłać szczegółów logowania więcej niż pięć razy na sekundę, możemy zdecydować, że jeśli użytkownik wysyła żądania częściej, jest to prawdopodobnie próba ataku. Następnie możemy ustawić limit liczby żądań dla punktu końcowego API logowania na pięć na sekundę i zablokować każdy adres IP klienta, który narusza tę zasadę.

Do wprowadzenia ograniczenia żądań na naszym serwerze użyjemy **flask_limiter**. Aby go zainstalować użyj komendy:

```pip3 install flask_limiter```

Przykład użycia możemy zobaczyć na stronie: 
> https://flask-limiter.readthedocs.io/en/stable/

### TODO
Za pomocą komendy `nano` lub dowolnego innego edytora wprowadź do pliku server1.py ograniczenie **1 zapytania na 2 sekundy**.

Teraz możemy ponownie przeprowadzić wybrany atak i porównać czas odpowiedzi serwera jak i ilość otrzymywanych pakietów (np. GET)

