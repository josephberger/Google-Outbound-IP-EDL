# Google Outbound IP EDL

Simple http server to pull Google's outbound IPs into a Palo Alto Networks Pan-OS EDL.

[Google Document](https://support.google.com/a/answer/60764?hl=en)

## Installation

```bash
git clone https://github.com/josephberger/Google-Outbound-IP-EDL.git
cd Google-Outbound-IP-EDL
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Usage

```bash
python3 app.py -i <ip-address> -p <port>

```
