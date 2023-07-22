from .email import *
import datetime
from django.utils import timezone, dateformat
from datetime import timedelta
from django.utils.timezone import make_aware


CURRENT_YEAR = datetime.datetime.now().year
TODAY_DATE = datetime.date.today()


class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


def is_today(date):
    """[Compare today date with database date]        
    Returns:
        [bool]: [Returns True or False]
    """    
    datetime_now = timezone.localtime(timezone.now())
    return date == datetime_now.date()
    

def has_expired(date):
    """[Compare Today and Expiry Date]

    Args:
        date ([date]): [Expiry date of Coupon]

    Returns:
        [bool]: [Returns True or False]
    """   
    datetime_now = timezone.localtime(timezone.now()) 
    return date < datetime_now.date()



def format_datetime(datetime=timezone.now(), format='d/m/Y - h:i a'):
    # return dateformat.format(timezone.localtime(docket.created_at), format),
    return dateformat.format(timezone.localtime(datetime), format)

def string_to_datetime(str_date, format='%d-%m-%Y %H:%M:%S'):
    return make_aware(datetime.datetime.strptime(str_date, format))

def get_current_datetime():
    return timezone.localtime(timezone.now())

def gap_between_datetime(stored_datetime):
    datetime_now = timezone.localtime(timezone.now())
    stored_datetime = timezone.localtime(stored_datetime)
    gap  = datetime_now - stored_datetime
    days, seconds = gap.days, gap.seconds

    # minutes = divmod(gap.total_seconds(), 60)
    # print('Total difference in minutes: ', minutes[0], 'minutes', minutes[1], 'seconds')
    
    return days * 24 + seconds // 3600 # returning hour
