import collections
import datetime
import random
import hashlib
import string
import time

from server import logger
from server.constants import Constants, FadeOption, TargetType
from server.exceptions import ArgumentError, AreaError, ClientError, HubError, MusicError, ServerError, TaskError
from server.exceptions import PartyError, ZoneError, TrialError, NonStopDebateError
from server.client_manager import ClientManager

from typing import Union

def ooc_cmd_hub(client: ClientManager.Client, arg: str):
    """
    Either lists all hubs in the server or changes your area to a new given area.
    Returns an error if you are already in the target hub or you are unable to move to the default
    area of the new hub.

    SYNTAX
    /hub
    /hub <new_hub_numerical_id>

    PARAMETERS
    <new_hub_numerical_id>: Numerical ID of the hub

    EXAMPLES
    >>> /hub
    Lists all hubs in the server.
    >>> /hub 1
    Moves you to hub 1.
    """

    Constants.assert_command(client, arg, parameters='<2')

    args = arg.split()
    # List all hubs
    if not args:
        client.send_limited_hub_list()

    # Switch to new area
    else:
        try:
            numerical_id = int(args[0])
        except ValueError:
            raise ArgumentError('Hub ID must be a number.')

        try:
            hub = client.hub.manager.get_managee_by_numerical_id(numerical_id)
        except HubError.ManagerInvalidGameIDError:
            raise HubError.ManagerInvalidGameIDError('Hub not found.')

        if hub.invite_pass == "":
            client.change_hub(hub, from_party=(client.party is not None))
        else:
            raise HubError.ManagerInvalidGameIDError('Hub not found.')

def ooc_cmd_hub_personal(client: ClientManager.Client, arg: str):
    """
    Creates or transports the user to their own persona hub.
    The numerical ID of the hub will be the lowest non-taken numerical hub ID.

    SYNTAX
    /hub_personal

    PARAMETERS
    None

    OPTIONAL PARAMETERS
    None

    EXAMPLES
    Assuming that two hubs with numerical IDs 0 and 2 respectively exist...
    >>> /hub_personal
    Creates hub with numerical ID 1.
    """

    user_id = client.discord_id
    if user_id is 0:
        user_id = client.hdid


    hub = None
    for i, hub_iterate in client.hub.manager.get_managee_numerical_ids_to_managees().items():
        if hub_iterate.owner_id == user_id:
            hub = hub_iterate
            break

    if hub == None:
        hub = client.hub.manager.new_managee()
        hub.owner_id = user_id

        hub.set_name(f'{client.name}\'s Personal Hub')

        letters = string.ascii_letters + string.digits
        hub.invite_pass = ''.join(random.choice(letters) for i in range(6))
        hub.is_temporary = False
        hub.allowed_clients.append(client.ipid)

    client.send_music_list_view()
    client.change_hub(hub, from_party=(client.party is not None))
    client.send_ooc(f'You are now in your personal hub {hub.get_numerical_id()}.\nThe access code is `{hub.get_id()[1:]}_{hub.invite_pass}`.\n\nYour GM login password is {hub.get_password()}. Only share this with people you trust. If you wish to make this hub public, please contact a moderator.')
    client.send_ooc_others(f'{client.name} [{client.id}] created personal hub {hub.get_numerical_id()}.',
                               is_officer=True, in_hub=None)

def ooc_cmd_hub_create(client: ClientManager.Client, arg: str):
    """ (OFFICER ONLY)
    Creates a new hub with the given name, or with a default generated name if not given one.
    The numerical ID of the hub will be the lowest non-taken numerical hub ID.

    SYNTAX
    /hub_create {name}

    PARAMETERS
    None

    OPTIONAL PARAMETERS
    {name}: Name of the hub

    EXAMPLES
    Assuming that two hubs with numerical IDs 0 and 2 respectively exist...
    >>> /hub_create
    Creates hub with numerical ID 1.
    >>> /hub_create hubby hub
    Creates hub with numerical ID 3 and name "hubby hub".
    """

    Constants.assert_command(client, arg, is_officer=True)

    hub = client.hub.manager.new_managee()
    if arg:
        hub.set_name(arg)

    for target in client.server.get_clients():
        target.send_music_list_view()

    if arg:
        client.send_ooc(
            f'You created hub {hub.get_numerical_id()} with name {hub.get_name()}.')
        client.send_ooc_others(f'{client.name} [{client.id}] created hub {hub.get_numerical_id()} '
                               f'with name {hub.get_name()}.', is_officer=True, in_hub=None)
    else:
        client.send_ooc(f'You created hub {hub.get_numerical_id()}.')
        client.send_ooc_others(f'{client.name} [{client.id}] created hub {hub.get_numerical_id()}.',
                               is_officer=True, in_hub=None)


