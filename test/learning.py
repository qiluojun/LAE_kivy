from plyer import notification
from datetime import datetime, time
import time as tm

def send_notification(remind_time, remind_content):
    """
    Send a notification at the specified remind_time with given remind_content.
    
    Args:
    remind_time (str): Target time in 'HH:MM:SS' format.
    remind_content (str): Content of the notification.
    """
    # Parse the remind_time string into a time object
    target_time = datetime.strptime(remind_time, '%H:%M:%S').time()
    
    while True:
        # Continuously check the time
        current_time = datetime.now().time()
        
        # Check if the current time is close to the target time (within one second)
        if current_time >= target_time :
            # If the time matches, send a notification
            notification.notify(
                title='Time Reminder',
                message=remind_content,
                app_name='Reminder App'
                
            )
            # Break the loop after sending the notification
            
            break
        # Sleep for a short while to avoid high CPU usage
        tm.sleep(3)

# Example usage: Uncomment the following line to test the function
send_notification('22:55:15', 'It is time to sleep!')
