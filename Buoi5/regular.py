import re

line = 'the wheel on the bus go round, round and round, round and round'

matchObj = re.match(r'(.*) go (.*?).*', line, re.M|re.I)


if matchObj:
    print(matchObj)
else:
    pass
    # Do some thing