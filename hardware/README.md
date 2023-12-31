# Wordclock v2 Build

## BOM

* Raspberry pi pico
* RTC precision module DS3231 with stemma qt connectors (regular RTC modules like pcf8523 will drift by almost an hour per year)
* Light sensor BH1750 with stemma qt connectors
* 2 stemma qt connectors
* Neopixel led strip (eg. SK6812 or ws2814) 60 LED/m, 2.5m (important: not waterproof)
* USB-C breakout board
* Optional: XT30 or 60 connector
* 11 PCB jumper (or use 11*3 small cables) [See /hardware/pcb_jumper](pcb_jumper/)
* 3mm thick glass panel 30x30cm
* MDF (3mm) Board to cut all components
* 4x M6 bolts with cone-shaped head

## Build

![Wordclock v2 side slice](/docs/img/side-slice.png)

The clock is made of a *glass panel* with a *die-cut vinyl sticker* on the back with the pattern of our clock. I ordered my glass panel from a glass shop nearby, prefer chamfered and polished edges. For the clock face I used this font [word-clock-stencil-mono](https://github.com/mrudelle/wordclock-stencil-mono). Pattern was cut on a cricut tracer. To apply the pattern I used the water technique and an credit card to squeeze all bubbles out. Longest part was taking out all the letters with a pair of tweezers (that's why the font is stencil).

On the vinyl is glued a lasercut MDF grid spacer. The vinyl was gently sanded to provide more grip for the glue.

A diffuser is placed on the spacer. I colored the diffuser with a black marker so that letters are stealth when not lit up. _Tip: mark the squares with a checker pattern to avoid the page to warp too much_

![Wordclock v2 diffuser](/docs/img/build-diffuser.jpg)

Another MDF grid spacer is placed on top (glued) with 4 cone-shaped head m6 screws. The screw will help hold the various layers together. The MDF grid spacer m6 holes are chamfered to hold on to the screws when glued to the vinyl. And the screws are flush with the spacer.

The next layer is an MDF LED row spacer.

Then the back plate, with LED taped on it, with the PCB jumpers soldered to recreate a long chain. I ordered 1.6mm thick custom designed PCB jumpers for cheap (from PCBway IIRC). With castelated holes to easily solder them onto the led strips. See [/hardware/pcb_jumper](pcb_jumper/).

![Wordclock v2 custom designed pcb](/docs/img/build-pcb.jpg)
![Wordclock v2 jumper pcb soldering](/docs/img/build-pcb-solder.jpg)
![Wordclock v2 back plate assembled](/docs/img/build-pcb-done.jpg)

On the back of that back plate goes all the electronics. Hidden by a rim that is screwed to the bolts and holds everything together. I painted the visible parts black to hide them a bit more when looking from the side.

![Wordclock v2 back plate with electornics](/docs/img/back.jpeg)

Tip: do not tighten the screews too much, it might apply a localised negative pressure on the vinyl and start pealing it.



