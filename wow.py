import webbrowser
import wow_notes


print("Talents Express\n")
mythics =["1. Shadowmoon Burial Grounds",
"2. Halls of Valor",
"3. Court of Stars",
"4. Ruby Life Pools",
"5. The Nokhud Offensive",
"6. The Azure Vault",
"7. Algeth'ar Academy",
"8. Temple of the Jade Serpent",]

for i in mythics:
	print(i)

# Ask what key then provide links to talents
# def ask_and_tell():
key = input("What key are you doing?\n").lower()


# Takes input, Checks input, Opens link.
def ask_and_tell(key, list, url, route):
	if key in list:
		webbrowser.open(url)
		webbrowser.open(route)

	else:
		print(f"Error-not-{key}")



# Function for inputs and talent links to dictionaries.
ask_and_tell(key, wow_notes.mythicdic["hov"], wow_notes.mythicdic["hov"][4], wow_notes.mythicdic["hov"][5])
ask_and_tell(key, wow_notes.mythicdic["sbg"], wow_notes.mythicdic["sbg"][4], wow_notes.mythicdic["sbg"][5])
ask_and_tell(key, wow_notes.mythicdic["cos"], wow_notes.mythicdic["cos"][3], wow_notes.mythicdic["cos"][4])
ask_and_tell(key, wow_notes.mythicdic["rlp"], wow_notes.mythicdic["rlp"][3], wow_notes.mythicdic["rlp"][4])
ask_and_tell(key, wow_notes.mythicdic["nok"], wow_notes.mythicdic["nok"][4], wow_notes.mythicdic["nok"][5])
ask_and_tell(key, wow_notes.mythicdic["av"], wow_notes.mythicdic["av"][5], wow_notes.mythicdic["av"][6])
ask_and_tell(key, wow_notes.mythicdic["aa"], wow_notes.mythicdic["aa"][2], wow_notes.mythicdic["aa"][3])
ask_and_tell(key, wow_notes.mythicdic["tjs"], wow_notes.mythicdic["tjs"][5], wow_notes.mythicdic["tjs"][6])

