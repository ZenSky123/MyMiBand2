import sys
from base import MiBand2

MAC = sys.argv[1]

band = MiBand2(MAC, debug=True)
band.setSecurityLevel(level="medium")
band.authenticate()

# if len(sys.argv) > 2:
#     if band.initialize():
#         print("Init OK")
#     band.set_heart_monitor_sleep_support(enabled=False)
#     band.disconnect()
#     sys.exit(0)
# else:
#     band.authenticate()

# print 'Message notif'
# band.send_alert(ALERT_TYPES.MESSAGE)
# time.sleep(3)
# this will vibrate till not off
# print 'Phone notif'
# band.send_alert(ALERT_TYPES.PHONE)
# time.sleep(8)
# print 'OFF'
# band.send_alert(ALERT_TYPES.NONE)
print 'Soft revision:', band.get_revision()
print 'Hardware revision:', band.get_hrdw_revision()
print 'Serial:', band.get_serial()
print 'Battery:', band.get_battery_info()
print 'Time:', band.get_current_time()
print 'Steps:', band.get_steps()



# band.start_heart_rate_realtime(heart_measure_callback=l)
heart = band.start_raw_data_realtime()
print(heart)
# for i in range(10):
#     print(heart.next())
band.disconnect()

# Soft revision: V1.0.1.81
# Hardware revision: V0.1.3.2
