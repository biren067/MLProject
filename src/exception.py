import sys
import logging

def get_error_message(error,error_message_detail:sys):
    _,_,err = error_message_detail.exc_info()
    filename= err.tb_frame.f_code.co_filename
    lineno=err.tb_lineno
    error_info = "Error occured in python script \n FileName::{0}\n LineNo: {1}\n Message:{2}".format(filename,lineno,error)
    return error_info

class CustomException(Exception):
    def __init__(self,error_message,error_message_detail:sys):
        super().__init__(error_message)
        self.error_message = get_error_message(error_message,error_message_detail)

        # return self.error_message

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    # logging.info("Logging started...")
    try:
        a = 1 / 0
    except Exception as e:
        # logging.info("Divide by Zeor")
        raise CustomException(e,sys)

    