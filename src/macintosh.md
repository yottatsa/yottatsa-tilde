# Apple Macintosh Classic II

Model M4150 (for UK), 4MB RAM, 80MB SCSI HDD. System Software B1-7.0.1.
It was used as a word processor primarily around 1995.

## ToDo

* try out Ethernet
* find a toolchain
* MacTerminal

## Repairs

* floppy drive eject mechanism has been cleaned and oiled;
* CMOS battery has been replaced;
* CRT has been adjusted to fill the screen;
* unclogged and refilled printer cartrige;
* memory upgraded to 10MB;
* FPU installed;
* SCSI hard drive is replaced with the [BlueSCSI];
* Iomega Zip 100 to transfer files.

## Necessary Macinstosh software

For clean System 7.0.1 I found this software useful

* [Simple Text][SimpleText] in addition to TeachText.
* <i>StuffIt Expander 5.5 for System 7</i> to unpack `.sit.hqx`;
* [Disk Copy 6][DiskCopy] to open images.

## Interoperability

Macintosh relies on multi-stream files on filesystem, which makes file exchange a little cumbersome. It's best to keep files either in text, `.hqx` or <i>Apple Double</i>, binary representation.

What works:

* 1.4M floppy and Iomega Zip drives are readable on linux, and contain `hfs` filesystem;
* `unar` can handle both `.hqx` and `.sit` to peek into its content, and extracting streams as separate files;
* <i>MacTar</i> works just fine;
* <i>The Unarchiver</i> for Mac OS X opens `.sit` just fine;

What's somewhat works:

* <i>Compact Pro 1.51</i> can handle packing large archives (10Mb, 600 small files), however there are no modern unpackers;
* small ZIP archives can be created with <i>ZipIt 1.3.8</i>;
* `fondu` can create AppleDouble binary files from resources;

What didn't work:

* can't reliably handle 800K floppies on PC;

## Connectivity

The only readily available option is Macintosh Serial to RS-232 Null-modem adapter on 57600bps.

* <i>ZTerm 1.0.1</i> works just fine, note that it configured for software flow control instead of hardware one that used in linux by default;
* to setup terminal, run `agetty --local-line -hm 57600 ttyUSB0 vt100`;
* `rzsz` gives ability to exchange files over serial connection;

## Networking

For System 7, <i>MacTCP 2.0.x</i>, <i>MacPPP 2.0.1</i>, and a minimal `pppd` setup is enough. The only needed configurations are the next.

For `/etc/ppp/options`:

    proxyarp
    auth
    <local-ip>:<remote-ip>

And for Macintosh, a domain name resolver in the MacTCP control panel. Reboot is required to apply the changes.

* <i>NCSATelnet</i> takes ~600kB RAM and also supports FTP;
* <i>NCSAMosaic 3.0</i> supports HTTP/1.0 and gopher, takes about 4M of RAM;
* <i>MacWeb</i> supports HTTP/1.0 and gopher, no images tho;

I found a few resouces:

* [by The Web Toolbox][oldmacs],
* [by shmhav][mac-internet-faq],
* [by Eric Behr][mactcp], and
* [by Jag][classicinternet].

[DiskCopy]: http://web.archive.org/web/20011202081927/http://download.info.apple.com/Apple_Support_Area/Apple_Software_Updates/English-North_American/Macintosh/Utilities/Disk_Copy/
[bcs]: http://web.archive.org/web/20011218001224/http://download.info.apple.com/Apple_Support_Area/Apple_Software_Updates/English-North_American/Macintosh/Networking-Communications/Comm_Toolbox/BCS_1.1.1.sea.bin
[tldp-macterm]: https://tldp.org/HOWTO/Mac-Terminal.html
[mactcp]: http://web.archive.org/web/20090224140319/http://www.math.niu.edu/~behr/Comp/mactcp.html
[classicinternet]: http://web.archive.org/web/20020603235308/http://www.jagshouse.com:80/classicinternet.html
[oldmacs]: http://web.archive.org/web/19991001223806/http://www.rtis.com/nat/user/toolbox/oldmacs/
[SimpleText]: http://web.archive.org/web/20011125070522/http://download.info.apple.com/Apple_Support_Area/Apple_Software_Updates/English-North_American/Macintosh/Utilities/SimpleText_1.3.txt
[mac-internet-faq]: http://web.archive.org/web/20000817225026/http://www.sjoki.uta.fi/~shmhav/mac-internet-faq.txt
