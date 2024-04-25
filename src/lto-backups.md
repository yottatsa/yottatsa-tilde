# LTO Backups

## for system backup

It uses [`dump`][man_dump]/[`restore`][man_restore] under the hood.

    # mt stsetoptions scsi2logical  # figure out /etc/stinit.def
                                    # make /dev/tape symlink or use /dev/nst0
    $ cd backup
    $ tapebackup
    Target is required

    Dump these file systems:
      /dev/mapper/volume        	(     /) Last dump: Level 6, Date ...

    Usage: tapebackup [-t /dev/tape] -[0-9] TARGET [...]
    $ tapebackup -7 /dev/mapper/volume

## for <ruby>media<rt>anime</rt></ruby> backup

    # mt stclearoptions scsi2logical

1. [`tapemount`][tapeutils] mounts the tape cartrige based on the RFID chip
   label to `/mnt/$LABEL`;
2. [`animetape`][animeutils] without options shows pending items to sort.
3. Operator need to sort out the *Pending* queue, either by creating 
   directories that matching the titles, or moving the titles from `unsorted` 
   to it's directories;
4. Running `animetape --clowntown` will copy anything missing on tapes to a
   current tape if anything is mounted to `/mnt/anime_*`, and then move it to
   place. It will also make all missing copies. Finally, it will create index
   symlinks in `/srv/backup/tape`;
5. [`tapeumount`][tapeutils] will unmount and eject the tape.

```
INFO:__main__:Archive [HorribleRips] Gakuen Babysitters [1080p] as Gakuen Babysitters and backup to anime_A00003
INFO:__main__:Backup [MTBB] Banana Fish (BD 1080p) to anime_A00003
```

[tapeutils]: https://github.com/yottatsa/tapeutils
