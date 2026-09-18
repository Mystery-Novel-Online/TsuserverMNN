# GM Commands

A cmprehensive list of available commands for GMs.
GMs can bypass area passages and locks, receive special RP notifications and use GM specific commands.

---


## Area Locks

| Command | Parameters | Description |
|----------|------------|-------------|
| `/unlock` | - | Unlocks an area, provided the lock came as a result of /lock. |
| `/transient` | `<id>` | Changes a player's ability to ignore passage locks and thus access all areas from any given area. By default it is off. |
| `/bilock` | `<area 1>, <area 2>` | Changes the passage locked status (locked/unlocked) between two areas, or from the current area to area 1 if just given one area. Locking a passage in such a way does not change its current visibility to non-GMs. Areas do not need to be initially connected for this to work. |
| `/bilockh` | `<area 1>, <area 2>` | Changes the passage locked status (locked/unlocked) between two areas, or from the current area to area 1 if just given one area. Locking a passage in such a way hides it from non-GMs; unlocking it reveals it to non-GMs. Areas do not need to be initially connected for this to work. |
| `/passage_clear` | `<area range start>, <area range end>` | Clears passage locks that start in the areas in the given area range, or just the ones in the current area if not given a range. |
| `/passage_restore` | `<area range start>, <area range end>` | Restores passage locks that start in the areas in the given area range to their original status, or just the ones in the current area if not given a range. |
| `/unilock` | `<area 1>, <area 2>` | Changes the passage status (locked/unlocked) from area 1 to area 2 if given two areas, or from the current area to area 1 if just given one area. Locking a passage in such a way does not change its current visibility to non-GMs. |
| `/unilockh` | `<area 1>, <area 2>` | Changes the passage status (locked/unlocked) from area 1 to area 2, or from the current area to area 1 if just given one area. Locking a passage in such a way hides it from non-GMs; unlocking it reveals it to non-GMs. |
| `/uninvite` | `<ID/char name/showname/char showname/OOC name>` | Removes a target from your locked area's invite list, so that if they leave, they will not be allowed back until the area is unlocked. |

---

## Bloodtrail 

| Command | Parameters | Description |
|----------|------------|-------------|
| `/bloodtrail` | - | Changes the bleeding status of a target. If bleeding, they will leave 'blood' in all areas they pass through, and send OOC notifications to players in the area and those who join indicating their status. Sneaking and bleeding players send altered notifications. |
| `/bloodtrail_list` | - | Lists all areas that have bloodtrails in them, and where they lead to if appropiate. |
| `/bloodtrail_clean` | `[area 1], [area 2], ...` | Cleans the blood trails in the given areas (or the current one if not given any areas). If someone is bleeding in any of the given areas, the cleaning process will fail. |
| `/bloodtrail_set` | `[area 1], [area 2], ...` | Sets the current area to have bloodtrails leading to the listed areas. If no areas are given, the area is set to have an unconnected pool of blood. |
| `/bloodtrail_smear` | `[area 1], [area 2], ...` | Smears the blood trails in the given areas (or the current one if not given any areas). |

---

## Music

| Command | Parameters | Description |
|----------|------------|-------------|
| `/play` | `<song.extension>` `[playback type]` | Plays a song, even if not in the server music list. |
| `/rplay` | `<song.extension>` `[playback type]` | Plays a song in all areas reachable from the current one. |
| `/zone_play` | `<song.extension>` `[playback type]` | Plays a track in all areas in the zone you are watching. |

If the song is within some folders within the client music folder, such folders must be included separated by "/" (e.g. "trial/Trial Start.opus" to play "Trial Start.opus" within the "trial" folder of the client music folder).
    
Playback type is an optional variable which determines how the song will transition into the next.
-  `Sync`: Playback will fade into the new song without resetting the timestamp to the start.
-  `Instant`: Playback of the song will begin instantly. 

---

* **ambient** "name"
    - Changes the ambient sound effect of your current area.
* **ambient_end**
    - Clears the ambient sound effect of your current area.
* **area_list** "area list"
    - Sets the area list of your hub.
    - If not given an area list, it will use the default file `config/areas.yaml`.
* **area_list_info**
    - Returns the area list of your hub.
* **autopass** "ID"
    - Toggles enter/leave messages being sent automatically or not to users in the current area, including original/target areas, whenever the target moves.
    - Messages will not be sent if sneaking. Altered messages will be sent if the area's lights are turned off.
    - If no ID is given, target is yourself.\
