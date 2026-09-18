[![Build Status](https://travis-ci.org/Chrezm/TsuserverDR.svg?branch=master)](https://travis-ci.org/Chrezm/TsuserverDR)
# TsuserverDR

A Python-based server for Danganronpa Online. It is a fork from [tsuserver3](https://github.com/AttorneyOnline/tsuserver3) which is targeted towards Attorney Online.

Requires Python 3.9-3.11, PyYAML and aiohttp (follow instructions below to install).

## How to use

### Installing

It is highly recommended you read through all the installation steps first before going through them.

* Install the latest version of Python. **Python 2 will not work**.
  - You can download Python from its official website [here](https://www.python.org/downloads/). If you already have Python installed, check that your Python version satisfies the version requirement listed above.
  - If prompted during the installation to add `python` as a PATH environment variable, accept this option. You may see this option appear on the very first screen during the installation process.
  - If you know what a virtual environment is and your system supports it, it is recommended that you use one, such as [Anaconda](https://www.continuum.io/downloads) for Windows, or [virtualenv](https://virtualenv.pypa.io/en/stable/) for everyone else (it runs itself using Python). If you do not know what a virtual environment is, you may skip this point.
  - If you have Python 3.8 or lower, you will be prompted on server launch to update to a newer version of Python. That is because the server requires Python 3.9 or higher. Follow instructions under Updating to update your Python version.

* Open Command Prompt, PowerShell or your preferred terminal, and change to the directory where you downloaded TsuserverDR to. You can do this in two ways:
  - On Windows 10 or higher, go up one folder above the TsuserverDR folder, Shift + right click the TsuserverDR folder, and click `Open PowerShell window here` or `Open in Terminal`. This is the easiest method. Alternatively...
  - On most operating systems, copy the path of the TsuserverDR folder, open the terminal, and type in `cd "[paste here]"`, excluding the brackets, but including the quotation marks if the path contains spaces.

* Make sure Python is properly installed by typing `python` in the terminal and pushing Enter.
  - If text that starts with `Python 3.11.0 (main, ` or similar appears, you are all set with this step. Push Ctrl+Z followed by Enter to continue to the next step if you are on Windows; and Ctrl+D if you are on Linux.
  - If text that starts with `The term 'python' is not recognized as the name of a cmdlet` or similar, Python wasn't properly added to path. Follow the instructions [here](https://realpython.com/add-python-to-path/#how-to-add-python-to-path-on-windows) to try and fix the issue (this is for Windows, instructions for other operating systems are also available in the same website if you scroll further down).
  - If on Windows and a separate window opens that leads to the Microsoft Store, Windows may have added an execution alias. Follow the instructions [here](https://stackoverflow.com/a/58773979) to try and remove this alias.

* Install all dependencies by typing in the following two commands in the terminal you just opened:
  ```
  python -m pip install --upgrade pip
  python -m pip install --user -r requirements.txt
  ```

  If you are using Windows and have both Python 2 and 3 installed, you may do the following:
  ```
  py -3 -m pip install --upgrade pip
  py -3 -m pip install --user -r requirements.txt
  ```

  This operation should not require administrator privileges, unless you decide to remove the `--user` option.

* Rename the folder `config_sample` to `config` and edit the values in the provided YAML files to your liking. Be sure to check the YAML files for syntax errors after you are done. *Use spaces only; do not use tabs.*

* If you intend to have players outside of your network connect to your server, open or forward the port that you would like them to connect to. The port number is available in `config/config.yaml` next to `port`, and you may change it to something else if you want to. The port that you choose must be made to accept TCP connections. This whole process may involve you doing some (or all) of the following:
    - If you are hosting your server in your own device: go to your router settings, and proceed to open/forward/allow inbound connections into the port. You can typically find instructions for this by finding the brand and model name of your router, and searching "brand + model + port forwarding".
    - If you are hosting your server in an external device (such as a VPS): find its networking settings, and proceed to open/forward/allow inbound connections into the port. You can typically find instructions for this by searching something like this "your VPS + open/forward/allow inbound connections into the port".
    - Go to your operating system firewall settings, and proceed to create a rule to allow inbound connections into the port. You can typically find instructions for this by searching "your operating system + create inbound port rule".
    - Go to your third-party antivirus/firewall software settings (if you have it), and proceed to create a rule to allow inbound connections into the port (if applicable). You can typically find instructions for this by searching "your antivirus + open/forward/allow inbound connections into the port".

### Running

* To launch a server, you may either
  - Double-click `start_server.py` in your TsuserverDR folder, or...
  - In PowerShell, Command Prompt or your preferred terminal, change directory to your TsuserverDR folder and type `python start_server.py`, or `py -3 start_server.py` if you use both Python 2 and 3. For instructions on how to launch any of the above programs or change directory, refer to the second point in the Installing section.

* If everything was set up correctly, you will see something like this appear:

```
[2022-11-23T10:20:20]: Starting...
[2022-11-23T10:20:20]: Launching TsuserverDR 5.0.0 (221123a)...
[2022-11-23T10:20:20]: Loading server configurations...
[2022-11-23T10:20:20]: Server configurations loaded successfully!
[2022-11-23T10:20:20]: Starting a nonlocal server...
[2022-11-23T10:20:20]: Server started successfully!
[2022-11-23T10:20:21]: Server should be now accessible from address 192.0.2.0 and port 50000.
```

* If you are listing your server in the Attorney Online master server, make sure its details are set up correctly. In particular, make sure that your server name and description are correct, as that is how players will find your server. If everything was set up correctly, you will see something like this appear:

```
[2022-11-23T10:20:21]: Attempting to connect to the master server at https://servers.aceattorneyonline.com/servers with the following details:
[2022-11-23T10:20:21]: *Server name: My First DR Server
[2022-11-23T10:20:21]: *Server description: This is my flashy new DR server
[2022-11-23T10:20:22]: Connected to the master server.
```

  - The server will make a single ping to [ipify](https://api.ipify.org) in order to obtain its public IP address. If it fails to do that, it will let you know that, as it means there is probably something wrong with your internet connection and that other players may not be able to connect to your server.
  - Successful connection or getting a spot in the master server list does not imply that your server will be accessible to other players. In particular, you must make sure that your external port in `config/config.yaml` is open and accepting connections, which usually involves a combination of router and firewall settings. In case of doubt, you can use websites such as [Can You See Me](https://canyouseeme.org) to check if your port is visible.

* To stop the server, press Ctrl+C once from your terminal. This will initiate a shutdown sequence and notify you when it is done. If the shutdown finished successfully, you will see something like this appear:

```
[2022-11-23T22:23:04]: You have initiated a server shut down.
[2022-11-23T22:23:04]: Kicking 12 remaining clients.
[2022-11-23T22:23:04]: Server has successfully shut down.
```

* If you do not see anything after a few seconds of starting a shutdown, you can try spamming Ctrl+C to try and force a shutdown or directly close out your terminal. This is not recommended due to the cleanup process not finishing correctly but it is doable.

* To restart a server, you can follow the steps outlined above to shut down and then start the server again.

* In the unlikely event that there is an error during runtime, the server will do its best to print out to your terminal a complete traceback of the error with some additional information, as well as a more complete log file in the `logs` folder with the error timestamp, to help with debugging. Depending on the nature of the error, the server may or may not be able to continue execution normally after such an error happens.

### Updating

* If you already have a version of TsuserverDR or tsuserver3 installed and wish to update to a new version, you can download the new version and then overwrite your previously existing files. Do note that you do not need to shut down your server before overwriting the files, but you must restart it from console in order for changes to take effect.

  - This process will not overwrite your server configurations inside the `config` folder, your existing logs inside the `logs` folder, or the user information inside the `storage` folder. However, it will overwrite other files including the Python files inside the `server` folder. Therefore, make sure to save backups of those files before overwriting in case you have modified them and wish to keep an archive of your changes.

* If you want to update **Python** itself, you can get the latest Python download [from their website here](https://www.python.org/downloads/) and then follow the instructions under the Installing section in this readme. To check your current version of Python, you can run ``python`` on its own and look at the first line. The latest stable major Python release is *Python 3.11* as of October 24, 2022.

  - Please follow the installation instructions again even if you had successfully ran a server before, because your new Python installation may be missing libraries that TsuserverDR expects there to exist. You should not need to change any server configuration files though.
  - In general, updating to a Python version beyond what is specified as supported may lead to unstable behavior, so for active servers try to keep your Python version among the ones specifically labeled as supported.

## Commands
Additional notes are listed at the end of the command list. Unless otherwise specified, all command arguments have a character limit of 1024 characters, beyond which they will be cut off.

### User Commands

* **help** "command name"
    - Displays help for a command, or links to the server repository if not given an argument.
* **help_more** "command name"
    - Displays extended help for a command, usually significantly longer than what /help does.
* **ambient_info**
    - Displays the current area ambient sound effect.
* **area** "area number"
    - Moves you to an area by its numerical ID if it is reachable from your own, or displays all areas if not given a number.
* **autoglance**
    - Toggles area descriptions (if present) being sent automatically or not when you move areas.
    - No messages will be sent if your area's lights are turned off or you are blind.
* **autopass**
    - Toggles enter/leave messages being sent automatically or not to users in your area, including original/target areas.
    - Messages will not be sent if sneaking. Altered messages will be sent if the area's lights are turned off.
* **bg** "background"
    - Changes the current background.
* **bilock** "area number/name"
    - Changes the passage status (locked/unlocked) between the current area and the given area.
* **bloodtrail_clean**
    - Cleans the bloodtrail in the current area.
    - If someone is bleeding in the current area, the cleaning process will fail.
* **bloodtrail_smear**
    - Smears the bloodtrail in the current area.
* **charselect**
    - Puts you back to the character select screen.
* **chars_restricted**
    - Lists all characters that are restricted in the current area.
* **cleardoc**
    - Clears the doc url of the current area.
* **cid** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Gives you the client ID of the target, or your own client ID if not given an argument.
* **coinflip** "call"
    - Flips a coin and returns its result, as well as whatever it is called with (e.g. a prediction, consequences for heads/tails, etc.) if given.
* **currentmusic**
    - Displays the current music, who played it, and its source if given in the music list.
* **discord**
    - Displays the invite link of the server's Discord server.
* **doc** "url"
    - Gives the doc url if blank, updates the doc url otherwise.
* **exit**
    - Exits the server.
* **files** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Gives a download link set by the target that links to their files, or gives your own download link if not given an argument.
* **files_area**
    - Gives the download link of the character files of all players visible in your area.
* **files_set** "url"
    - Sets a download link for your character files, or clears it if not given an argument.
* **follow** "ID"
    - Starts following a target, provided you were a spectator. If the target changes areas, you will automatically follow them there.
* **g** "message"
    - Sends a serverwide message. Fails if the current area disallows sending global messages.
* **getarea**
    - Shows the current characters in your area, including their showname if they have set it.
* **getareas**
    - Shows all characters in all areas reachable from your own, including their showname if they have set it.
* **hub** "hub number"
    - Moves you to the default area of a hub by its numerical ID, or displays all hubs if not given a number.
* **ignore** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Marks a target as ignored, so you will no longer receive any IC messages from them.
    - The target is not notified of you marking them as ignored.
* **invite** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Adds target to the invite list of your locked area so they may join.
* **kickself**
    - Removes all of of the user's clients except the one that used the command.
* **knock** "area"
    - Knocks on a reachable area's door, sending an OOC notification to that area. Can be either area ID or name.
* **lights** "on/off"
    - Changes the light status in the area to on or off.
    - Areas with lights off will have a dark background, and they disable /getarea(s) and alter /autopass, bleeding, /look and sneaking notifications.
* **lock**
    - Locks your area. Prevents normal users from entering.
    - People in the area, including yourself, at the time the area is locked are free to come and go regardless of their status.
* **login** "password"
    - Makes you a Moderator.
* **logincm** "password"
    - Makes you a Community Manager.
* **logingm** "password"
    - Makes you a Game Master.
* **logout**
    - Logs you out of the rank you have, if any.
* **look**
    - Obtains the description of the current area as well as players inside
* **minimap**
    - Lists all areas reachable from the current one.
* **motd**
    - Returns the server's Message of the Day.
* **personal_music** "music list name"
    - Sets your music list to the given one, or restores the original one if not given any.
* **music_list_info**
    - Returns your current music list.
* **notecard** "content"
    - Sets the content of your notecard.
* **notecard_clear**
    - Clears the content of your notecard.
* **notecard_info**
    - Returns the content of your notecard.
* **nsd_info**
    - Returns details about your NSD.
* **nsd_leave**
    - Makes you leave your NSD.
    - You will no longer be able to interact with the NSD, but you will still see messages of the NSD, provided you stay in the NSD area.
    - If you are the last player to leave the NSD, it will be automatically destroyed.
* **online**
    - Returns how many players are online.
* **party**
    - Creates a party and makes you its leader.
* **party_end**
    - Ends your party.
* **party_id**
    - Returns your party ID.
* **party_invite** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Invites a player in the same area to your party.
* **party_join** "party ID"
    - Makes you join a party you were invited to.
* **party_kick** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Kicks a player off your party.
* **party_lead**
    - Makes you a leader of your party.
* **party_leave**
    - Makes you leave your party.
    - Other people in the party are warned of your departure if you are not sneaking.
    - If you are the last player to leave the party, it will be automatically ended.
* **party_members**
    - Lists the leaders and regular members of your party.
* **party_uninvite** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Revokes an invitation sent to a player to join your player.
* **party_unlead**
    - Removes your party leader role.
* **party_whisper** "message"
    - Sends an IC private message to everyone in the party.
    - Other people in the area are warned that a whisper has taken place (but not the message content). However, staff members do get message contents, so this command should only be used in RP settings.
	- Messages are limited to 256 characters.
* **peek** "area ID"
    - Peeks into an area visible to you, returning information that would have been available had you done /look there.
    - Successful peeks have a 75% chance to notify of the peek having taken place for each player in the target area.
* **ping**
    - Returns "Pong", used to check for server connection.
* **play** "song.extension"[ "fade type"]
    - Plays a song, provided the area you are in allows non-staff members to run this command.
    - If the song is within some folders within the client music folder, such folders must be included separated by "/" (e.g. "trial/Trial Start.opus" to play "Trial Start.opus" within the "trial" folder of the client music folder).
    - [OPTIONAL] Fade type determines how the new and previous stopping behavior.
    * `in`: The new song will fade in as it begins to play.
    * `out`: The old song will fade out before the new song begins to play.
    * `mix`: A combination of `in` and `out`.
* **poison** "ID" "initials of effects" "length"
* **pm** "ID/char name/edited-to character/showname/char showname/OOC name" "message"
    - PMs the target.
* **pos** "position"
    - Changes your position in the court.
    - Positions: 'def', 'pro', 'hld', 'hlp', 'jud', 'wit'
* **randomchar**
    - Changes your character to a randomly chosen one.
* **randommusic**
    - Plays a randomly chosen song from your current music list.
* **reload**
    - Reloads your character ini file.
* **roll** "number of dice"d"number of faces" "modifiers"
    - Rolls as many dice as given with the given number of faces, and applies modifiers if given. If no arguments are given, rolls one d6.
* **rollp** "number of dice"d"number of faces" "modifiers"
    - Same as roll but other non-staff members in the area only are notified that someone rolled.
* **scream** "message"
    - Sends an IC message visible to all players in the areas that are set to be able to listen to screams from the current area.
    - Messages are limited to 256 characters.
* **showname** "showname"
    - Sets your showname to be the given one, or clears it if not given one.
* **status** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Check the custom status of a player
* **status_set** "status"
    - Sets a custom status for your character, or clears it if not given an argument.
* **spectate**
    - Switches you to a SPECTATOR character.
* **switch** "character name"
    - Switches you to the given character, provided no other player is using it in the area and it is not restricted.
* **think** "message"
    - Sends an IC message that only you and zone watchers or GMs+ can see.
* **time**
    - Displays the server's local time.
* **time12**
    - Displays the server's local time in 12 hour format.
* **timer** "length" "timer name" "public"
    - Starts a timer of the given length in seconds, which will send a notification to people in the area once it expires.
    - If given a timer name, it will override the default timer name (OOCNameTimer).
    - If public is set to any of the following: "False, false, 0, No, no", the timer details will be hidden from non-staff players.
* **timer_end** "timer name"
    - Ends the timer by name, provided it is yours.
* **timer_get** "timer name"
    - Obtains the remaining time of the given timer by name, provided it is public, or list all remaining times in all public timers if not given a name.
* **ToD**
    - Chooses "Truth" or "Dare" for Truth or Dare minigames.
* **toggle_fp**
    - Changes your setting to be in first person mode (your character does not appear to you when you send IC messages) or normal mode (your character does appear). By default it is in normal mode.
* **toggle_fs**
    - Changes your setting to have forward sprites mode off (your character sprites are not sent to anyone, everyone sees the last sprites they last saw) or on (your character appears normally). By default it is on.
* **toggle_global**
    - Changes your setting to receive global messages. By default it is on.
* **toggle_music_list_default**
    - Changes your setting to see which music list to see when no personal music list is active: current hub or server default. By default it is current hub.
* **toggle_pm**
    - Changes your setting to receive PMs. By default it is on.
* **toggle_shownames**
    - Changes your setting to have the IC messages you receive to include the sender's custom showname. By default it is on.
* **trial_info**
    - Returns details about your trial.
* **trial_leave**
    - Makes you leave your trial.
    - You will still see messages of the trial, provided you stay in the trial area.
    - If you are the last player to leave the trial, it will be automatically destroyed.
* **unfollow**
    - Stops following whoever you were following, provided you were a spectator.
* **unignore** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Marks a target as no longer ignored, so you will now receive any IC messages from them.
    - The target is not notified of you marking them as no longer ignored.
* **unilock** "area number/name"
    - Changes the passage status (locked/unlocked) from the current area to the given one.
* **uninvite** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Removes a target from your locked area's invite list, so that if they leave, they will not be allowed back until the area is unlocked.
* **unlock**
    - Unlocks your area, provided the lock came as a result of /lock.
* **version**
    - Obtains the current version of the server software.
* **whisper** "ID/char name/edited-to character/showname/char showname/OOC name" "message"
    - Sends an IC private message to the target, provided they are in the area.
    - Other people in the area are warned that a whisper has taken place (but not the message content). However, staff members do get message contents, so this command should only be used in RP settings.
    - Messages are limited to 256 characters.
* **zone_global**
    - Sends a message to all players in the zone you are in.
* **8ball** "question"
    - Gains insight from the magic 8 ball in response to a question if given one.

### GM Commands
A list of GM commands can be found [here](docs/gm-commands.md).

### Community Manager Commands

* **blockdj** "ID/IPID"
    - Mutes the target from changing music.
* **charlog** "ID/IPID"
    - Lists all character changes (including iniswaps and character name changes) a target has gone through since connecting, including the time they were changed.
* **cleargm** "ID"
    - Logs out the target from their GM rank, or all GMs in the server if not given a target.
* **g** "message"
    - Sends a serverwide message, even if the current area disallows sending global messages.
* **getarea**
    - Shows the current characters in your area as well as their IPIDs.
* **getareas**
    - Shows all characters in all areas of the server as well as their IPIDs.
* **glock**
    - Changes the global chat lock status of the server.
    - If the server has its global chat locked, only CMs and above can use /g and /zone_global.
* **handicap** "ID/IPID" "length" "name" "announce if over"
    - Sets a movement handicap on a client by ID or IPID so that they need to wait a set amount of time in seconds between changing areas.
    - If name is given, the handicap announcement will use it as the name of the handicap.
    - If announce if over is set to any of "False, false, 0, No, no", no announcements will be sent to the player indicating that they may now move areas.
* **hub_create** "name"
    - Creates a new hub with given name, or with a default generated name otherwise.
* **hub_end** "hub"
    - Deletes the hub by numerical ID, or your hub if not given any.
* **hub_info** "hub"
    - Returns information about the hub by numerical ID, or your hub if not given any.
* **hub_password_info** "hub"
    - Returns the password of the hub by numerical ID, or your hub if not given any.
* **hub_rename** "name"
    - Changes the name of your hub to the given name, or clears it if not given any.
* **invite** "ID/IPID/char name/edited-to character/showname/char showname/OOC name"
    - Adds target to the invite list of your area.
* **kick** "ID/IPID"
    - Kicks the target from the server.
* **make_gm** "ID"
    - Makes the target a GM.
* **multiclients** "ID/IPID"
    - Lists all the clients opened by a target and the areas they are in.
* **mute** "ID/IPID"
    - Mutes the target from all IC actions.
* **ooc_mute** "OOC name"
    - Mutes the target from all OOC actions.
* **ooc_unmute** "OOC name"
    - Unmutes the target.
* **reveal** "ID/IPID"
    - Reveals a target if they were previously sneaking.
    - Also restores their formerly assigned handicap if they had one that was shorter than the server's automatic sneaking handicap.
* **showname_history** "ID/IPID"
    - Lists all shownames a target has gone through since connecting, including the time they were changed.
* **showname_set** "ID/IPID" "showname"
    - Sets a target's showname to be the given one, or clears it if not given one.
* **sneak** "ID/IPID"
    - Sets a target to be sneaking if they were visible.
    - If the target was subject to a handicap shorter than the server's automatic sneak handicap length, they will be imposed this handicap.
* **summon** "ID/IPID" "area number"
    - Summons target from their area to the intended area, or to your area if not given an area, and remove them from the invite list of their old area.
* **transient** "ID/IPID"
    - Changes a player's ability to ignore passage locks and thus access all areas from any given area. By default it is off.
* **unblockdj** "ID/IPID"
    - Allows the target to change music again.
* **unhandicap** "ID/IPID"
    - Removes movement handicaps on a target.
* **uninvite** "ID/IPID/char name/edited-to character/showname/char showname/OOC name"
    - Removes a target from your locked area's invite list, so that if they leave, they will not be allowed back until the area is unlocked.
* **unmute** "ID/IPID"
    - Unmutes the target from the IC chat.
* **whereis** "ID/IPID"
    - Obtains the area a target is.
* **whois** "ID/IPID/char name/showname/OOC name"
    - Obtains a lot of properties of the target, including HDID and IPID.
* **zone_end** "zone"
    - Deletes a zone by its ID, or the zone you are watching if not given a zone.

### Moderator Commands
A list of moderator commands can be found [here](docs/moderator-commands.md).

### Debug commands

* **exec** "command"
    - (DEBUG) Executes the given command as a Python instruction. Requires turning on in `server/commands.py` before using.
* **dump**
    - (DEBUG) Prepares a server dump containing debugging information about the server and saves it in the server log files.
* **lasterror**
    - (DEBUG) Obtains the latest uncaught error as a result of a client packet. This message emulates what is output on the server console.
* **reload_commands**
    - (DEBUG) Reloads the `server/commands.py` file.

### Deprecated commands and aliases
Commands marked with (D) are marked as deprecated. They will continue to serve their original purpose as usual for at least three months after the stated date. If an alternative command name is given to a deprecated command, please try and use that command instead.

Commands without (D) are aliases to commands and can be freely used (subject to the parent command's conditions).

#### Everyone

* **huddle**: Same as /party_whisper.
* **pw**: Same as /party_whisper.
* **sa**: Same as /getarea.
* **sas**: Same as /getareas.
* **shout**: Same as /scream.
* **showname_list**: Same as /getareas.
* **unsneak**: Same as /reveal.
* **yell**: Same as /scream.
* **zg**: Same as /zone_global.
* **zi**: Same as /zone_info.
* **fa**: Same as /files_area.
* **l**: Same as /look.
* **forcepos**: Same as /pos_force.
* **showname_area**: Same as /getarea.
* **showname_areas**: Same as /getareas.
* **ga**: Same as /getarea.
* **gas**: Same as /getareas.

#### GM+

* **area_kick**: Same as /summon.
* **loginrp**: Same as /logingm.
* **slit**: Same as /bloodtrail.
* **unsneak**: Same as /reveal.

### Notes

* **Note 1**: the commands may refer to the following identifiers for a player:
    - **Character Name**: the folder name of the character the player is using, also the name that appears in /getarea.
    - **HDID**: the hard drive ID of the player, accessible through /whois (requires community manager rank).
    - **ID**: number in brackets [] in /getarea.
    - **IPID**: number in parentheses () in /getarea (requires community manager rank).
    - **IP**: the IP address of the player.
    - **OOC Name**: the username of the player in the OOC chat.
* **Note 2**: some commands include commas (,) between the parameters. If that is the case, the command expects you to actually use the commas between the parameters. If for whatever reason your parameter also has a comma followed by a space, you can include it by using ,\ (so 'Hello, world' becomes 'Hello,\ world').
* **Note 3**: additional documentation for the commands can be found in `config/commands.py` and consulting the docstrings. For example, to get additional information for /help, you would look for `ooc_cmd_help` and look for the associated text.

## License

This server is licensed under the AGPLv3 license. In short, if you use a modified version of TsuserverDR, you *must* distribute its source licensed under the AGPLv3 as well, and notify your users where the modified source may be found. The main difference between the AGPL and the GPL is that for the AGPL, network use counts as distribution. If you do not accept these terms, you should use [serverD](https://github.com/Attorney-Online-Engineering-Task-Force/serverD), which uses GPL rather than AGPL.

See the [LICENSE](LICENSE.md) file for more information.
