# Apricot PC

* Emulation: `mame`, `qdae`
* Disk IO:
  - [`APRIDISK`](http://actapricot.org/support/apricot_apridisk.html)
  - [APEDRIVE](https://ai.ansible.uk/apedrive.html)
* Terminal: `ASYNC`


## Emulating

    mame apricotxi -flop1 apr00001.dsk -flop2 xx.dsk -window -exp:1 512k -exp:2 128k
