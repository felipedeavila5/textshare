from mock import MagicMock
from text.permissions import NotListOrIsAuthenticated
from conftest import user, user_anonymous


def test_creation_or_auth_not_has_permission(db, user_anonymous):
    """
    An authenticated user should have permissions
    """
    ic = NotListOrIsAuthenticated()
    request = MagicMock(user=user_anonymous)
    view = MagicMock(action="list")
    assert ic.has_permission(request=request, view=view) == False


def test_creation_or_auth_has_permission(db, user):
    """
    An authenticated user should have permissions
    """
    ic = NotListOrIsAuthenticated()
    request = MagicMock(user=user)
    view = MagicMock(action="list")
    assert ic.has_permission(request=request, view=view) == True
