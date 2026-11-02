# Persistent Network Keylogger Suite

A complete toolkit consisting of two client variants (instant streaming vs. local logging with periodic uploads) and a persistent Bash listener script to receive data via Netcat.


## Requirements

Make sure you have the required Python library installed on the client machine:
```bash
pip install pynput
```


## 1. Client Variants

### Option A: Instant Stream (`keylogger.py`)

This script captures keystrokes (`pynput`) and immediately sends every single keystroke event over a TCP socket connection to the remote server.

**Usage:**
```bash
python keylogger.py
```


### Option B: Local Log & Periodic Upload (`keylogger_log.py`)

This version is more discreet and robust against connection drops. It writes keystrokes locally to a file (`keylog.txt`) and uses a background thread (`threading`) to send the accumulated log file to the server at regular intervals (default: every 10 seconds), clearing the file afterward.

**Configuration (inside code):**
* `LOG_FILE`: Name of the local log file (default: `"keylog.txt"`).
* `SERVER_IP` & `SERVER_PORT`: Destination address and port.


**Usage:**
```bash
python keylogger_log.py
```

*Note for both:* Press **Esc** to stop the local listener.


## 2. Server Listener Script (`persistent_nc.sh`)

A persistent Bash script designed to run on the server. It runs Netcat in an infinite loop (`nc -lvnp`), so whenever a connection closes or drops, it immediately starts listening again for incoming logs.

### Configuration

Edit the port variable inside the script:

* `PORT`: The port number to listen on (must match the client's port).

### Usage

Make the script executable and run it:

```bash
chmod +x persistent_nc.sh
./persistent_nc.sh

```

## Summary of Components

| Component | Type | Description |
| --- | --- | --- |
| `keylogger.py` | Python Script | Streams keystrokes instantly over TCP as they occur. |
| `keylogger_log.py` | Python Script | Saves keystrokes to a local file (`keylog.txt`) and flushes/sends them periodically via background thread. |
| `persistent_nc.sh` | Bash Script | Runs a persistent Netcat listener loop to catch incoming logs safely (`Ctrl+C` handled). |


