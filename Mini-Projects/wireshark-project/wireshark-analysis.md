# Wireshark Network Analysis

## Tool Used
- tshark (command-line Wireshark)

## Capture Info
- **File:** wireshark-project/captures/my_capture.pcapng
- **Total Packets:** 100
- **Interface:** eth0 (IP: 10.0.2.15)
- **Duration:** ~77 seconds

---

## Packet 1 — DNS (Domain Name System)
**Packet #1**
- **Protocol:** DNS over UDP (Port 53)
- **Source:** 10.0.2.15 (my Kali machine)
- **Destination:** 10.0.2.3 (DNS resolver/gateway)
- **What is happening:** My machine is sending a DNS query asking "What is the IP address of google.com?" (Type A record). The DNS server responds in Packet #2 with the answer: 142.250.76.206. This is the first step before any connection to google.com can happen.

---

## Packet 2 — ICMP (Internet Control Message Protocol)
**Packet #17**
- **Protocol:** ICMP (Ping)
- **Source:** 10.0.2.15 (my Kali machine)
- **Destination:** 142.250.76.206 (google.com)
- **What is happening:** My machine sends an ICMP Echo Request (ping) to Google's server. Packet #18 shows Google replying with an Echo Reply, confirming the host is reachable. TTL=64 means the packet started with 64 hops remaining. Round trip was ~38ms.

---

## Packet 3 — ARP (Address Resolution Protocol)
**Packet #29**
- **Protocol:** ARP
- **Source:** 08:00:27:b4:a1:05 (my Kali machine MAC)
- **Destination:** Broadcast (ff:ff:ff:ff:ff:ff)
- **What is happening:** My machine is broadcasting "Who has 10.0.2.3? Tell 10.0.2.15" asking the local network for the MAC address of the gateway. Packet #30 shows the gateway (52:55:0a:00:02:03) replying with its MAC address. This is how Layer 2 (MAC) addresses are resolved from Layer 3 (IP) addresses.

---

## Packet 4 — TCP (Transmission Control Protocol)
**Packets #57-59**
- **Protocol:** TCP (3-Way Handshake)
- **Source:** fd17:625c:f037:2:5373:973b:4507:96e4 (my machine IPv6, Port 44396)
- **Destination:** 2606:4700:9642:8c7c:33c5:0:ccc4:a209 (example.com, Port 80)
- **What is happening:** This is a classic TCP 3-way handshake before loading example.com:
  - Packet 57: SYN — my machine initiates connection
  - Packet 58: SYN-ACK — server acknowledges and responds
  - Packet 59: ACK — my machine confirms, connection established
  After this, HTTP data transfer begins.

---

## Packet 5 — HTTP (HyperText Transfer Protocol)
**Packet #60**
- **Protocol:** HTTP/1.1 (unencrypted web traffic)
- **Source:** fd17:625c:f037:2:5373:973b:4507:96e4 (my machine, Port 44396)
- **Destination:** 2606:4700:9642:8c7c:33c5:0:ccc4:a209 (example.com, Port 80)
- **What is happening:** My machine sends an HTTP GET / request to example.com asking for the homepage. Packet #62 shows the server responding with HTTP/1.1 200 OK and returning the HTML content (text/html). This is plain unencrypted HTTP — in real scenarios HTTPS (port 443) would be used instead, encrypting all this data.

---

## Protocol Summary Table

| # | Protocol | Packets | Purpose |
|---|----------|---------|---------|
| 1 | DNS | 34 | Resolving domain names to IPs |
| 2 | ICMP | 30 | Ping requests and replies |
| 3 | ARP | 4 | Resolving IPs to MAC addresses |
| 4 | TCP | 4 | Connection setup (3-way handshake) |
| 5 | HTTP | 4 | Unencrypted web page transfer |

---

## Key Takeaways
- **DNS always comes first** — before any connection, the domain must be resolved to an IP
- **ARP works at Layer 2** — needed to find the MAC address of the local gateway
- **TCP requires a handshake** — SYN → SYN-ACK → ACK before any data flows
- **HTTP is unencrypted** — all request/response data is visible in plain text in the capture
- **ICMP is used for diagnostics** — ping confirms host reachability and measures latency
