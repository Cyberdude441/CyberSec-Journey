# Networking Fundamentals Notes

## 1. OSI Model (7 Layers)

The OSI (Open Systems Interconnection) model is a framework that breaks down how network communication works. Think of it as a building with 7 floors, where each floor handles a specific job. Data travels down these layers when sending and back up when receiving.

### Layer 7: Application Layer
This is where users and applications live. When you open your browser, send an email, or download a file, you're working at this layer. Applications like Chrome, Outlook, and Discord operate here. These apps create the data that needs to be sent.

### Layer 6: Presentation Layer
This layer acts like a translator and formatter. It takes data from the application and gets it ready for transmission by compressing it, encrypting it, or converting it to a standard format that other computers can understand. If you're sending encrypted messages, this layer handles the encryption/decryption.

### Layer 5: Session Layer
This layer manages conversations between computers. Imagine calling someone on the phone - this layer is like establishing the call, keeping it connected, and hanging up properly. It creates, maintains, and terminates sessions so data flows smoothly between two devices.

### Layer 4: Transport Layer
This is about reliability and speed. It decides whether data should be sent reliably (making sure nothing is lost) or quickly (not waiting for confirmations). It also breaks large messages into smaller chunks called segments that can travel through the network.

### Layer 3: Network Layer
This layer handles routing - figuring out the best path for data to reach its destination. It's like a postal system that looks at an address and decides which route the mail should take. It uses IP addresses to identify devices across networks.

