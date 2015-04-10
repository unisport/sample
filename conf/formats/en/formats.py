# ---- Django provided formats ----
DATE_FORMAT = 'd/m/Y'
TIME_FORMAT = 'H:i'
DATETIME_FORMAT = DATE_FORMAT + ' ' + TIME_FORMAT

DATE_INPUT_FORMATS = [
    '%d/%m/%Y',             # '25/10/2006'
    '%d/%m/%y',             # '25/10/06'
    '%Y-%m-%d',             # '2006-10-25'
]

DATETIME_INPUT_FORMATS = [
    '%d/%m/%Y %H:%M:%S',    # '25/10/2006 14:30:59'
    '%d/%m/%Y %H:%M',       # '25/10/2006 14:30'
    '%d/%m/%Y',             # '25/10/2006'

    '%d/%m/%y %H:%M:%S',    # '25/10/06 14:30:59'
    '%d/%m/%y %H:%M',       # '25/10/06 14:30'
    '%d/%m/%y',             # '25/10/06'

    '%Y-%m-%d %H:%M:%S',    # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M',       # '2006-10-25 14:30'
    '%Y-%m-%d',             # '2006-10-25'
]

# ---- Our Python formats ----
PY_DATE_FORMAT = '%d/%m/%Y' # '25/10/2006'
PY_TIME_FORMAT = '%H:%M'    # '14:30'
PY_DATETIME_FORMAT = PY_DATE_FORMAT + ' ' + PY_TIME_FORMAT
PY_MONTH_FORMAT = '%b %Y'   # 'Jan 2006'
PY_YEAR_FORMAT = '%Y'       # '2006'

# --- Our javascript formats ----
JS_DATE_FORMAT = 'd/m/Y'
JS_DATETIME_FORMAT = 'd/m/Y H:i'
