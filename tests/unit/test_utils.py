from django.test import TestCase, override_settings


@override_settings(
    SECURE_MAIL_GNUPG_ENCODING=None)
class GetGPGTestCase(TestCase):
    def test_get_gpg_default_encoding(self):
        from secure_mail import utils
        previous_value = utils.GNUPG_ENCODING
        try:
            utils.GNUPG_ENCODING = None
            gpg_obj = utils.get_gpg()
        finally:
            utils.GNUPG_ENCODING = previous_value

        self.assertEquals(gpg_obj.encoding, 'latin-1')