* **blind** "ID"
    - Changes the blind status of a target.
    - Blind players will receive no character sprites nor background with IC messages and cannot use "visual" commands such as /look, /getarea, etc.
* **bg_list** "list"
    - Sets the background list of your hub.
    - If not given a background list, it will use the default file `config/backgrounds.yaml`.
* **bg_list_info**
    - Returns the background list of your hub.
* **bg_period** "period name" "bg name"
    - Sets the special background to be displayed in the area whenever there is a clock in the area with the given period.

* **bg_period_end** "period name"
    - Removes the special background to be displayed in the area whenever there is a clock in the area with the given period, so that it instead displays the normal background of the area.

* **can_passagelock**
    - Changes the current area's setting to allow non-staff members to change passages starting in the area with /bilock or /unilock. By default area setting is indicated in your hub's area list.
* **can_rollp**
    - Changes the current area's setting to allow non-staff members to do /rollp. By default area setting is indicated in your hub's area list.
* **can_rpgetarea**
    - Changes the current area's setting to allow RP users to use /getarea. By default area setting is indicated in your hub's area list.
* **can_rpgetareas**
    - Changes the current area's setting to allow RP users to use /getareas. By default area setting is indicated in your hub's area list.
* **char_list** "list"
    - Sets the character list of your hub.
    - If not given a character list, it will use the default file `config/characters.yaml`.
* **char_list_info**
    - Returns the character list of your hub.
* **char_restrict** "character name"
    - Changes the restricted status of a character in the current area.
    - If a character is restricted, only GMs and above can use the character in the current area.
* **charlog** "ID"
    - Lists all character changes (including iniswaps and character name changes) a target has gone through since connecting, including the time they were changed.
* **clock** "area range start" "area range end" "hour length" "hour start" "hours in a day"
    - Sets up a day cycle that, starting from the given hour, will tick one hour every given number of seconds (main hour length) and provide a time announcement to a given range of areas.
    - Hours go from 0 inclusive to the number of hours in a day given exclusive, or 0 to 23 inclusive if not given a number of hours in a day.
* **clock_end** "ID"
    - Ends the day cycle initiated by the target or yourself if not given a target.
* **clock_pause** "ID"
    - Pauses the day cycle initiated by the target or yourself if not given a target.
* **clock_period** "name" "hour length" "hour start"
    - Initializes a clock period that starts at the given hour for your day cycle.
    - Whenever the clock ticks into the period, players in the clock range will be ordered to switch to that time of day's version of their theme.
    - If only two arguments are given, the second argument is assumed to be hour start, and hour length is the main hour length.
    - Clock period names are automatically made all lowercase.
* **clock_period_end** "name"
    - Deletes a clock period for your day cycle.
* **clock_set** "hour length" "hour"
    - Modifies the hour length and current hour of your day cycle without restarting it. This is the way to move the day cycle out of unknown time if needed as well.
    - Acts just like doing /clock again, but does not erase already set periods.
* **clock_set_hours** "hours in day"
    - Modifies the number of hours in your day cycle.
* **clock_unknown**
    - Sets the time of your day cycle to be unknown, a special time where hours do not tick.
    - Players in the clock range will be ordered to switch to the unknown time of day version of their theme.
* **clock_unpause** "ID"
    - Unpauses the day cycle initiated by the target or yourself if not given a target.
* **cure** "ID" "initials of effects"
    - Clears the given effects from the target, as well as any poison that would have inflicted those effects.
* **deafen** "ID"
    - Changes the deafened status of a target.
    - Deafened players will be unable to read IC messages properly or receive other audio cues from commands such as /knock, /scream, etc.
* **dicelog** "ID"
    - Obtains the last 20 rolls from a target, or your last 20 rolls if not given a target.
* **dicelog_area** "area"
    - Obtains the last 20 rolls from an area by ID or name, or the last 20 rolls of your area if not given one.
* **music_list** "music list"
    - Sets the music list of your hub.
    - If not given a music list, it will use the default file `config/music.yaml`.
* **dj_list_info**
    - Returns the music list of your hub.
* **follow** "ID"
    - Starts following a target. If the target changes areas, you will automatically follow them there.
* **gag** "ID"
    - Changes the gagged status of a target.
    - Gagged players will be unable to talk IC properly or use other talking features such as /scream.
* **getarea** "area"
    - Shows the current characters in the given area, or your area if not given any.
* **globalic** "area range start", "area range end"
    - Sends subsequence IC messages to the area range described above. Can take either area IDs or area names.
