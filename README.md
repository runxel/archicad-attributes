# Archicad Template & Attributes

Handcrafted deligthful attributes for Archicad and template(s).  
I'm using them daily, so they might not be too much rubbish.

_Your mileage may vary._

---

Maybe you want to have a look at my [Workspace configuration](https://github.com/runxel/archicad-workspaces), using the wonderful [Archicad objects](https://github.com/runxel/ArchiCAD-Objects)  made by me, or just [write GDL code easier](https://github.com/runxel/GDL-sublime).

---

## Index Management
Index management is an integral part of Archicad.

To be consistent over many years it is easier to 'reserve' blocks of index numbers for Archicad and for your own attributes, so you can ease the 'update pain'.
You can do it however you want. I recommend to split them at the hundred marks:

| attr | Archicad reserved | own block starting at |
| --- | --- | --- |
Hatches | `1–199` | `200`

One example: The current last hatch has index number 72. You start with index 73. Next update there are 4 new hatches – your own hatches would start at 77 now. If you migrate one of your projects suddenly some things would display wrongly.

You could also make a project specific block.
Since you can't change the index number in Archicad's interface one strategy consists of pre-generating 'blanks': empty attributes you can fill in when in need.

Beware of changing template attributes. Always duplicate and give a new name (e.g. starting with the project number).
Good work discipline doesn't take much effort and saves a lot of time and headaches!

---

## External objects
Some offices tend or try to keep their files as clean as possible and hotlink the "technical" .pln's into a separate file where the heavy lifting takes place (polygon count wise; think of detailed firniture) and use them for rendering, BimX exporting and such. 
