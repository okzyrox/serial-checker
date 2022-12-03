# serial-checker

## What does this do?

The serial-checker python script checks the serial number on your Nintendo Switch, and validates is patchness for Homebrew modification through fusee-gelee.

It has 3 possible outcomes: 
- Unpatched: you can homebrew
- Possibly Patched: you might not be able to mod this version; includes most consoles that have been sent back to nintendo for repair.
- Patched: you cant homebrew

## Where is the json-file's data sourced from?

- [GBAtemp post](https://gbatemp.net/threads/switch-informations-by-serial-number-read-the-first-post-before-asking-questions.481215/)
- [Google sheet (partially outdated)](https://docs.google.com/spreadsheets/d/1ifBIsbTeTpk-bL1Ul9Z9ORPVX3BNH2pHlGW1Z0g8nvM/edit?usp=sharing)

## How reliable is the validity checking?

It should be mostly reliable, however there can be false-positives that this software can't account for. This is common for when you check only the first few characters of your serial code.

## What about the Switch OLED or Lite?

Confirmed patched, including the 2019/2018 HAC-001(-01) release of the base switch, although you can bypass it through other means.
