# uxn-unx

How to build an OS from scratch.

## 6th of February, 2022

The [uxn]/[varvara] concept looks beautiful as it is. Especially with [paradise], it asks not to bring there any of the conceptions one learned before.

> Make what you can, or what you want?

As a unix-like systems engineer, I really miss fork/wait/kill in varvara, this way I could build something unix-like out of it.
Tho I'm still worried I just do things the way I learnt things should be. This approach works well in commercial world, sure. Would it work in the *world of art*?

In classic, monolithic, unix-like operating systems, there is always a process, and the way to create a process is to `fork` itself. Then the child would `exec` into new application, much like [launcher] in [varvara] can run another ROM. Arguments to the new app are passed inside the `syscall` and straight to the `int main(int argc, char *argv)`. Operating system there is no more that the library with the interfaces, `syscall`, protected behind interrupts.

Most of it can be done with [uxn]/[varvara] with its devices and vectors. 

> You'd want to create a uxn app that handles the routing of vectors to loaded applications in memory. You'd have to devise a scheme for the application format if you're really keen on doing multi-tasking in uxn.

This, however, poses a question yet to solve:

* do I want an OS inside the [uxn], self-hosted and handling device access; 
* or do I want an OS outside of [varvara], where [uxn] is the only runtime and the microkernel is just juggling devices and merely VMs?

First is how the [@devine] desined it, quoting them

> Uxn is the CPU, think of uxn like the 6502 residing inside the NES. Varvara is only a device API spec, think of it like the Commodore 64, or the Atari. An operating system written for varvara, in uxntal, would allocate time and devices control to applications in memory.

Second is how I saw it in real life: [uxn] is supposed to run on top of some kind of CPU, [varvara] is supposed to run on top of some kind of OS.
