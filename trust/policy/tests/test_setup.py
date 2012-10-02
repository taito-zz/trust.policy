from Products.CMFCore.utils import getToolByName
from trust.policy.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_is_package_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('trust.policy'))

    def test_is_trust_content_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('trust.content'))

    def test_is_trust_template_installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('trust.template'))

    def test_browserlayer(self):
        from trust.policy.browser.interfaces import ITrustPolicyLayer
        from plone.browserlayer import utils
        self.assertIn(ITrustPolicyLayer, utils.registered_layers())

    def test_cssregistry(self):
        css = getToolByName(self.portal, 'portal_css')
        self.assertFalse(css.getResource(
            '++resource++plone.app.jquerytools.overlays.css').getEnabled())

    def test_jsregistry__popupforms(self):
        javascripts = getToolByName(self.portal, 'portal_javascripts')
        self.assertFalse(javascripts.getResource('popupforms.js').getEnabled())

    def test_mailhost__smtp_host(self):
        mailhost = getToolByName(self.portal, 'MailHost')
        self.assertEqual(mailhost.smtp_host, 'smtp.gmail.com')

    def test_mailhost__smtp_port(self):
        mailhost = getToolByName(self.portal, 'MailHost')
        self.assertEqual(mailhost.smtp_port, 587)

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(
            setup.getVersionForProfile('profile-trust.policy:default'), u'0')

    def test_properties_title(self):
        self.assertEqual(self.portal.getProperty('title'), 'ABITA')

    def test_properties_description(self):
        self.assertEqual(
            self.portal.getProperty('description'),
            'Open Source Technologies for Open Mind(ed)')

    def test_properties__email_from_address(self):
        self.assertEqual(self.portal.getProperty('email_from_address'), 'info@abita.fi')

    def test_properties__email_from_name(self):
        self.assertEqual(self.portal.getProperty('email_from_name'), 'ABITA')

    def test_propertiestool__site_properties__external_links_open_new_window(self):
        properties = getattr(getToolByName(self.portal, 'portal_properties'), 'site_properties')
        self.assertEqual(properties.getProperty('external_links_open_new_window'), 'true')

    def test_propertiestool__site_properties__mark_special_links(self):
        properties = getattr(getToolByName(self.portal, 'portal_properties'), 'site_properties')
        self.assertEqual(properties.getProperty('mark_special_links'), 'true')

    def test_propertiestool__site_properties__use_email_as_login(self):
        properties = getattr(getToolByName(self.portal, 'portal_properties'), 'site_properties')
        self.assertTrue(properties.getProperty('use_email_as_login'))

    def test_setuphandlers__uninstall_package__plonetheme_classic(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertFalse(installer.isProductInstalled('plonetheme.classic'))

    def test_setuphanders__set_enable_user_folders(self):
        from plone.app.controlpanel.security import ISecuritySchema
        self.assertTrue(ISecuritySchema(self.portal).get_enable_user_folders())

    def test_setuphandlers_exclude_from_nav(self):
        ids = ['news', 'events', 'Members']
        for oid in ids:
            self.assertTrue(self.portal[oid].getExcludeFromNav())

    def test_set_member_area_type(self):
        membership = getToolByName(self.portal, 'portal_membership')
        self.assertEqual(membership.memberarea_type, 'trust.content.MemberSite')

    def test_tinymce__link_using_uids(self):
        tinymce = getToolByName(self.portal, 'portal_tinymce')
        self.assertTrue(tinymce.link_using_uids)

    def test_uninstall__package(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['trust.policy'])
        self.assertFalse(installer.isProductInstalled('trust.policy'))

    def test_uninstall__browserlayer(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['trust.policy'])
        from trust.policy.browser.interfaces import ITrustPolicyLayer
        from plone.browserlayer import utils
        self.assertNotIn(ITrustPolicyLayer, utils.registered_layers())
