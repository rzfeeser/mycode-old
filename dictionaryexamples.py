
def main():
    marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }


    cn = input("what name? ")
    cn = cn.capitalize()

    cs = input("what stat? ")
    cs = cs.lower()

    print(marvelchars.get(cn).get(cs))

    print(cn + "'s", cs, "is:", marvelchars.get(cn).get(cs))

main()