def ooc_cmd_hub_end(client: ClientManager.Client, arg: str):
    """ (VARYING REQUIREMENTS)
    (STAFF ONLY) Deletes the current hub if not given a numerical ID, or
    (OFFICER ONLY) of the given hub by numerical ID.
    Players in the deleted hub are moved to the default hub of the server.
    Returns an error if given a numerical ID and it is not the numerical ID of a hub in the server,
    or if the server has only one hub.

    SYNTAX
    /hub_end
    /hub_end <hub_id>

    PARAMETERS
    <hub_id>: Numerical ID

    EXAMPLES
    >>> /hub_end
    Deletes the current hub.
    >>> /hub_end 2
    Deletes the hub with numerical ID 2.
    """

    try:
        Constants.assert_command(client, arg, is_officer=True, parameters='<2')
    except ClientError.UnauthorizedError:
        Constants.assert_command(client, arg, is_staff=True, parameters='=0')

    if not arg:
        arg = client.hub.get_numerical_id()

    try:
        hub = client.hub.manager.get_managee_by_numerical_id(arg)
    except HubError.ManagerInvalidGameIDError:
        raise ClientError(f'Hub {arg} not found.')

    try:
        client.hub.manager.delete_managee(hub)
    except HubError.ManagerCannotManageeNoManagees:
        raise ClientError(
            f'You cannot delete a hub when it is the only one of the server.')

    for target in client.server.get_clients():
        target.send_music_list_view()

    client.send_ooc(f'You deleted hub {hub.get_numerical_id()}.')
    client.send_ooc_others(f'{client.name} [{client.id}] deleted hub {hub.get_numerical_id()}.',
                           is_officer=True, in_hub=None)


def ooc_cmd_hub_info(client: ClientManager.Client, arg: str):
    """ (VARYING REQUIREMENTS)
    (STAFF ONLY) Return information about the current hub if not given a numerical ID, or
    (OFFICER ONLY) of the given hub by numerical ID.
    Returns an error if given a numerical ID and it is not the numerical ID of a hub in the server.

    SYNTAX
    /hub_info
    /hub_info <hub_id>

    PARAMETERS
    <hub_id>: Numerical ID

    EXAMPLES
    >>> /hub_info
    May return something like this:
    | [17:34] $H: == Hub 0 ==
    | *GMs: 1. NonGMs: 0
    | *Area list: config/areas.yaml
    | *Background list: config/bg_lists/beach.yaml
    | *Character list: config/char_lists/custom.yaml
    | *DJ list: config/music.yaml
    """

    try:
        Constants.assert_command(client, arg, is_officer=True, parameters='<2')
    except ClientError.UnauthorizedError:
        Constants.assert_command(client, arg, is_staff=True, parameters='=0')

    if not arg:
        arg = client.hub.get_numerical_id()

    try:
        hub = client.hub.manager.get_managee_by_numerical_id(arg)
    except HubError.ManagerInvalidGameIDError:
        raise ClientError(f'Hub {arg} not found.')

    info = hub.get_info()
    client.send_ooc(info)


def ooc_cmd_hub_password(client: ClientManager.Client, arg: str):
    """ (STAFF ONLY)
    Changes the hub password.

    SYNTAX
    /hub_password <password>

    PARAMETERS
    <password>: New password

    EXAMPLES
    >>> /hub_password 11037
    Sets the hub password to 11037.
    """

    Constants.assert_command(client, arg, is_staff=True, parameters='>0')

    client.hub.set_password(arg)
    client.send_ooc('You have changed the password of your hub.')
    client.send_ooc_others(f'(X) {client.displayname} [{client.id}] changed the password of your '
                           f'hub. Do /hub_password_info to retrieve it.',
                           is_zstaff_flex=True, is_officer=False)
    hid = client.hub.get_numerical_id()
    client.send_ooc_others(f'{client.name} [{client.id}] changed the password of hub {hid}. Do '
                           f'/hub_password_info {hid} to retrieve it.',
                           is_officer=True, in_hub=None)


