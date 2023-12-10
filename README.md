# alfred-intend 
(previously Alfred-Complice)

### A workflow to manage your [Intend](https://intend.do/) intentions and timers with  [Alfred](https://www.alfredapp.com/)



![](images/intend-screencast.gif "")
<a href="https://github.com/giovannicoppola/alfred-intend/releases/latest/">
  
  <img alt="Downloads"
       src="https://img.shields.io/github/downloads/giovannicoppola/alfred-intend/total?color=purple&label=Downloads"><br/>
</a>
<!-- MarkdownTOC autolink="true" bracket="round" depth="3" autoanchor="true" -->

- [Setting up](#setting-up)
- [Basic Usage](#usage)
- [Known Issues](#known-issues)
- [Acknowledgments](#acknowledgments)
- [Changelog](#changelog)
- [Feedback](#feedback)

<!-- /MarkdownTOC -->


<h1 id="setting-up">Setting up ⚙️</h1>

### Needed

- Alfred with Powerpack license
- Intend account (use [this](https://intend.do/?r=4z020qsycl) link to get a bonus third week of free trial)
- Intend API Token (available [here](https://intend.do/$USERNAME/auth_token) while you are logged in)




1. Download the [most recent release](https://github.com/giovannicoppola/alfred-intend/releases/latest) of `alfred-intend` from Github and double-click to install
2. Get your Intend Auth Token 
	- in [Intend](https://intend.do/$USERNAME/auth_token), Select and copy to clipboard the auth token. 
	_Example_: if the string is `{"username":"johndoe","auth_token":"abcd1234"}`, copy `abcd1234` (without quotes)

3. In Alfred, open the 'Configure Workflow' window in `Alfred Intend` preferences
				
	- set the `TOKEN` variable to the Intend Auth Token retrieved in Step 2
	- _Optional:_ set the `POMOLENGTH` variable (predefined value: 25 min)
	- _Optional:_ set the `TIMERLENGTH` variable (predefined value: 10 min)
	
4. _Optional:_ Setup a hotkey to launch alfred-intend
5. _Optional:_ Change the keyword to launch alfred-intend
	- keyword currently set to `!c`



<h1 id="usage">Basic Usage 📖</h1>

Most features are self-explanatory, briefly described below:
## Intentions
- Add new intentions (remember to add the goal number (e.g. `1)`) otherwise it will be entered as `&`)
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



<h1 id="known-issues">Limitations & Known issues ⚠️</h1>


- Pausing a targeted time will shift the end time accordingly (for example, if you pause for 10 min and then restart a timer that is supposed to end at 9:30, it will end at 9:40). Unsure how to deal with this special case: 1) not allow pausing for targeted timers or 2) calculate the new timer duration after pausing. I will add this feature in future releases based on interest and feedback. 
- nothing else for now, but please let me know if you see anything!

<h1 id="acknowledgments">Acknowledgments 😀</h1>

- [Dean Jackson](https://github.com/deanishe) for creating the `alfred-workflow` package and for their incredible help on the Alfred mailing list. 
- Intend's creator [Malcom Ocean](https://github.com/malcolmocean) for assistance with the API

<h1 id="changelog">Changelog 🧰</h1>

- 12-10-2023: version 0.4.2 URL updates to intend.do
- 07-18-2023: version 0.4.1 sorting intentions
- 07-15-2023: version 0.4 (Rebranding to Intend, bug fixes)
- 12-04-2022: version 0.3 (Alfred 5)
- 03-16-2021: version 0.2 (Python3, reduced dependencies)
- 09-17-2021: version 0.1


<h1 id="feedback">Feedback 🧐</h1>

Feedback welcome! If you notice a bug, or have ideas for new features, please feel free to get in touch either here, or on the [Alfred](https://www.alfredforum.com) forum. 

