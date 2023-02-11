# Dial-in server

Configure PPP:

    # /etc/ppp/options:
    asyncmap 0
    crtscts
    local
    lock
    passive
    proxyarp
    lcp-echo-interval 30
    lcp-echo-failure 4
    netmask 255.255.255.0
    192.168.1.7:192.168.1.8
    noauth
    silent

Setting up alias:

    alias ppp="exec /usr/sbin/pppd -detach"

Automating `getty`: 

    # /etc/udev/rules.d/99-usb-serial.rules
    # get attributes: `udevadm info --attribute-walk -n /dev/...`
    # reload rules: `udevadm control --reload-rules`
    SUBSYSTEM=="tty", DRIVERS=="pl2303", TAG+="systemd", ENV{SYSTEMD_WANTS}="serial-getty@$name.service"

[`udev` rules, <cite>cbrake</cite>](https://gist.github.com/cbrake/4337154).
