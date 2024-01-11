import bcrypt

from src.general.response import error_response, get_message
from config.logger import logger


def get_hash_password(first_name, mobile: str = None):
    """
    This function will generate password from the combination of first name and @ and mobile
    first_name: Tirth
    mobile: 1234567890
    password: Tirt@7890
    """
    try:
        first_name = first_name.replace(" ", "")
        if len(first_name) < 4:
            name = first_name + '#' if len(first_name) == 3 else first_name + '##' \
                if len(first_name) == 2 else first_name + '###'
        else:
            name = first_name[0:4]
        if mobile:
            mobile = "".join([i for i in mobile if i.isalnum()])
        else:
            mobile = "####"
        result_str = name.capitalize() + '@' + mobile[-4:]
        result = bcrypt.hashpw(result_str.strip().encode("utf-8"), bcrypt.gensalt(rounds=4))
        return result, result_str
    except Exception as e:
        logger.error(f"Internal server error: {e.args}")
        return error_response(get_message("internal_server", "internal"), 500)
