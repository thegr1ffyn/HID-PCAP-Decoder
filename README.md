# HID-PCAP Decoder

## Overview
`HID-PCAP Decoder` is a Python-based tool designed to extract and decode HID (Human Interface Device) data from USB packets in Wireshark `.pcap` files. It translates HID keycodes into readable text, allowing you to analyze USB keyboard input captured in network packet dumps.

---

## Features
- Extracts USB HID data directly from `.pcap` files.
- Decodes keycodes into readable characters, including support for:
  - Lowercase and uppercase letters.
  - Numbers and special characters.
  - Arrow keys and other common keys.
- Handles shifted key inputs (e.g., Shift + Key).
- User-friendly error handling for missing files and invalid inputs.

---

## Requirements
- Python 3.x
- Scapy library

Install Scapy using pip:
```bash
pip install scapy
```

---

## Usage
1. Capture USB traffic with Wireshark and save it as a `.pcap` file.
2. Run the decoder tool:

```bash
python hid_pcap_decoder.py [pcap_file]
```

Replace `[pcap_file]` with the path to your `.pcap` file containing USB traffic.

### Example:
```bash
python hid_pcap_decoder.py usb_traffic.pcap
```

Output will display the decoded characters based on the HID keycodes in the `.pcap` file.

---

## How It Works
1. **Packet Reading**:
   - The tool uses Scapy to parse `.pcap` files.
   - Filters for USB HID packets.

2. **HID Data Decoding**:
   - Processes HID reports to extract keycodes.
   - Uses predefined key mappings for decoding.

3. **Output**:
   - Prints the translated characters in sequence.

---

## Contribution
Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests.

---

## License
This project is licensed under the MIT License.
