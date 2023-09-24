# Contributing

> Warning: This is old!

Please follow the [KiCad Library Convention](https://kicad-pcb.org/libraries/klc/) before contributing.

TODO: Use official [KiCad Library Utilities](https://github.com/kicad/kicad-library-utils) to check and fix libraries.

Take a look at the [KiCad File Format DEF](https://en.wikibooks.org/wiki/Kicad/file_formats#Description_of_DEF). As for the FAB library there are a few things to keep in mind:

- In schematics, keep the IC background filled.
- Leave passive components not filled.
- Adjust the footprints so that they are easy to hand-solder.

> Run `test.py` before pushing changes to reposotory.

It will check if everything is right. It will help you fix errors if any. The script is run automatically when push to the repository happens. However it is best to do it before pushing locally. The following is a list of what the script does.

- [x] Match symbol DEF name with its F1 name
- [x] Check if the footprint entry has a library field (fab:Part_Name)
- [x] Check if the footprint fab.pretty/footprint.kicad_mod file exists
- [x] Check if footprint is mapped to a symbol in the library
- [ ] Check if the footprint file name matches the name in the file
- [ ] Check if footprints are visible also on layers F.Cu F.Paste F.Mask
- [ ] Check naming structure PartName_SizeXYZmm_Pitch
- [ ] ...

This library should have all the basic components and parts for the FabAcademy and it's always under construcction. If you want to contribute and add more components to the KiCad libraries, feel free to follow this manual.

You will need to follow this 3 steps:
- Create the footprint and add it to the footprint's library
- Create the symbol and add it to the symbol's library
- Make sure they are connected and they work fine

## Create the footprint and add it to the footprint's library
Create a new project in KiCad and open the Footprint Editor:

![](https://i.imgur.com/npzIxGA.png)

Here you can create a new component from scratch, drawing the pads of it and the vias if necessary. You can write the name of the component and its value or refer it to the schematic. This is the icon to create a new Footprint:

![](https://i.imgur.com/jstb0v3.png)


You can also create a new Footprint using the Footprint Wizard using this icon:

![](https://i.imgur.com/Gsvlrzt.png)

There are different predefined shapes and edit the main parameters. This is an example of a SOIC package and the parameters that you can define:

![](https://i.imgur.com/mS3L9nJ.png)

Another option is to use an existing footprint from any library and edit it. When you finish your footprint, save it as a new footprint.

Finally, you can create a symbol by code. This code is an example of a footprint, in this case it is the code for a 1x05 SMD Pin Header.
```
(module fab-1X05SMD (layer F.Cu) (tedit 5E6F66F5)
  (attr smd)
  (fp_text reference >NAME (at -2.54 0 90) (layer F.SilkS)
    (effects (font (size 1.27 1.27) (thickness 0.1016)))
  )
  (fp_text value Val** (at 0 0) (layer F.SilkS)
    (effects (font (size 1.27 1.27) (thickness 0.15)))
  )
  (pad 1 smd rect (at 0 -5.08) (size 2.54 1.27) (layers F.Cu F.Paste F.Mask))
  (pad 2 smd rect (at 0 -2.54) (size 2.54 1.27) (layers F.Cu F.Paste F.Mask))
  (pad 3 smd rect (at 0 0) (size 2.54 1.27) (layers F.Cu F.Paste F.Mask))
  (pad 4 smd rect (at 0 2.54) (size 2.54 1.27) (layers F.Cu F.Paste F.Mask))
  (pad 5 smd rect (at 0 5.08) (size 2.54 1.27) (layers F.Cu F.Paste F.Mask))
)
```

The most important part here is to make sure you have the correct numbering of your pads, as this will be the link to your symbol.

When you save your component KiCad will ask you in which library you want to save the new footprint, select the fab library.

## Create the symbol and add it to the symbol's library

> Tip: Keep 150 unit distance between the pins for consistency.

After creating a footprint, it's time to create the new symbol for the schematics of the footprint. First open the symbol editor.

![](https://i.imgur.com/SM1c8HN.png)

Here we have 3 options too:

We can create a new symbol from scratch, using the KiCad symbol editor. When you create a new symbol, it will ask you to choose a library and then you can define the properties of it. Finally, you will need to draw the schematic of it and its shape.

![](https://i.imgur.com/MRbK2EW.png)


You can also edit an existing symbol. Just double click it to open it in the editor, edit it and Save it as a new symbol in the library.

Finally, you code it in the <i>fab.lib</i> file, just open the file in a code editor and add your component following the structure of the other components. This is the code of the 1x05-SMD-PinHeader, for example.

```
#
# PINHD-1x05-SMD-HEADER     # PINHD-1x05-SMD-HEADER
#
DEF PINHD-1x05-SMD-HEADER M 0 40 Y Y 1 L N
F0 "M" 0 0 45 H I C CNN
F1 "PINHD-1x05-SMD-HEADER" 0 0 45 H I C CNN
F2 "fab-1X05SMD" 30 150 20 H I C CNN
$FPLIST
 *1X05SMD*
$ENDFPLIST
DRAW
P 2 1 0 0 250 650 100 650 N
P 2 1 0 0 100 650 100 -075 N
P 2 1 0 0 100 -075 250 -075 N
P 2 1 0 0 250 -075 250 650 N
X 1 1 0 500 200 R 40 40 1 1 P I
X 2 2 0 400 200 R 40 40 1 1 P I
X 3 3 0 300 200 R 40 40 1 1 P I  
X 4 4 0 200 200 R 40 40 1 1 P I  
X 5 5 0 100 200 R 40 40 1 1 P I
ENDDRAW
ENDDEF
````

If you've created the symbol in the Symbol Editor, you will need to define the footprint. Just press the <i>Edit symbol properties</i> icon and search for the footprint you've created before in the footprint gap.

![](https://i.imgur.com/PqoqEpy.png)


Save the library and go back to KiCad, you have your symbol and footprint up and running.

## Make sure they are connected and they work fine
Before uploading the new component into this repository, please, make sure they are well connected and referenced and that the footprint works with the physical component, this library will be used by the students so we have to ensure that they work fine.
