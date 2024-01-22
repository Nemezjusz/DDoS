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
git clone https://github.com/Nemezjusz/DDoS.git
flask –app <servername> run --host=0.0.0.0
```

## Task 1 - Przeprowadzenie ataku i analiza 

## Task 2 - Zapezpieczenie serwera
