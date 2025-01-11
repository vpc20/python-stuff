def validate_ip_addr(s):
    numxs = s.split('.')
    if len(numxs) != 4:
        return False
    return all([numx.isdigit() and 0 <= int(numx) <= 255 for numx in numxs])


# ip = '255.255.255.255'
# ip = '0.0.0.0'
# ip = '192.168.0.1'
# ip = '192.168.0.'
ip = '...'
print(validate_ip_addr(ip))