* **globalic_pre** "prefix"
    - Ensures only IC messages that start with the prefix are sent to the preestablished area range through /globalic (otherwise, just to the current area), or removes the need for a prefix if not given one.
* **gmself**
    - Logs all opened multiclients as GM.
* **guide** "ID/char name/edited-to character/showname/char showname/OOC name" "message"
    - Sends an IC private 'guiding' message to the target.
    - Unlike /whisper, other people in the area are not warned that a whisper has taken place. However, staff members do get message contents, so this command should only be used in RP settings.
	- Messages are limited to 256 characters.
* **handicap** "ID" "length" "name" "announce if over"
    - Sets a movement handicap on a client by ID so that they need to wait a set amount of time in seconds between changing areas.
    - If name is given, the handicap announcement will use it as the name of the handicap.
    - If announce if over is set to any of "False, false, 0, No, no", no announcements will be sent to the player indicating that they may now move areas.
    - If the player had an existing handicap, it will be overwritten with this one.
* **hub_end**
    - Deletes your hub.
* **hub_info**
    - Returns information about your hub.
* **hub_password** "password"
    - Changes the password of your hub.
* **hub_password_info**
    - Gets the password of your hub.
* **hub_rename** "name"
    - Changes the name of your hub to the given name, or clears it if not given any.
* **iclock**
    - Changes the IC lock status of the current area.
    - If the area has an IC lock, only GMs and above will be able to send IC messages.
* **iclock_bypass** "ID"
    - Grants/revokes of an IC lock bypass to the target.
    - Targets with an IC lock bypass may talk in an area whose IC chat is locked. This effect disappears automatically as soon as they move area or their IC chat is unlocked.
* **judgelog** "area"
    - Lists the last 20 judge actions performed in the given area (or current area if not given).
    - Each entry includes the time of execution, client ID, character name, client IPID and the judge action performed.
* **lights** "on/off" "area 1" "area 2" ...
    - Changes the light status in the given areas to on or off, or in the current area if not given any.
    - Areas with lights off will have a dark background, and they disable /getarea(s) and alter /autopass, bleeding, /look and sneaking notifications.
* **look_clean** "area 1", "area 2", ...
    - Restores the default area descriptions of the given areas by ID or name, or the current area if not given any.
* **look_list**
    - Lists all areas that have custom descriptions.
* **look_set** "description"
    - Sets the area's description to the given one, or restores the default one if not given.
* **lurk** "length"
    - Sets the area's lurk callout timer to the given length in seconds, so players who remain silent for that long are called out in OOC.
* **lurk_end**
    - Ends the area's lurk callout timer if there is one active.
* **make_gm** "ID"
    - Makes the target a GM, provided the target is a multiclient of the player.
* **mindreader** "ID"
    - Changes a player's ability to see thoughts of other players made with /think. By default it is off.
* **multiclients** "ID"
    - Lists all the clients opened by a target and the areas they are in.
* **notecard_check**
    - Returns the contents of all notecards set by players in your current area.
* **notecard_clear** "ID"
    - Clears the content of a player's notecard by ID, or your own notecard if not given one.
* **notecard_clear_area**
    - Clears the content of the notecards of all players in your current area.
* **notecard_list**
    - Returns the content of all notecards currently set by players in the server.
* **notecard_reveal**
    - Reveals the contents to all players in the area of all notecards of all players in your current area.
* **notecard_reveal_count**
    - Tallies the contents of all notecards of players in the area and reveals the count to all players in your current area.
    - This does not reveal the people who wrote particular notecards.
* **noteworthy**
    - Changes the noteworthy status of the area.
* **noteworthy_info**
    - Returns the noteworthy status and noteworthy text of an area.
* **noteworthy_set** "text"
    - Changes the noteworthy text of the area to the given text, or a default one if not given any.
    - Noteworthy text can be changed independently of the noteworthy status of an area.
* **nsd** "time"
    - Starts an NSD part of your current trial with all players in the area part of your trial, making you leader of the NSD.
    - The NSD will have a given time limit in seconds, or no time limit if not given a time. Debates with a time limit will be automatically halted once the timer runs out.
    - Nonplayers may not talk IC while an NSD is taking place.
* **nsd_accept**
    - Accepts a break from a player who shot a bullet during looping or recording mode for the NSD you lead, restoring 0.5 influence and ending the NSD.
* **nsd_add** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Adds a player part of your current trial to your NSD.
* **nsd_autoadd**
    - Toggles players who are added to the trial of the NSD being automatically added to the NSD on or off.
    - By default it is the same as the trial's behavior when a user enters an area part of the trial (refer to /trial_autoadd).
