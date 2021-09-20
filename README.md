# alfred-complice 

### A workflow to manage your [Complice](https://complice.co/) intentions and timers with  [Alfred](https://www.alfredapp.com/)



![](images/complice-screencast.gif "")

<!-- MarkdownTOC autolink="true" bracket="round" depth="3" autoanchor="true" -->

- [Setting up](#setting-up)
- [Basic Usage](#usage)
- [Known Issues](#known-issues)
- [Acknowledgments](#acknowledgments)
- [Changelog](#changelog)
- [Feedback](#feedback)

<!-- /MarkdownTOC -->


<a name="setting-up"></a>
# Setting up

### Needed

- Alfred with Powerpack license
- Complice account (use [this](https://complice.co/?r=4z020qsycl) link to get a bonus third week of free trial)
- Complice API Token (available [here](https://complice.co/$USERNAME/auth_token) while you are logged in)




1. Download the [most recent release](https://github.com/giovannicoppola/alfred-complice/releases/latest) of `alfred-complice` from Github and double-click to install
2. Get your Complice Auth Token 
	- in [Complice](https://complice.co/$USERNAME/auth_token), Select and copy to clipboard the auth token. 
	_Example_: if the string is `{"username":"johndoe","auth_token":"abcd1234"}`, copy `abcd1234` (without quotes)

3. In Alfred, open the 'Configure Workflow and Variables' window in `alfred-complice` preferences
	<img src='images/alfred_prefs.png' width="500">	
			
	- set the `TOKEN` variable to the Complice Auth Token retrieved in Step 2
	- _Optional:_ set the `POMOLENGTH` variable (predefined value: 25 min)
	- _Optional:_ set the `TIMERLENGTH` variable (predefined value: 20 min)
	
4. _Optional:_ Setup a hotkey to launch alfred-complice
5. _Optional:_ Change the keyword to launch alfred-complice
	- keyword currently set to `!c`



<a name="usage"></a>
# Basic Usage 

Most features are self-explanatory, briefly described below:
## Intentions
- Add new intentions (remember to add the goal number (e.g. `1)`) otherwise it will be entered as )
- List intentions for the day
- Complete intentions

## Pomodoros 🍅
- Start a pomodoro (default length set in Settings) 

### 🍅 While running

- Check remaining 🍅 time
- Cancel 🍅

## Timers ⏳
- Start a timer (default length set in Settings) 
- Start a 'targeted' timer to the top of the hour (:00) or next half-hour (:30)

### ⏳ While running

- Check remaining ⏳ time 
- Pause and restart ⏳
- Cancel ⏳



<a name="known-issues"></a>
# Known issues 


- Pausing a targeted time will shift the end time accordingly (for example, if you pause for 10 min and then restart a timer that is supposed to end at 9:30, it will end at 9:40). Unsure how to deal with this special case: 1) not allow pausing for targeted timers or 2) calculate the new timer duration after pausing. I will add this feature in future releases based on interest and feedback. 
- nothing else for now, but please let me know if you see anything!

<a name="acknowledgments"></a>
# Acknowledgments

- [Dean Jackson](https://github.com/deanishe) for creating the `alfred-workflow` package and for their incredible help on the Alfred mailing list. 
- Complice's creator [Malcom Ocean](https://github.com/malcolmocean) for assistance with the API

<a name="changelog"></a>
# Changelog

- 09-17-2021: version 0.1

<a name="feedback"></a>
# Feedback

Feedback welcome! If you notice a bug, or have ideas for new features, please feel free to get in touch either here, or on the [Alfred](https://www.alfredforum.com) forum. 

