from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_page(self):

        self.browser.get('http://localhost:8000')

        # Name and header site
        self.assertIn('nogotki', self.browser.title)

        # We need our magic button Fast Enroll
        enroll_button = self.browser.find_element_by_id('fast_enroll')

        # Push the button
        enroll_button.click()

        # First, we need form to contact form
        enroll_form = self.browser.find_element_by_tag_name('form')

        # In form inputbox I write my phone number
        phone_inputbox = enroll_form.find_element_by_name('phone_number')
        phone_inputbox.send_keys('0931375857')

        # And submit it by button "Call me!"
        enroll_form.submit()

        self.assertIn('Thank you! We call you in 30 minutes!', self.browser.find_element_by_tag_name('h1').text)

        self.fail('Finish the test')


if __name__ == '__main__':
    unittest.main(warnings='ignore')