### Layer 2: Data Link Layer
This layer handles communication between devices on the same local network. It packages data into frames and uses MAC addresses (like unique identifiers on your computer's network card) to make sure data reaches the correct physical device nearby.

### Layer 1: Physical Layer
This is the actual hardware - cables, wireless signals, electrical pulses, and light signals. It's the physical stuff that carries the 1s and 0s. Ethernet cables, fiber optic lines, and WiFi radio waves all operate at this layer.

---

## 2. TCP vs UDP: Key Differences

Both TCP and UDP are transport layer protocols that sit at Layer 4 of the OSI model. They're like two different delivery services - one is reliable but slower, the other is fast but risky.

### TCP (Transmission Control Protocol)

**Reliability First:** TCP guarantees that every piece of data arrives at the destination in the correct order. If something gets lost, TCP automatically asks for it to be sent again. It's like sending a package with tracking and insurance.

**How it works:** Before sending data, TCP establishes a connection with a "handshake" (a quick back-and-forth greeting). Once connected, it sends data, waits for acknowledgment that it arrived, and only moves on when everything is confirmed.

**Slower but safer:** Because TCP waits for confirmations, it's slower. But you know nothing is lost.

**When to use TCP:**
- Email (you don't want to lose messages)
- Web browsing (websites need to load correctly)
- File transfers (every byte matters)
- Banking (absolutely cannot lose or corrupt data)
- SSH/remote login (commands must execute properly)

### UDP (User Datagram Protocol)

**Speed First:** UDP doesn't care if data arrives or if it arrives in order. It just sends data and moves on without waiting for confirmation. Like sending a postcard that might get lost - but you sent it anyway.

**Simple and fast:** UDP skips the handshake and all the checking. It just fires off the data, making it much quicker.

**When to use UDP:**
- Video streaming (a few lost frames won't ruin the video)
- Online gaming (faster response is more important than perfect data)
- Voice/video calls (slight delays matter more than perfect data)
- DNS queries (quick lookups)
- Live sports broadcasts (speed matters more than perfection)

### Quick Comparison Table

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Requires setup | Connectionless |
| Reliability | Guaranteed delivery | No guarantee |
| Order | Data arrives in order | Order not guaranteed |
| Speed | Slower (waits for confirmation) | Faster (no waiting) |
| Error checking | Extensive | Minimal |
| Best for | Important data | Time-sensitive data |

---

## 3. Ten Common Network Protocols and Their Port Numbers

Ports are like apartment numbers in a building - they tell data which service should handle it on a device.

### 1. HTTP (HyperText Transfer Protocol)
- **Port:** 80
- **What it does:** Transfers web pages from servers to your browser. It's unencrypted, so anyone on the network could potentially see what you're viewing.
- **Uses:** Regular websites without HTTPS

### 2. HTTPS (HyperText Transfer Protocol Secure)
- **Port:** 443
- **What it does:** Same as HTTP but encrypted. Your browser and the server scramble the data so only they can read it. This is why banks and email services use HTTPS.
- **Uses:** Secure websites, online banking, email

### 3. FTP (File Transfer Protocol)
- **Port:** 21
- **What it does:** Transfers files between computers. It's an older method that's less secure than modern alternatives, but still used for uploading website files to servers.
- **Uses:** File uploads/downloads, managing website files

### 4. SSH (Secure Shell)
- **Port:** 22
- **What it does:** Allows you to connect to another computer remotely and control it through commands. Everything is encrypted. Developers use this to access servers safely.
- **Uses:** Remote server access, secure file transfer (SFTP)

### 5. Telnet
- **Port:** 23
- **What it does:** Similar to SSH but without encryption. You can remotely access a computer, but anyone watching the network can see your commands and passwords. It's outdated and rarely used anymore.
- **Uses:** Legacy systems, testing connections (but SSH is preferred now)

### 6. SMTP (Simple Mail Transfer Protocol)
- **Port:** 25, 587, 465
- **What it does:** Sends emails from your email client to the mail server. When you hit "send" in Gmail or Outlook, SMTP is handling it.
- **Uses:** Sending emails

### 7. POP3 (Post Office Protocol 3)
- **Port:** 110
- **What it does:** Downloads emails from a mail server to your computer. Once downloaded, emails are usually deleted from the server (though you can configure it otherwise).
- **Uses:** Retrieving emails from servers

### 8. IMAP (Internet Message Access Protocol)
- **Port:** 143
- **What it does:** Syncs emails between server and your device. Unlike POP3, emails stay on the server so you can access them from multiple devices and they stay synced.
- **Uses:** Modern email access (Gmail, Outlook use IMAP)

### 9. DNS (Domain Name System)
- **Port:** 53
- **What it does:** Translates domain names (like google.com) into IP addresses (like 142.250.185.46) that computers actually understand. Every time you type a URL in your browser, DNS is working behind the scenes.
- **Uses:** All internet browsing

### 10. DHCP (Dynamic Host Configuration Protocol)
- **Port:** 67 (server), 68 (client)
- **What it does:** Automatically assigns IP addresses to devices on a network. When you connect to WiFi, DHCP is the service that gives your device an IP address so it can communicate on the network.
- **Uses:** WiFi networks, home networks

---

## 4. How DNS Works: Step-by-Step

When you type "github.com" in your browser and hit enter, a lot happens behind the scenes. Here's the journey:

### Step 1: You Make a Request
You type "github.com" in your browser. Your computer doesn't know what IP address this is, so it needs to ask.

### Step 2: Check Local Cache
Your computer first checks if it already knows the answer. If it looked up github.com recently, it remembers the IP address and skips ahead to step 6. If not, it continues.

### Step 3: Query the Recursive Resolver
Your computer asks your ISP's DNS recursive resolver "What's the IP address for github.com?" The recursive resolver is like a helpful librarian - it will search until it finds the answer.

### Step 4: Contact the Root Nameserver
The recursive resolver asks a root nameserver: "Where can I find information about .com domains?" The root nameserver doesn't know the specific IP, but it points to the right top-level domain (TLD) nameserver.

### Step 5: Ask the TLD Nameserver
The recursive resolver now asks the TLD nameserver for .com: "Where's the nameserver for github.com?" The TLD nameserver points to the authoritative nameserver that actually knows GitHub's information.

### Step 6: Query the Authoritative Nameserver
The recursive resolver asks GitHub's authoritative nameserver: "What's the IP address for github.com?" This nameserver has the actual answer: "It's 142.250.185.46" (or whatever GitHub's current IP is).

### Step 7: Response Travels Back
The authoritative nameserver sends the IP address back to the recursive resolver, which sends it back to your computer, which sends it to your browser.

### Step 8: Browser Connects
Your browser now knows that github.com lives at that IP address, so it connects to that server and requests the website.

### Step 9: Website Loads
The web server at that IP address sends your browser the website files, which your browser displays.

### Key Points About DNS:
- **Caching:** The answer is cached at multiple levels (your computer, your ISP, etc.) so repeated lookups are instant
- **Distributed:** No single server has all the information; it's spread across many servers
- **UDP:** DNS uses UDP protocol because speed matters more than perfect reliability for lookups
- **Port 53:** All DNS communication happens on port 53
- **Domain hierarchy:** The process goes from root → TLD → authoritative nameserver, like navigating a filing system

---

## Summary

Understanding these networking fundamentals is crucial for web development, system administration, and troubleshooting. The OSI model gives you a mental framework for understanding how communication works. TCP/UDP helps you choose the right tool for different situations. Knowing common protocols and their ports helps you diagnose network issues. And understanding DNS demystifies one of the internet's core workings.

The key takeaway: networking is layered. Each layer has a job, and when data travels across the internet, it goes through all these layers, getting packaged and processed at each step.
