from Products.CMFCore.utils import getToolByName
from plone.app.controlpanel.security import ISecuritySchema

import logging


logger = logging.getLogger(__name__)


def uninstall_package(context, packages):
    """Uninstall packages.

    :param packages: List of package names.
    :type packages: list
    """
    portal = context.getSite()
    installer = getToolByName(portal, 'portal_quickinstaller')
    packages = [
        package for package in packages if installer.isProductInstalled(package)
    ]
    installer.uninstallProducts(packages)

def remove_front_page(context):
    portal = context.getSite()
    if portal.get('front-page'):
        portal.manage_delObjects(['front-page'])


def setupVarious(context):

    if context.readDataFile('trust.policy_various.txt') is None:
        return

    uninstall_package(context, ['plonetheme.classic'])
    ISecuritySchema(context.getSite()).set_enable_user_folders(True)
    remove_front_page(context)
