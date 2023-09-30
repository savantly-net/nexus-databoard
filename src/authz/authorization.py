from streamlit.web.server.websocket_headers import _get_websocket_headers
from .user import User
from config import dev_mode, dev_role


def _anonymous_user():
  return User(None, [])

def _extractRolesFromHeader():
  headers = _get_websocket_headers()
  roles = headers.get("X-Forwarded-Groups")
  if roles is None:
    return []
  else:
    return roles.upper().split(",")

def _getUserFromHeader():
  headers = _get_websocket_headers()
  email = headers.get("X-Forwarded-Email")
  if email is None:
    return _anonymous_user()
  else:
    return User(email, _extractRolesFromHeader())

def get_current_user() -> User:
  if dev_mode:
    return User("dev@savantly", [dev_role])
  return _getUserFromHeader()