* **nsd_end**
    - Ends an NSD you lead.
* **nsd_join** "nsdID"
    - Enroll in the NSD in your trial occurring your area.
* **nsd_lead**
    - Makes you a leader of your NSD.
* **nsd_loop**
    - Sets the NSD you lead to be in looping mode: messages saved during recording mode will be played Danganronpa style one after the other until a bullet is shot or all messages are seen.
* **nsd_kick** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Kicks a player off the NSD you lead.
* **nsd_pause**
    - Pauses the NSD you lead, putting it in intermission mode.
* **nsd_reject**
    - Rejects a break from a player who shot a bullet during looping or recording mode for the NSD you lead, draining 1 influence from them.
    - The NSD will not end or resume automatically, you will be prompted to decide what to do.
* **nsd_resume**
    - Sets the NSD you lead to be in the mode prior to intermission mode: if it was recording mode, previously recorded messages will be saved and future messages will be saved on top of the older ones; if it was looping, messages will be played from the first one.
* **nsd_unlead**
    - Removes your NSD leader role.
* **paranoia** "player ID" "paranoia level"
    - Sets the player paranoia level (by default 2) of a player to the new level.
    - Paranoia level is a number from -100 to 100, and is internally added to the paranoia level of the player's current zone (if any) to determine the probability they occasionaly get phantom peek messages.
* **paranoia_info** "player ID"
    - Gets the player paranoia level of a player.
* **party_end** "party ID"
    - Ends a party.
* **party_join** "party ID"
    - Makes you join a party, even if you were not invited to it.
* **party_list**
    - Lists all active parties in the server, as well as some of their details.
* **poison** "ID" "initials of effects" "length"
    - Applies a poison to the target that will inflict them in the given length of time in seconds the given effects.
* **pos_force** "position" "ID"
    - Changes the IC position of a target by ID to the given one, or the one of all players in an area if not given a target.
* **refresh**
    - Reloads your hub's character, music and background lists.
* **reveal** "ID"
    - Reveals a target if they were previously sneaking.
    - Also restores their formerly assigned handicap if they had one that was shorter than the server's automatic sneaking handicap.
    - If no ID is given, target is yourself.
* **poison** "ID" "initials of effects" "length"
* **scream_range**
    - Returns the areas that can listen to screams sent from the current area.
* **scream_set** "area"
    - Changes the reachable status from screams sent from the current area to the given area.
* **scream_set_range** "area 1", "area 2", ...
    - Sets the current area's scream range to be the areas listed.
    - The special keyword <ALL> means all areas in the server should be able to listen to screams from the current area.
    - The special keyword <REACHABLE_AREAS> means all areas reachable from the current area.
* **shoutlog** "area"
    - Lists the last 20 shouts sent in the given area, or from the current area if not given.
    - Each entry includes the time of execution, client ID, character name, client IPID, the shout ID and the IC message sent alongside.
* **showname_history** "ID"
    - Lists all shownames a target has gone through since connecting, including the time they were changed.
* **showname_set** "ID" "showname"
    - Sets a target's showname to be the given one, or clears it if not given one.
* **sneak** "ID"
    - Sets a target to be sneaking if they were visible.
    - If the target was subject to a handicap shorter than the server's automatic sneak handicap length, they will be imposed this handicap.
    - If no ID is given, target is yourself.
* **sneakself**
    - Sneaks all opened multiclients that can be sneaked.
* **summon** "ID" "area number"
    - Summons target from their area to the intended area, or to your area if not given an area, and remove them from the invite list of their old area.
* **st** "message"
    - Sends a message to all active staff members.
* **status_set_other** "ID/char name/edited-to character/showname/char showname/OOC name" "status"
    - Sets the player status of another user, or clears it if not given a status.
* **switch** "character name"
    - Switches you to the given character, provided no other player is using it in the area.
* **toggle_allpasses**
	- Changes your ability to receive autopass notifications from players that do not have autopass on. By default it is off.
* **toggle_allrolls**
    - Changes your ability to receive /roll and /rollp results from other areas. By default it is off.
* **trial**
    - Starts a trial with all players in the area, making you leader of the trial.
* **trial_add** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Adds a player to a trial you lead.* **nsd_autoadd**
* **trial_autoadd**
    - Toggles users who enter an area of the trial being automatically added to the trial on or off.
    - By default it is off.
* **trial_end**
    - Ends a trial you lead, as well as any minigames that may have be taking place in the trial.
