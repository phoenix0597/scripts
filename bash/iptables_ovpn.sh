#!/bin/sh

eth=$1
proto=$2
port=$3

# Private OpenVPN subnet
PRIVATE=10.8.0.0/24

# Loopback address
LOOP=127.0.0.1

# Allow local loopback
iptables -A INPUT -s "$LOOP" -j ACCEPT
iptables -A INPUT -d "$LOOP" -j ACCEPT

# Allow incoming pings (can be disabled)
iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT

# Allow services such as www and ssh (can be disabled)
iptables -A INPUT -p tcp --dport http -j ACCEPT
iptables -A INPUT -p tcp --dport ssh -j ACCEPT

# Allow incoming OpenVPN packets
iptables -A INPUT -p "$proto" --dport "$port" -j ACCEPT

# Allow TUN interface connections to OpenVPN server
iptables -A INPUT -i tun+ -j ACCEPT
iptables -A FORWARD -i tun+ -j ACCEPT

# Keep state of connections from local machine and private subnets
iptables -A OUTPUT -m state --state NEW -o "$eth" -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -m state --state NEW -o "$eth" -j ACCEPT
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

# Masquerade local subnet
iptables -t nat -A POSTROUTING -s "$PRIVATE" -o "$eth" -j MASQUERADE

# Set default policies
iptables -P OUTPUT ACCEPT
iptables -P INPUT DROP
iptables -P FORWARD DROP
