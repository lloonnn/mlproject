import sys
import logging

'''
Exception Type: <class 'ZeroDivisionError'>
Exception value: division by zero
Traceback details:
    File "<path_to_your_file>", line X, in <module>
        1 / 0
'''

def error_message_detail(error, error_detail: sys):
    exc_type, exc_value, exc_traceback = error_detail.exc_info()
    file_name = exc_traceback.tb_frame.f_code.co_filename
    error_message = "Error occurec in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, 
        exc_traceback.tb_lineno, 
        str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    


