class CidrMaskConvert:

    def cidr_to_mask(self, val):
        val = int(val)
        if 1 > val or val > 32:
            return "Invalid"
        val = '.'.join([str((0xffffffff << (32 - val) >> i) & 0xff)
                    for i in [24, 16, 8, 0]])
        return val

    def mask_to_cidr(self, val):
        mask_list = val.split(".")
        check =  IpValidate().ipv4_validation(val)
        binary = [bin(int(i))[2:].count('1') for i in mask_list]
        if not check or binary[0] ==3:
            return 'Invalid'
        val = sum(binary) if sum(binary) > 0 else 'Invalid'
        return  str(val)

class IpValidate:

    def ipv4_validation(self, val):

        octets = val.split(".")
        return len(octets) == 4 and \
           all(o.isdigit() and 0 <= int(o) < 256 for o in octets)
