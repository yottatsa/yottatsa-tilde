# File transfers for Amstrad CP/Ms

Comparing available tools

* [libdsk-utils] and [cpmtools]
* [SAMdisk]
* [iDSK]

## Directory listing

   $ cpmls -f cf2dd boot720.dsk
   $ samdisk dir boot720.dsk
   $ iDSK boot.dsk -l

## Transferring files

   $ cpmcp -f cf2dd -T raw /dev/sde du54/DU54.DOC 0:

   dskform -type dsk -format pcw180 empty.dsk
   iDSK empty.dsk -i myprog.bas
   iDSK empty.dsk -l

   dskform -type dsk -format pcw720 empty.dsk
   cpmcp empty.dsk myprog.bas 0:
   cpmls empty.dsk

## Read and write

MS-DOS 720K format is fine. For [Compaq][CompaqARMADA7800]:

   C:\>format b: /f:720  # on compaq

USB floppy + dd can easily write 720K from raw .img. For more options, use [SAMdisk] or [libdsk-utils]:

   $ samdisk copy /dev/sde f.dsk
   $ 
