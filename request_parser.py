
##################
# REQUEST PARSER #
##################

valid_auth_tokens = ["ah37j2ha483u", "safh34ywb0p5", "ba34wyi8t902"]
requests = [
    ["GET", "https://example.com/?token=347sd6yk8iu2&name=alex"],
    ["GET", "https://example.com/?token=safh34ywb0p5&name=sam"],
    ["POST", "https://example.com/?token=safh34ywb0p5&name=alex"],
    ["POST", "http://example.com.at/?name=alex&token=safh34ywb0p5"],
    ["POST", "http://example.com.at/?name=alex&token=safh34ywb0p5&csrf=sAfh347wb"],
    ["POST", "http://example.com.at/?name=alex&token=safh34ywb0p5&csrf=safhwb"],
    ["POST", "http://example.com.at/?name=alex&token=safh34ywb0p5&csrf=saddkdjdythj"],
    ["POST", "http://example.com.at/?name=alex&token=safh34ywb0p5&csrf="],
    ["POST", "https://example.com/?token=safh34ywb0p5&csrf=ak2sh32dy&name=chris"],
]

def get_url_parameters(url):
    import re

    URL_REGEX = re.compile(r'''
        https?://
        \w+
        [.\w+]+/
        \?
        (.*)
    ''', re.VERBOSE)

    return URL_REGEX.search(url).group(1)


def request_parser(valid_auth_tokens, requests):
    responses = []
    for action, url in requests:
        url_parameters = get_url_parameters(url)
        parameters = url_parameters.split("&")

        param_dict = {}
        valid_string = ""
        for parameter in parameters:
            key, value = parameter.split("=")
            valid_string += "," + key + "," + value
            param_dict[key] = value

        if param_dict.get("token") not in valid_auth_tokens:
            responses.append("INVALID")
            continue

        if action == "POST":
            csrf = param_dict.get("csrf")
            if not (csrf and csrf.isalnum() and csrf.islower() and len(csrf) >= 8):
                responses.append("INVALID")
                continue

        responses.append("VALID" + valid_string)

    return responses

print(request_parser(valid_auth_tokens, requests))
