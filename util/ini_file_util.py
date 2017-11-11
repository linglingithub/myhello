from configparser import *
import os
from collections import OrderedDict

class IniFileUtil(object):
    """
    Sample usage:
    
    
        from util.ini_file_util import IniFileUtil
        params = IniFileUtil.read_into_dict("backpack_case6.ini")
        nums = IniFileUtil.string_to_int_list(params.get("nums"))
        # nums = IniFileUtil.string_to_int_list_list(params.get("nums"))   # for matrix input
        m = int(params.get("m"))
    
    """
    DATA_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data")

    @classmethod
    def read_into_dict(cls, filename):
        config = RawConfigParser(allow_no_value=True)
        data_file = os.path.join(IniFileUtil.DATA_FOLDER, filename)
        print("DEBUG ===== loading ini file: ", data_file)
        with open(data_file) as fin:
            config.readfp(fin)
            print(config.sections())
            return config._sections["data"]

    @classmethod
    def string_to_int_list(cls, instr):
        import re
        tokens = re.split(',| |\[|\]', instr)
        result = []
        # tokens = instr.split(",[]")
        for token in tokens:
            if token != "":
                result.append(int(token))
        return result

    @classmethod
    def string_to_int_list_list(cls, instr):
        """
        out put is like [[5,9], [1,3], ....]
        :param instr: 
        :return: 
        """
        import re
        tokens = re.split(',| |\[|\]', instr)
        result = []
        # tokens = instr.split(",[]")
        i = 0
        while i < len(tokens):
            if tokens[i] == '':
                i += 1
                continue
            result.append([int(tokens[i]),int(tokens[i+1])])
            i += 2
        return result