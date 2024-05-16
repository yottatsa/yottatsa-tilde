# Icom IC-F11 series handheld radio

* Robust "professional" (no screen) VHF or UHF handheld series released in 2001, goes with good [service manual][ICOM-F11_SM] and parts compatibility across variants.
* Programming software: [CS-F11], [CS-F11 Adj][CS-F11_Adj], cable: [OPC-478/U/UC].
* Hi-resolution photos of [top](../assets/icom_ic-f22sr-f12s-top.jpg) and [bottom](../assets/icom_ic-f22sr-f12s-bottom.jpg) sides of the board

I use pair of `F12S` VHFs, it only has 2 channels, and configured for commercial license.

## 2 to 16 channels

I want to have:

* more channels on VHF stations, and
* handy UHF stations for hacking, 

so I ordered "a bucket-full of borker UHF stations" from hire, gonna try mixing/matching parts. The batch has 8 F22SRs (16 channels, non-removable antenna), 2 F4SRs (out of scope), and all the charging gadgets (honestly, it was a steal of a deal). The only significant downside is non-removable antenna&nbsp;&mdash; those are going to be replaced with Icom standard _8950004671 ANT connector 101A_.

To change the variant, strapping `0R` resistors `W11`, `W12`, `W13` to be removed, and the switch unit replaced from _SW-B_ (toggle switch) to _SW-A_ (16 postition encoder).
Channel variant is only configured in EEPROM in second nibble of 4th and 8th bytes. Flipping those changes the station type in _CS-F11_.

<pre class="hex"> 
 pmr1ch.icf: <i>0000</i><i>10</i><span>24</span><span>58</span><span>01</span><span>0<strong>0</strong></span><span>00</span><span>00</span><span>00</span><span>C<strong>3</strong></span><span>84</span><span>63</span><span>50</span><span>0D</span><span>32</span><span>64</span><span>0F</span><span>0A</span>
 pmr2ch.icf: <i>0000</i><i>10</i><span>24</span><span>58</span><span>01</span><span>0<strong>1</strong></span><span>00</span><span>00</span><span>00</span><span>C<strong>2</strong></span><span>84</span><span>63</span><span>50</span><span>0D</span><span>32</span><span>64</span><span>0F</span><span>0A</span>
pmr16ch.icf: <i>0000</i><i>10</i><span>24</span><span>58</span><span>01</span><span>0<strong>2</strong></span><span>00</span><span>00</span><span>00</span><span>C<strong>0</strong></span><span>84</span><span>63</span><span>50</span><span>0D</span><span>32</span><span>64</span><span>0F</span><span>0A</span>
</pre>

## Flash version

There seem to be an access port on `F22SR`, could be because it uses `HD64F3664FP` (flash) instead of HD6433664A24FP (mask), TBD

Port has next pinout, CCW:

1. `GND`
2. `?`
3. <code class="invert"><abbr title="inverted">/</abbr>RES</code>
4. `VCC`
5. `?`
6. `?`

## Notes

* battery’s type detection pad should be tied to ground to transmit in high power
* configuration software has advanced modes, navigate Help -> About... and type:
    - "manufacture" for unlocked channels (still figuring out)
    - "reserve" for additional adjustments
* configuration file is just a hexdump of `BR24C16FV-E2` 2KB I²C EEPROM, no need to solder the hookup to patch
* hardware selectors located on a top side:
    - `R143`: all VHF and `F21`, `F21S`, `F22`, `F22S`, or
    - `R145`: license-free, `F21BR`, `F21GM`, `F22SR`;
    - `R146`: present on all models, TBD, or
    - `R144` (virtual, weak pull-up is routed on PCB like in `R143,R145`): absent on all models, TBD.

[ICOM-F11_SM]: ../assets/icom_ic-f11_sm.pdf
