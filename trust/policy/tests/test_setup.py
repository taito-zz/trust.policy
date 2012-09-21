from Products.CMFCore.utils import getToolByName
from trust.policy.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_trust_policy_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('trust.policy'))

    def test_browserlayer(self):
        from trust.policy.browser.interfaces import ITrustPolicyLayer
        from plone.browserlayer import utils
        self.failUnless(ITrustPolicyLayer in utils.registered_layers())

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['trust.policy'])
        self.failIf(installer.isProductInstalled('trust.policy'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['trust.policy'])
        from trust.policy.browser.interfaces import ITrustPolicyLayer
        from plone.browserlayer import utils
        self.failIf(ITrustPolicyLayer in utils.registered_layers())
