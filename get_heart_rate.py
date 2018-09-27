from base import MiBand2

with open('mac.txt') as f:
    MAC = f.read()

band = MiBand2(MAC, debug=True)
band.setSecurityLevel(level="medium")
band.authenticate()

heart = band.start_raw_data_realtime()
print(heart)
band.disconnect()
