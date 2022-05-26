# 4.	Дан список гостей, посетивших вечеринку, причем гости в этом списке располагаются в порядке их прибытия:
#       Adela, Fleda, Owen, May, Mona, Gilbert, Ford (Adela приехала на вечеринку первая, а Ford - последний).
#       Гость, прибывший после того, как половина гостей уже была на вечеринке, считается в меру опоздавшим,
#       в то время как гость, прибывший последним, считается опоздавшим неприлично.
#       Определите, попадают ли в одну из этих категорий (и если да, то в какую) следующие гости: May, Fleda, Gilbert и Ford.

guest = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

guest_ok = guest.index('Ford')
opozdal_v_meru = len(guest)/2
neprilichno_pozdno = len(guest) - 1
# neprilichno_pozdno = len(guest)

# v_meru = guest_ok < opozdal_v_meru
# silno = opozdal_v_meru < guest_ok < neprilichno_pozdno

v_meru = guest_ok < neprilichno_pozdno
silno = guest_ok == neprilichno_pozdno

print(f'Гость {guest_ok} опоздал в меру - {v_meru},'
      f' неприлично сильно - {silno}')