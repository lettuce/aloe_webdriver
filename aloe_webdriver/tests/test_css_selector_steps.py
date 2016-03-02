"""Test CSS selector steps."""

from aloe.testing import FeatureTest

from aloe_webdriver.tests.base import feature


class TestCSS(FeatureTest):
    """Test CSS steps."""

    @feature()
    def test_css_match(self):
        # pylint:disable=line-too-long
        """
        When I go to "{basic_page}"
        Then There should be an element matching $("textarea[name='bio']") within 1 second
        """
        # pylint:enable=line-too-long

    @feature()
    def test_forms(self):
        """
        When I go to "{basic_page}"
        Then I fill in $("input[name='user']") with "A test string"
        And I check $("input[value='Bike']")
        """
