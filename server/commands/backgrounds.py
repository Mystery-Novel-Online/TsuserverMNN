from server import logger
from server.constants import Constants, FadeOption, TargetType
from server.exceptions import ArgumentError, AreaError, ClientError, HubError, MusicError, ServerError, TaskError
from server.exceptions import PartyError, ZoneError, TrialError, NonStopDebateError
from server.client_manager import ClientManager

def ooc_cmd_bg(client: ClientManager.Client, arg: str):
    """
    Changes the background of the current area.
    Returns an error if area background is locked and you are unathorized or if the sought
    background does not exist.

    SYNTAX
    /bg <background_name>

    PARAMETERS
    <background_name>: New background name, possibly with spaces (e.g. Principal's Room)

    EXAMPLES
    >>> /bg Principal's Room
    Changes background to Principal's Room
    """

    try:
        Constants.assert_command(client, arg, parameters='>0')
    except ArgumentError:
        raise ArgumentError('You must specify a name. Use /bg <background>.')
    if not client.is_mod and client.area.bg_lock:
        raise AreaError("This area's background is locked.")

    client.area.change_background(arg, validate=not (
        client.is_staff() or client.area.cbg_allowed))
    client.area.broadcast_ooc('{} changed the background to {}.'
                              .format(client.displayname, arg))
    logger.log_server('[{}][{}]Changed background to {}'
                      .format(client.area.id, client.get_char_name(), arg), client)

def ooc_cmd_bglock(client: ClientManager.Client, arg: str):
    """ (MOD ONLY)
    Toggles background changes by non-mods in the current area being allowed/disallowed.

    SYNTAX
    /bglock

    PARAMETERS
    None

    EXAMPLES
    Assuming the current area's background is unlocked
    >>> /bglock
    Locks the background.
    >>> /bglock
    Unlocks the background.
    """

    Constants.assert_command(client, arg, is_mod=True, parameters='=0')

    client.area.bg_lock = not client.area.bg_lock
    client.area.broadcast_ooc('A mod has set the background lock to {}.'
                              .format(client.area.bg_lock))
    logger.log_server('[{}][{}]Changed bglock to {}'
                      .format(client.area.id, client.get_char_name(), client.area.bg_lock), client)

def ooc_cmd_bg_period(client: ClientManager.Client, arg: str):
    """ (STAFF ONLY)
    Changes the background of the current area associated with the given period.
    Returns an error if area background is locked and you are unathorized or if the sought
    background does not exist.

    SYNTAX
    /bg_period <period_name> <background_name>

    PARAMETERS
    <period_name>: Period name
    <background_name>: New background name, possibly with spaces (e.g. Principal's Room)

    EXAMPLES
    >>> /bg_period night Beach (night)
    Changes background to Beach (night) whenever the area has a night period active.
    """

    Constants.assert_command(client, arg, is_staff=True, parameters='>1')
    if not client.is_mod and client.area.bg_lock:
        raise AreaError("This area's background is locked.")

    args = arg.split()
    tod_name = args[0]
    bg_name = ' '.join(args[1:])

    client.area.change_background_tod(bg_name, tod_name, validate=False)
    client.send_ooc(f'You changed the background associated with period `{tod_name}` to '
                    f'`{bg_name}`.')
    client.send_ooc_others(f'(X) {client.displayname} [{client.id}] changed the background '
                           f'associated with period `{tod_name}` to `{bg_name}`.',
                           is_zstaff_flex=True)
    logger.log_server('[{}][{}]Changed background associated with period `{}` to {}'
                      .format(client.area.id, client.get_char_name(), tod_name, bg_name), client)

def ooc_cmd_bg_period_end(client: ClientManager.Client, arg: str):
    """ (STAFF ONLY)
    Removes the background of the current area associated with the given period
    Returns an error if area background is locked and you are unathorized or if the sought
    background does not exist.

    SYNTAX
    /bg_period_end <period_name>

    PARAMETERS
    <period_name>: Period name

    EXAMPLES
    >>> /bg_period_end night
    Removes the background associated with the night period of the current area.
    """

    Constants.assert_command(client, arg, is_staff=True, parameters='=1')
    if not client.is_mod and client.area.bg_lock:
        raise AreaError("This area's background is locked.")

    client.area.change_background_tod('', arg, validate=False)
    client.send_ooc(
        f'You removed the background associated with period `{arg}`.')
    client.send_ooc_others(f'(X) {client.displayname} [{client.id}] removed the background '
                           f'associated with period `{arg}`.',
                           is_zstaff_flex=True)
    logger.log_server('[{}][{}]Removed background associated with period `{}`'
                      .format(client.area.id, client.get_char_name(), arg), client)

def ooc_cmd_bg_variant(client: ClientManager.Client, arg: str):
    try:
        Constants.assert_command(client, arg, parameters='>0')
    except ArgumentError:
        raise ArgumentError('You must specify a variant. Use /bg_variant <variant>.')
    if not client.is_mod and client.area.bg_lock:
        raise AreaError("This area's background is locked.")

    client.area.change_background_variant(arg, validate=not (client.is_staff() or client.area.cbg_allowed))
    client.area.broadcast_ooc('{} changed the backgrounds variant to {}.'.format(client.displayname, arg))
    logger.log_server('[{}][{}]Changed background variant to {}' .format(client.area.id, client.get_char_name(), arg), client)