* **trial_focus** "ID/char name/edited-to character/showname/char showname/OOC name" "number"
    - Sets the focus level of a player in your trial to the given value.
    - Number must be an integer from 0 to 10.
* **trial_influence** "ID/char name/edited-to character/showname/char showname/OOC name" "number"
    - Sets the influence level of a player in your trial to the given value.
    - Number must be an integer from 0 to 10.
* **trial_info**
    - Returns details about your trial.
    - If a leader of your trial, also includes the influence and focus values of all trial players.
* **trial_join** "trial ID"
    - Enrolls in the trial by ID occurring in your area.
* **trial_lead**
    - Makes you a leader of your trial.
* **trial_kick** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Kicks a player off your trial.
* **trial_unlead**
    - Removes your trial leader role.
* **unfollow**
    - Stops following whoever you were following.
* **unignore** "ID/char name/edited-to character/showname/char showname/OOC name"
    - Marks a target as no longer ignored, so you will now receive any IC messages from them.
    - The target is not notified of you marking them as no longer ignored.
* **unglobalic**
    - Stops sending subsequent IC messages to the area range specified in a previous /globalic command.
* **unhandicap** "ID"
    - Removes movement handicaps on a target.
* **whereis** "ID"
    - Obtains the area a target is.
* **whois** "ID/char name/showname/OOC name"
    - Obtains a lot of properties of the target.
* **zone** "area range start", "area range end"
    - Creates a zone involving the area range given above, just the given area if given one parameter, or just the current area if not given a parameter.
    - You are automatically set to watch the zones you create like this.
* **zone_add** "area"
    - Adds an area by name or ID to the zone you are watching.
* **zone_ambient** "name"
    - Changes the ambient sound effect of all areas of the zone you are watching.
* **zone_ambient_end**
    - Clears the ambient sound effect of all areas of the zone you are watching.
* **zone_autoglance**
    - Changes the autoglance status of the zone you are watching. If turned on, turns autoglance on for players in an area part of a zone and players that later join; otherwise, it turns it off for players in an area part of the zone
* **zone_autopass**
    - Changes the autopass status of the zone you are watching. If turned on, turns autopass on for players in an area part of a zone and players that later join; otherwise, it turns it off for players in an area part of the zone
* **zone_end**
    - Ends the zone you are watching.
* **zone_handicap** "length" "name" "announce if over"
    - Sets a movement handicap on all clients part of the zone (now or later) you are watching so that they need to wait a set amount of time in seconds between changing areas.
    - Players who are subject to a zone handicap that then leave the zone will have their handicap removed.
    - If name is given, the handicap announcement will use it as the name of the handicap.
    - If announce if over is set to any of "False, false, 0, No, no", no announcements will be sent to the player indicating that they may now move areas.
    - If a player in the zone had an existing handicap, it will be overwritten with this one.
* **zone_handicap_affect** "ID"
    - Makes the player subject to the zone's movement handicap.
    - This is useful if the player lost the zone handicap because another handicap was removed.
* **zone_iclock**
    - Applies the same lock/unlock status to all areas part of the zone.
* **zone_info**
    - Lists brief description of the zone you are watching, as well as lists all players in areas part of the zone.
* **zone_lights** "on/off"
    - Changes the light status of every area in a zone you are watching to on or off.
* **zone_list**
    - Lists all active zones in the server, as well as some of their details.
* **zone_mode** "mode"
    - Sets up the gamemode of your zone, or clears it if not given one.
    - Players in an area part of the zone will be ordered to switch to that gamemode's version of their theme.
    - Gamemodes are automatically made all lowercase.
* **zone_paranoia** "paranoia level"
    - Sets the zone paranoia level (by default 2) of the zone you are watching to the new level.
    - Paranoia level is a number from -100 to 100, and is internally added to a player paranoia's level to determine the probability percentage they occasionaly get phantom peek messages.
* **zone_paranoia_info**
    - Gets the zone paranoia level of the zone you are watching.
* **poison** "ID" "initials of effects" "length"
* **zone_remove** "area"
    - Removes an area by name or ID from the zone you are watching.
* **zone_tick** "chat tick rate"
    - Sets the chat tick rate in milliseconds in your zone. All players in an area part of a zone will render IC messages with this chat tick rate.
* **zone_tick_remove**
    - Removes the chat tick rate in your zone. All players in an area part of a zone will render IC messages with their own chat tick rate.
* **zone_unhandicap**
    - Removes the zone's movement handicap.
* **zone_unwatch**
    - Makes you stop watching the zone you were watching.
* **zone_watch** "zone"
    - Makes you start watching a zone by its ID.
