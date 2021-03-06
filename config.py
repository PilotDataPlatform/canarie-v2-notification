# flask configs
class ConfigClass(object):
    # the packaged modules
    api_modules = ["service_email"]
    postfix = 'mailout.easydns.com'
    smtp_user = 'oit.on.ca'
    smtp_pass = '1991alex'
    smtp_port = 587

    POSTFIX_URL = "external-postfix.utility"
    POSTFIX_PORT = 25

    ALLOWED_EXTENSIONS = set(['pdf', 'png', 'jpg', 'jpeg', 'gif'])
    IMAGE_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
