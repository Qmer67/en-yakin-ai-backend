from datetime import datetime
from typing import Optional

def get_time_segment(hour: Optional[int] = None) -> str:
    """
    Zaman dilimini döner: morning / noon / evening / night
    """
    if hour is None:
        hour = datetime.now().hour

    if 6 <= hour < 11:
        return "morning"
    elif 11 <= hour < 17:
        return "noon"
    elif 17 <= hour < 23:
        return "evening"
    else:
        # 23–06 arası
        return "night"
