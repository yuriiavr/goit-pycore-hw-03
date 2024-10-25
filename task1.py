from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        target_date = datetime.strptime(date, '%Y-%m-%d')
        
        current_date = datetime.today()
        
        delta = current_date - target_date
        
        return delta.days
    except ValueError as e:
        print(f"Не правильний формат дати: {e}")
        return None

print(get_days_from_today("2025-10-09"))