def ooc_cmd_hub_password_info(client: ClientManager.Client, arg: str):
    """ (VARYING REQUIREMENTS)
    (STAFF ONLY) Gets the password of the current hub or, (OFFICER ONLY) the given hub by numerical
    ID.
    Returns an error if given a numerical ID and it is not the numerical ID of a hub in the server.

    SYNTAX
    /hub_password_info
    /hub_password_info <hub_id>

    PARAMETERS
    <hub_id>: Numerical ID

    EXAMPLES
    >>> /hub_password_info
    May return something like this:
    | $H: The hub password is `2124`.
    """

    try:
        Constants.assert_command(client, arg, is_officer=True, parameters='<2')
    except ClientError.UnauthorizedError:
        Constants.assert_command(client, arg, is_staff=True, parameters='=0')

    if not arg:
        arg = client.hub.get_numerical_id()

    try:
        hub = client.hub.manager.get_managee_by_numerical_id(arg)
    except HubError.ManagerInvalidGameIDError:
        raise ClientError(f'Hub {arg} not found.')

    password = hub.get_password()
    client.send_ooc(f'The hub password is `{password}`.')

def ooc_cmd_hub_invite_info(client: ClientManager.Client, arg: str):

    Constants.assert_command(client, arg, is_staff=True)

    if not arg:
        arg = client.hub.get_numerical_id()

    try:
        hub = client.hub.manager.get_managee_by_numerical_id(arg)
    except HubError.ManagerInvalidGameIDError:
        raise ClientError(f'Hub {arg} not found.')

    client.send_ooc(f'The access code for the hub is `{hub.get_id()[1:]}_{hub.invite_pass}`.')

def ooc_cmd_hub_rename(client: ClientManager.Client, arg: str):
    """ (STAFF ONLY)
    Changes the name of a hub by its numerical ID if given a name, or clears it if not given one.

    SYNTAX
    /hub_rename
    /hub_rename <name>

    PARAMETERS
    <name>: Name

    EXAMPLES
    >>> /hub_rename Great Hub
    Changes the name of the hub to Great Hub.
    >>> /hub_rename
    Clears the name of the hub.
    """

    Constants.assert_command(client, arg, is_staff=True)

    hub = client.hub
    hub.set_name(arg)

    if arg:
        client.send_ooc(f'You have renamed your hub to `{arg}`.')
        client.send_ooc_others(f'{client.displayname} [{client.id}] renamed your hub to `{arg}` '
                               f'({client.area.id}).', is_zstaff_flex=True)
    else:
        client.send_ooc('You have cleared the name of your hub.')
        client.send_ooc_others(f'{client.displayname} [{client.id}] cleared the name of your hub '
                               f'({client.area.id}).', is_zstaff_flex=True)

    for target in client.server.get_clients():
        target.send_music_list_view()

def ooc_cmd_hub_privatize(client: ClientManager.Client, arg: str):
    Constants.assert_command(client, arg, is_staff=True)

    letters = string.ascii_letters + string.digits
    client.hub.invite_pass = ''.join(random.choice(letters) for i in range(6))
    client.send_ooc('You have privatized the hub. The new password is `{}_{}`.'.format(client.hub.get_id()[1:], client.hub.invite_pass))

def ooc_cmd_hub_publicize(client: ClientManager.Client, arg: str):
    Constants.assert_command(client, arg, is_officer=True)

    client.hub.invite_pass = ''
    client.hub.owner_id = -1
    client.send_ooc('You have publicized the hub. It is now accessible to everyone.')

def ooc_cmd_hub_access(client: ClientManager.Client, arg: str):
    
    args = arg.split('_')
    
    hub_id, password = args

    try:
        hub = client.hub.manager.get_managee_by_numerical_id(hub_id)
    except HubError.ManagerInvalidGameIDError:
        raise ClientError(f'Password {arg} does not belong to any hubs.')

    if hub.invite_pass != password:
        raise ClientError(f'Password {arg} does not belong to any hubs.')

    if client.ipid in hub.allowed_clients:
        client.send_ooc('You already have access to the hub `{}`.'.format(hub.get_name()))
        return

    hub.allowed_clients.append(client.ipid)
    client.send_ooc('You have gained access to the hub `{}`.'.format(hub.get_name()))
    client.change_hub(hub, from_party=(client.party is not None))

def ooc_cmd_hub_toggle_streaming(client: ClientManager.Client, arg: str):
    Constants.assert_command(client, arg, is_staff=True)

    client.hub.allow_streaming = not client.hub.allow_streaming
    status = 'enabled' if client.hub.allow_streaming else 'disabled'
    client.send_ooc(f'You have {status} music streaming in the hub.')

def ooc_cmd_hub_toggle_global(client: ClientManager.Client, arg: str):
    Constants.assert_command(client, arg, is_staff=True)

    client.hub.allow_global = not client.hub.allow_global
    status = 'enabled' if client.hub.allow_global else 'disabled'
    client.send_ooc(f'You have {status} hub wide global chat.')
