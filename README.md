# Fusion
### Video Demo:  [Watch How Fusion Works](https://cs50.storage.iran.liara.space/Fusion.mp4)
## What Is Fusion:

Fusion is a python application, which recursively call itself. Downloading, modifying and storing the content of a website in relative way. Thus make the files portable. It is mainly programmed for documents. Make them available for situations you don't have internet access.

## Why Fusion:

its first name was supposed to be collective, but somehow the idea of how it works, remind me of nuclear reactions. (Technically, the name must be fission but fusion sounds better to me !!!)

## How Fusion Works

Well, simply it starts from user URL, validating it, catch the content, scan for other links and recursively do this process for every one of them, until a that link content does not contain a link.

## What _project.py_ Does

Project file take care of error handling and some validation, in addition of the paint function which makes a text colored inside a terminal.

## What _fusion.py_ Does

fusion file contains the core part of the program. a class with name of _Trigger_ as it sounds stars the reaction (recursion). additionally does some initializations that are not supposed to happen every recursion. class _Fusion_ take care of the rest of the process. function _init_ asks for content of the URl, then call collective to find other links (function _find_urls_ takes care of the links inside the file, using a regular expression). Since the recursion at this scale could potentially never end and use a lot of resources, some break point are considered to stop the operation. Firstly relative links are transformed to absolute links. Then we check if the link is inside the same website and check if we have not already call it (This avoids circular loops with infinitive recursions). if all the conditions are met we call _Fusion_ on every one of those links. after being done, both relative and absolute links are transformed to make the connection between links okay again. Finally function _save_ takes care of saving.

## What You Should Consider

This is personal project for personal usage. There are still a lot of things that must be fixed like improving the recursion (right now, typing I have a few ideas how to improve speed). there are some links that are tricky,cause the whole program to crash. the way how I look for the links is just a over-simplification (it just looks for href and src tags).

**Feel Free To Reach Me:** so.ra.as@outlook.com