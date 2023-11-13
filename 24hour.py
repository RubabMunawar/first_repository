def to_24_hour_clock(hours):
    """ (number) -> number

    hours is a number of hours since midnight. Return the
    hour as seen on a 24-hour clock.

    Precondition: hours >= 0

    >>> to_24_hour_clock(24)
    0
    >>> to_24_hour_clock(48)
    0
    >>> to_24_hour_clock(25)
    1
    >>> to_24_hour_clock(4)
    4
    >>> to_24_hour_clock(28.5)
    4.5
    """

    return hours % 24

def get_hours(seconds):
    """(int)->(int)

    Seconds is a number of seconds since midnight. Return the number of hours that have elapsed since midnight, as seen on a 24-hour clock.

    precondition: seconds>=0

    >>>get_hours(3800)
    1
    >>>get_hours(15000)
    4
    >>>get_hours(86400)
    0
    """
    return (seconds//3600)%24

def get_minutes(seconds):
    """(int)->(int)

    Seconds is a number of seconds since midnight. Return the number of minutes that have elapsed since midnight, as seen on a 24-hour clock.

    precondition: seconds>=0

    >>>get_minutes(3800)
    3
    >>>get_minutes(15000)
    10
    >>>get_minutes(86400)
    0
    """
    return ((seconds//60)-(get_hours(seconds))*60)%60

def get_seconds(seconds):
    """(int)->(int)

    Seconds is a number of seconds since midnight. Return the number of seconds that have elapsed since midnight, as seen on a 24-hour clock.

    precondition: seconds>=0

    >>>get_seconds(3800)
    20
    >>>get_seconds(15000)
    0
    >>>get_seconds(86400)
    0
    """
    return (seconds-((get_hours(seconds)*3600)+(get_minutes(seconds)*60)))%60

def time_to_utc(utc_offset, time):
    """ (number, float) -> float

    Return time at UTC+0, where utc_offset is the number of hours away from
    UTC+0.

    >>> time_to_utc(+0, 12.0)
    12.0
    >>> time_to_utc(+1, 12.0)
    11.0
    >>> time_to_utc(-1, 12.0)
    13.0
    >>> time_to_utc(-11, 18.0)
    5.0
    >>> time_to_utc(-1, 0.0)
    1.0
    >>> time_to_utc(-1, 23.0)
    0.0
    """
    return (time-utc_offset)%24

def time_from_utc(utc_offset, time):
    """ (number, float) -> float

    Return UTC time in time zone utc_offset.

    >>> time_from_utc(+0, 12.0)
    12.0
    >>> time_from_utc(+1, 12.0)
    13.0
    >>> time_from_utc(-1, 12.0)
    11.0
    >>> time_from_utc(+6, 6.0)
    12.0
    >>> time_from_utc(-7, 6.0)
    23.0
    >>> time_from_utc(-1, 0.0)
    23.0
    >>> time_from_utc(-1, 23.0)
    22.0
    >>> time_from_utc(+1, 23.0)
    0.0
    """
    return (time+utc_offset)%24
