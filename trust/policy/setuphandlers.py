from Products.CMFCore.utils import getToolByName

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
        package for package in packages if installer.isProductInstalled(package)]
    installer.uninstallProducts(packages)


def exclude_from_nav(context):
    portal = context.getSite()
    ids = ['news', 'events', 'Members']
    for oid in ids:
        obj = portal.get(oid)
        obj.setExcludeFromNav(True)
        obj.reindexObject()


def set_member_area_type(context):
    """Set member area type to trust.content.MemberSite."""
    portal = context.getSite()
    membership = getToolByName(portal, 'portal_membership')
    membership.setMemberAreaType('trust.content.MemberSite')


def setupVarious(context):

    if context.readDataFile('trust.policy_various.txt') is None:
        return

    uninstall_package(context, ['plonetheme.classic'])
    exclude_from_nav(context)
    set_member_area_type(context)
