def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        
        if minutes == 60:
            minutes = 0
            hour += 1
            
        h = (hour*60+minutes)*0.5
        m = minutes*6
        
        angle = abs(h-m)
        
        return min(360-angle,angle)
