apt update && apt upgrade -y
apt install python
apt install w3m
pip install -r tools/doc/requirements.txt
mv tools/hio.py .
chmod +x hio.py
rm -rf package.sh
python hio.py