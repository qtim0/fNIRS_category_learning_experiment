#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on May 20, 2022, at 17:04
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'taskPrototype'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Tim\\Google Drive\\category\\fnirs\\task-fNIRS-CR\\task-fNIRS-CR-V4_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "start"
startClock = core.Clock()
txt_start = visual.TextStim(win=win, name='txt_start',
    text='Begin Experiment\n\nPress [X]',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
#import pyxid2
#import time 
#devices = pyxid.get_xid_devices() 
#assert len(devices) > 0 
#d = devices[0] 
#d.init_device() 
#d.set_pulse_duration(1000) 
# one sweep through all lines 
#for i in range(1,9): 
#d.activate_line(lines=[i]) 
#time.sleep(1.2) 

#initalize the loop limits for each device
gaborLim = 24
ctrlLim = 24
blockLim = 5
learnlim = 180

# Initialize components for Routine "learnTrial"
learnTrialClock = core.Clock()
imgLearn = visual.ImageStim(
    win=win,
    name='imgLearn', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
keyLearn = keyboard.Keyboard()

# Initialize components for Routine "learnFb"
learnFbClock = core.Clock()
learnloopc = 0
txtLearnFb = visual.TextStim(win=win, name='txtLearnFb',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "rest0"
rest0Clock = core.Clock()
txtRest0 = visual.TextStim(win=win, name='txtRest0',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "gaborTrial"
gaborTrialClock = core.Clock()
img_gaborTrial = visual.ImageStim(
    win=win,
    name='img_gaborTrial', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_gaborTrial = keyboard.Keyboard()

# Initialize components for Routine "gaborFb"
gaborFbClock = core.Clock()
msg='doh!' #debug msg printing
gaborloopc = 0
txt_gaborfb = visual.TextStim(win=win, name='txt_gaborfb',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "rest1"
rest1Clock = core.Clock()
txtFixation1 = visual.TextStim(win=win, name='txtFixation1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "ctrlTrial"
ctrlTrialClock = core.Clock()
imgCtrlTrial = visual.ImageStim(
    win=win,
    name='imgCtrlTrial', 
    image='sin', mask=None,
    ori=0.0, pos=(0, -0.05), size=(0.8, 0.8),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
keyCtrlTrial = keyboard.Keyboard()
txtCtrlTrial = visual.TextStim(win=win, name='txtCtrlTrial',
    text='MATCH [1]                                          NO [0]',
    font='Open Sans',
    pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "ctrlFb"
ctrlFbClock = core.Clock()
msg = "oop"

ctrlloopc = 0
txtCtrlFb = visual.TextStim(win=win, name='txtCtrlFb',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
txtCtrlFbSustain = visual.TextStim(win=win, name='txtCtrlFbSustain',
    text='MATCH [1]                                          NO [0]',
    font='Open Sans',
    pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "rest2"
rest2Clock = core.Clock()
#initalize blockloop counter starting at 0
#blockloop gets ++ at end of each loop
blockloopc = 0
txtFixation2 = visual.TextStim(win=win, name='txtFixation2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "end"
endClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='yay you fin!\n\n[Q]',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "start"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
startComponents = [txt_start, key_resp]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt_start* updates
    if txt_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt_start.frameNStart = frameN  # exact frame index
        txt_start.tStart = t  # local t and not account for scr refresh
        txt_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt_start, 'tStartRefresh')  # time at next scr refresh
        txt_start.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['x'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txt_start.started', txt_start.tStartRefresh)
thisExp.addData('txt_start.stopped', txt_start.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
learnLoop = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CR_coord_arbitrary.csv'),
    seed=None, name='learnLoop')
thisExp.addLoop(learnLoop)  # add the loop to the experiment
thisLearnLoop = learnLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLearnLoop.rgb)
if thisLearnLoop != None:
    for paramName in thisLearnLoop:
        exec('{} = thisLearnLoop[paramName]'.format(paramName))

for thisLearnLoop in learnLoop:
    currentLoop = learnLoop
    # abbreviate parameter names if possible (e.g. rgb = thisLearnLoop.rgb)
    if thisLearnLoop != None:
        for paramName in thisLearnLoop:
            exec('{} = thisLearnLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    imgLearn.setImage(stimID)
    keyLearn.keys = []
    keyLearn.rt = []
    _keyLearn_allKeys = []
    # keep track of which components have finished
    learnTrialComponents = [imgLearn, keyLearn]
    for thisComponent in learnTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *imgLearn* updates
        if imgLearn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            imgLearn.frameNStart = frameN  # exact frame index
            imgLearn.tStart = t  # local t and not account for scr refresh
            imgLearn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(imgLearn, 'tStartRefresh')  # time at next scr refresh
            imgLearn.setAutoDraw(True)
        if imgLearn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > imgLearn.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                imgLearn.tStop = t  # not accounting for scr refresh
                imgLearn.frameNStop = frameN  # exact frame index
                win.timeOnFlip(imgLearn, 'tStopRefresh')  # time at next scr refresh
                imgLearn.setAutoDraw(False)
        
        # *keyLearn* updates
        waitOnFlip = False
        if keyLearn.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            keyLearn.frameNStart = frameN  # exact frame index
            keyLearn.tStart = t  # local t and not account for scr refresh
            keyLearn.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyLearn, 'tStartRefresh')  # time at next scr refresh
            keyLearn.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyLearn.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyLearn.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyLearn.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > keyLearn.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                keyLearn.tStop = t  # not accounting for scr refresh
                keyLearn.frameNStop = frameN  # exact frame index
                win.timeOnFlip(keyLearn, 'tStopRefresh')  # time at next scr refresh
                keyLearn.status = FINISHED
        if keyLearn.status == STARTED and not waitOnFlip:
            theseKeys = keyLearn.getKeys(keyList=['1', '0'], waitRelease=False)
            _keyLearn_allKeys.extend(theseKeys)
            if len(_keyLearn_allKeys):
                keyLearn.keys = _keyLearn_allKeys[-1].name  # just the last key pressed
                keyLearn.rt = _keyLearn_allKeys[-1].rt
                # was this correct?
                if (keyLearn.keys == str(keymap)) or (keyLearn.keys == keymap):
                    keyLearn.corr = 1
                else:
                    keyLearn.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial"-------
    for thisComponent in learnTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    learnLoop.addData('imgLearn.started', imgLearn.tStartRefresh)
    learnLoop.addData('imgLearn.stopped', imgLearn.tStopRefresh)
    # check responses
    if keyLearn.keys in ['', [], None]:  # No response was made
        keyLearn.keys = None
        # was no response the correct answer?!
        if str(keymap).lower() == 'none':
           keyLearn.corr = 1;  # correct non-response
        else:
           keyLearn.corr = 0;  # failed to respond (incorrectly)
    # store data for learnLoop (TrialHandler)
    learnLoop.addData('keyLearn.keys',keyLearn.keys)
    learnLoop.addData('keyLearn.corr', keyLearn.corr)
    if keyLearn.keys != None:  # we had a response
        learnLoop.addData('keyLearn.rt', keyLearn.rt)
    learnLoop.addData('keyLearn.started', keyLearn.tStartRefresh)
    learnLoop.addData('keyLearn.stopped', keyLearn.tStopRefresh)
    
    # ------Prepare to start Routine "learnFb"-------
    continueRoutine = True
    # update component parameters for each repeat
    #provides feedback for trial
    #no response/wrong shows red
    #correct repsonse shows green
    if not keyLearn.keys:
        msg = "Failed to respond"
        txtLearnFb.color = "Red"
        learnFbDur = 1.0 #fb default 1.0s
    elif keyLearn.corr: #stored on last run routine
        msg = "Correct!"
        txtLearnFb.color = "Green"
        learnFbDur = 1.0 + (2.0 - keyLearn.rt) #leftover t
    else:
        msg = "Incorrect"
        txtLearnFb.color = "Red"
        learnFbDur = 1.0 + (2.0 - keyLearn.rt)
    
    #adds loop counter
    learnloopc = learnloopc + 1
    
    #ends gabor loop at defined limit
    if learnloopc >= learnlim:  
        learnLoop.finished = True
        
    
    txtLearnFb.setText(msg)
    # keep track of which components have finished
    learnFbComponents = [txtLearnFb]
    for thisComponent in learnFbComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnFbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnFb"-------
    while continueRoutine:
        # get current time
        t = learnFbClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnFbClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txtLearnFb* updates
        if txtLearnFb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            txtLearnFb.frameNStart = frameN  # exact frame index
            txtLearnFb.tStart = t  # local t and not account for scr refresh
            txtLearnFb.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txtLearnFb, 'tStartRefresh')  # time at next scr refresh
            txtLearnFb.setAutoDraw(True)
        if txtLearnFb.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > txtLearnFb.tStartRefresh + learnFbDur-frameTolerance:
                # keep track of stop time/frame for later
                txtLearnFb.tStop = t  # not accounting for scr refresh
                txtLearnFb.frameNStop = frameN  # exact frame index
                win.timeOnFlip(txtLearnFb, 'tStopRefresh')  # time at next scr refresh
                txtLearnFb.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnFbComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnFb"-------
    for thisComponent in learnFbComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    learnLoop.addData('txtLearnFb.started', txtLearnFb.tStartRefresh)
    learnLoop.addData('txtLearnFb.stopped', txtLearnFb.tStopRefresh)
    # the Routine "learnFb" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'learnLoop'


# ------Prepare to start Routine "rest0"-------
continueRoutine = True
routineTimer.add(20.000000)
# update component parameters for each repeat
# keep track of which components have finished
rest0Components = [txtRest0]
for thisComponent in rest0Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
rest0Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "rest0"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = rest0Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=rest0Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txtRest0* updates
    if txtRest0.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txtRest0.frameNStart = frameN  # exact frame index
        txtRest0.tStart = t  # local t and not account for scr refresh
        txtRest0.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txtRest0, 'tStartRefresh')  # time at next scr refresh
        txtRest0.setAutoDraw(True)
    if txtRest0.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > txtRest0.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            txtRest0.tStop = t  # not accounting for scr refresh
            txtRest0.frameNStop = frameN  # exact frame index
            win.timeOnFlip(txtRest0, 'tStopRefresh')  # time at next scr refresh
            txtRest0.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in rest0Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "rest0"-------
for thisComponent in rest0Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('txtRest0.started', txtRest0.tStartRefresh)
thisExp.addData('txtRest0.stopped', txtRest0.tStopRefresh)

# set up handler to look after randomisation of conditions etc
blockLoop = data.TrialHandler(nReps=6.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='blockLoop')
thisExp.addLoop(blockLoop)  # add the loop to the experiment
thisBlockLoop = blockLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
if thisBlockLoop != None:
    for paramName in thisBlockLoop:
        exec('{} = thisBlockLoop[paramName]'.format(paramName))

for thisBlockLoop in blockLoop:
    currentLoop = blockLoop
    # abbreviate parameter names if possible (e.g. rgb = thisBlockLoop.rgb)
    if thisBlockLoop != None:
        for paramName in thisBlockLoop:
            exec('{} = thisBlockLoop[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    gaborLoop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('CR_coord_arbitrary.csv'),
        seed=None, name='gaborLoop')
    thisExp.addLoop(gaborLoop)  # add the loop to the experiment
    thisGaborLoop = gaborLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisGaborLoop.rgb)
    if thisGaborLoop != None:
        for paramName in thisGaborLoop:
            exec('{} = thisGaborLoop[paramName]'.format(paramName))
    
    for thisGaborLoop in gaborLoop:
        currentLoop = gaborLoop
        # abbreviate parameter names if possible (e.g. rgb = thisGaborLoop.rgb)
        if thisGaborLoop != None:
            for paramName in thisGaborLoop:
                exec('{} = thisGaborLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "gaborTrial"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        img_gaborTrial.setImage(stimID)
        key_gaborTrial.keys = []
        key_gaborTrial.rt = []
        _key_gaborTrial_allKeys = []
        # sends trigger to fNIRS on initial trial (0)
        
        #if gaborloopc == 0:
        #    d.activate_line(lines=[1])
            
        
        # keep track of which components have finished
        gaborTrialComponents = [img_gaborTrial, key_gaborTrial]
        for thisComponent in gaborTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        gaborTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "gaborTrial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = gaborTrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=gaborTrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *img_gaborTrial* updates
            if img_gaborTrial.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                img_gaborTrial.frameNStart = frameN  # exact frame index
                img_gaborTrial.tStart = t  # local t and not account for scr refresh
                img_gaborTrial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(img_gaborTrial, 'tStartRefresh')  # time at next scr refresh
                img_gaborTrial.setAutoDraw(True)
            if img_gaborTrial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > img_gaborTrial.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    img_gaborTrial.tStop = t  # not accounting for scr refresh
                    img_gaborTrial.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(img_gaborTrial, 'tStopRefresh')  # time at next scr refresh
                    img_gaborTrial.setAutoDraw(False)
            
            # *key_gaborTrial* updates
            waitOnFlip = False
            if key_gaborTrial.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_gaborTrial.frameNStart = frameN  # exact frame index
                key_gaborTrial.tStart = t  # local t and not account for scr refresh
                key_gaborTrial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_gaborTrial, 'tStartRefresh')  # time at next scr refresh
                key_gaborTrial.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_gaborTrial.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_gaborTrial.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_gaborTrial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_gaborTrial.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    key_gaborTrial.tStop = t  # not accounting for scr refresh
                    key_gaborTrial.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_gaborTrial, 'tStopRefresh')  # time at next scr refresh
                    key_gaborTrial.status = FINISHED
            if key_gaborTrial.status == STARTED and not waitOnFlip:
                theseKeys = key_gaborTrial.getKeys(keyList=['1', '0'], waitRelease=False)
                _key_gaborTrial_allKeys.extend(theseKeys)
                if len(_key_gaborTrial_allKeys):
                    key_gaborTrial.keys = _key_gaborTrial_allKeys[-1].name  # just the last key pressed
                    key_gaborTrial.rt = _key_gaborTrial_allKeys[-1].rt
                    # was this correct?
                    if (key_gaborTrial.keys == str(keymap)) or (key_gaborTrial.keys == keymap):
                        key_gaborTrial.corr = 1
                    else:
                        key_gaborTrial.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in gaborTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "gaborTrial"-------
        for thisComponent in gaborTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        gaborLoop.addData('img_gaborTrial.started', img_gaborTrial.tStartRefresh)
        gaborLoop.addData('img_gaborTrial.stopped', img_gaborTrial.tStopRefresh)
        # check responses
        if key_gaborTrial.keys in ['', [], None]:  # No response was made
            key_gaborTrial.keys = None
            # was no response the correct answer?!
            if str(keymap).lower() == 'none':
               key_gaborTrial.corr = 1;  # correct non-response
            else:
               key_gaborTrial.corr = 0;  # failed to respond (incorrectly)
        # store data for gaborLoop (TrialHandler)
        gaborLoop.addData('key_gaborTrial.keys',key_gaborTrial.keys)
        gaborLoop.addData('key_gaborTrial.corr', key_gaborTrial.corr)
        if key_gaborTrial.keys != None:  # we had a response
            gaborLoop.addData('key_gaborTrial.rt', key_gaborTrial.rt)
        gaborLoop.addData('key_gaborTrial.started', key_gaborTrial.tStartRefresh)
        gaborLoop.addData('key_gaborTrial.stopped', key_gaborTrial.tStopRefresh)
        
        # ------Prepare to start Routine "gaborFb"-------
        continueRoutine = True
        # update component parameters for each repeat
        #provides feedback for trial
        #no response/wrong shows red
        #correct repsonse shows green
        if not key_gaborTrial.keys:
            msg = "Failed to respond"
            txt_gaborfb.color = "Red"
            gaborfbdur = 0.5 #fb default 0.5s
        elif key_gaborTrial.corr: #stored on last run routine
            msg = "Correct!"
            txt_gaborfb.color = "Green"
            gaborfbdur = 0.5 + (1.5 - key_gaborTrial.rt) #leftover t
        else:
            msg = "Incorrect"
            txt_gaborfb.color = "Red"
            gaborfbdur = 0.5 + (1.5 - key_gaborTrial.rt)
        
        #adds loop counter
        gaborloopc = gaborloopc + 1 
        
        #ends gabor loop at defined limit
        if gaborloopc >= gaborLim:  
            gaborLoop.finished = True
            
        
        txt_gaborfb.setText(msg)
        # keep track of which components have finished
        gaborFbComponents = [txt_gaborfb]
        for thisComponent in gaborFbComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        gaborFbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "gaborFb"-------
        while continueRoutine:
            # get current time
            t = gaborFbClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=gaborFbClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *txt_gaborfb* updates
            if txt_gaborfb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                txt_gaborfb.frameNStart = frameN  # exact frame index
                txt_gaborfb.tStart = t  # local t and not account for scr refresh
                txt_gaborfb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(txt_gaborfb, 'tStartRefresh')  # time at next scr refresh
                txt_gaborfb.setAutoDraw(True)
            if txt_gaborfb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > txt_gaborfb.tStartRefresh + gaborfbdur-frameTolerance:
                    # keep track of stop time/frame for later
                    txt_gaborfb.tStop = t  # not accounting for scr refresh
                    txt_gaborfb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(txt_gaborfb, 'tStopRefresh')  # time at next scr refresh
                    txt_gaborfb.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in gaborFbComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "gaborFb"-------
        for thisComponent in gaborFbComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        gaborLoop.addData('txt_gaborfb.started', txt_gaborfb.tStartRefresh)
        gaborLoop.addData('txt_gaborfb.stopped', txt_gaborfb.tStopRefresh)
        # the Routine "gaborFb" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'gaborLoop'
    
    
    # ------Prepare to start Routine "rest1"-------
    continueRoutine = True
    # update component parameters for each repeat
    #resets gabor loopcounter for next iteration
    gaborloopc = 0 
    
    #declare vector of jittered rest times
    #assign duration based on blockloop index
    #5B x 24T x 2s
    r1_jitter = [12,14,16,18,20]
    r1_jitdur = r1_jitter[blockloopc]
    
    
    txtFixation1.setText('+')
    # keep track of which components have finished
    rest1Components = [txtFixation1]
    for thisComponent in rest1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rest1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest1"-------
    while continueRoutine:
        # get current time
        t = rest1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rest1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txtFixation1* updates
        if txtFixation1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            txtFixation1.frameNStart = frameN  # exact frame index
            txtFixation1.tStart = t  # local t and not account for scr refresh
            txtFixation1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txtFixation1, 'tStartRefresh')  # time at next scr refresh
            txtFixation1.setAutoDraw(True)
        if txtFixation1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > txtFixation1.tStartRefresh + r1_jitdur-frameTolerance:
                # keep track of stop time/frame for later
                txtFixation1.tStop = t  # not accounting for scr refresh
                txtFixation1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(txtFixation1, 'tStopRefresh')  # time at next scr refresh
                txtFixation1.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rest1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest1"-------
    for thisComponent in rest1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockLoop.addData('txtFixation1.started', txtFixation1.tStartRefresh)
    blockLoop.addData('txtFixation1.stopped', txtFixation1.tStopRefresh)
    # the Routine "rest1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    ctrlLoop = data.TrialHandler(nReps=1.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('ctrl_coord.csv'),
        seed=None, name='ctrlLoop')
    thisExp.addLoop(ctrlLoop)  # add the loop to the experiment
    thisCtrlLoop = ctrlLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCtrlLoop.rgb)
    if thisCtrlLoop != None:
        for paramName in thisCtrlLoop:
            exec('{} = thisCtrlLoop[paramName]'.format(paramName))
    
    for thisCtrlLoop in ctrlLoop:
        currentLoop = ctrlLoop
        # abbreviate parameter names if possible (e.g. rgb = thisCtrlLoop.rgb)
        if thisCtrlLoop != None:
            for paramName in thisCtrlLoop:
                exec('{} = thisCtrlLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ctrlTrial"-------
        continueRoutine = True
        routineTimer.add(1.500000)
        # update component parameters for each repeat
        # sends trigger to fNIRS on initial trial (0)
        
        #if ctrlloopc == 0:
        #    d.activate_line(lines=[2])
        imgCtrlTrial.setImage(ctrlID)
        keyCtrlTrial.keys = []
        keyCtrlTrial.rt = []
        _keyCtrlTrial_allKeys = []
        # keep track of which components have finished
        ctrlTrialComponents = [imgCtrlTrial, keyCtrlTrial, txtCtrlTrial]
        for thisComponent in ctrlTrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ctrlTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ctrlTrial"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ctrlTrialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ctrlTrialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *imgCtrlTrial* updates
            if imgCtrlTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                imgCtrlTrial.frameNStart = frameN  # exact frame index
                imgCtrlTrial.tStart = t  # local t and not account for scr refresh
                imgCtrlTrial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(imgCtrlTrial, 'tStartRefresh')  # time at next scr refresh
                imgCtrlTrial.setAutoDraw(True)
            if imgCtrlTrial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > imgCtrlTrial.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    imgCtrlTrial.tStop = t  # not accounting for scr refresh
                    imgCtrlTrial.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(imgCtrlTrial, 'tStopRefresh')  # time at next scr refresh
                    imgCtrlTrial.setAutoDraw(False)
            
            # *keyCtrlTrial* updates
            waitOnFlip = False
            if keyCtrlTrial.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                keyCtrlTrial.frameNStart = frameN  # exact frame index
                keyCtrlTrial.tStart = t  # local t and not account for scr refresh
                keyCtrlTrial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(keyCtrlTrial, 'tStartRefresh')  # time at next scr refresh
                keyCtrlTrial.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(keyCtrlTrial.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(keyCtrlTrial.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if keyCtrlTrial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > keyCtrlTrial.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    keyCtrlTrial.tStop = t  # not accounting for scr refresh
                    keyCtrlTrial.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(keyCtrlTrial, 'tStopRefresh')  # time at next scr refresh
                    keyCtrlTrial.status = FINISHED
            if keyCtrlTrial.status == STARTED and not waitOnFlip:
                theseKeys = keyCtrlTrial.getKeys(keyList=['1', '0'], waitRelease=False)
                _keyCtrlTrial_allKeys.extend(theseKeys)
                if len(_keyCtrlTrial_allKeys):
                    keyCtrlTrial.keys = _keyCtrlTrial_allKeys[-1].name  # just the last key pressed
                    keyCtrlTrial.rt = _keyCtrlTrial_allKeys[-1].rt
                    # was this correct?
                    if (keyCtrlTrial.keys == str(ans)) or (keyCtrlTrial.keys == ans):
                        keyCtrlTrial.corr = 1
                    else:
                        keyCtrlTrial.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *txtCtrlTrial* updates
            if txtCtrlTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                txtCtrlTrial.frameNStart = frameN  # exact frame index
                txtCtrlTrial.tStart = t  # local t and not account for scr refresh
                txtCtrlTrial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(txtCtrlTrial, 'tStartRefresh')  # time at next scr refresh
                txtCtrlTrial.setAutoDraw(True)
            if txtCtrlTrial.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > txtCtrlTrial.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    txtCtrlTrial.tStop = t  # not accounting for scr refresh
                    txtCtrlTrial.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(txtCtrlTrial, 'tStopRefresh')  # time at next scr refresh
                    txtCtrlTrial.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ctrlTrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ctrlTrial"-------
        for thisComponent in ctrlTrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ctrlLoop.addData('imgCtrlTrial.started', imgCtrlTrial.tStartRefresh)
        ctrlLoop.addData('imgCtrlTrial.stopped', imgCtrlTrial.tStopRefresh)
        # check responses
        if keyCtrlTrial.keys in ['', [], None]:  # No response was made
            keyCtrlTrial.keys = None
            # was no response the correct answer?!
            if str(ans).lower() == 'none':
               keyCtrlTrial.corr = 1;  # correct non-response
            else:
               keyCtrlTrial.corr = 0;  # failed to respond (incorrectly)
        # store data for ctrlLoop (TrialHandler)
        ctrlLoop.addData('keyCtrlTrial.keys',keyCtrlTrial.keys)
        ctrlLoop.addData('keyCtrlTrial.corr', keyCtrlTrial.corr)
        if keyCtrlTrial.keys != None:  # we had a response
            ctrlLoop.addData('keyCtrlTrial.rt', keyCtrlTrial.rt)
        ctrlLoop.addData('keyCtrlTrial.started', keyCtrlTrial.tStartRefresh)
        ctrlLoop.addData('keyCtrlTrial.stopped', keyCtrlTrial.tStopRefresh)
        ctrlLoop.addData('txtCtrlTrial.started', txtCtrlTrial.tStartRefresh)
        ctrlLoop.addData('txtCtrlTrial.stopped', txtCtrlTrial.tStopRefresh)
        
        # ------Prepare to start Routine "ctrlFb"-------
        continueRoutine = True
        # update component parameters for each repeat
        #provides feedback for ctrl trials
        if not keyCtrlTrial.keys:
            msg = "Failed to respond"
            txtCtrlFb.color = "Red"
            ctrlfbdur = 0.5 #fb default 0.5s
        elif keyCtrlTrial.corr: #stored on last run routine
            msg = "Correct!"
            txtCtrlFb.color = "Green"
            ctrlfbdur = 0.5 + (1.5 - keyCtrlTrial.rt) #leftover t
        else:
            msg = "Incorrect"
            txtCtrlFb.color = "Red"
            ctrlfbdur = 0.5 + (1.5 - keyCtrlTrial.rt)
        
        #adds to control loop counter
        ctrlloopc = ctrlloopc + 1 
        
        #ends trial at defined limit
        if ctrlloopc >= ctrlLim: 
            ctrlLoop.finished = True
            
        
        txtCtrlFb.setText(msg)
        # keep track of which components have finished
        ctrlFbComponents = [txtCtrlFb, txtCtrlFbSustain]
        for thisComponent in ctrlFbComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ctrlFbClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ctrlFb"-------
        while continueRoutine:
            # get current time
            t = ctrlFbClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ctrlFbClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *txtCtrlFb* updates
            if txtCtrlFb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                txtCtrlFb.frameNStart = frameN  # exact frame index
                txtCtrlFb.tStart = t  # local t and not account for scr refresh
                txtCtrlFb.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(txtCtrlFb, 'tStartRefresh')  # time at next scr refresh
                txtCtrlFb.setAutoDraw(True)
            if txtCtrlFb.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > txtCtrlFb.tStartRefresh + ctrlfbdur-frameTolerance:
                    # keep track of stop time/frame for later
                    txtCtrlFb.tStop = t  # not accounting for scr refresh
                    txtCtrlFb.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(txtCtrlFb, 'tStopRefresh')  # time at next scr refresh
                    txtCtrlFb.setAutoDraw(False)
            
            # *txtCtrlFbSustain* updates
            if txtCtrlFbSustain.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                txtCtrlFbSustain.frameNStart = frameN  # exact frame index
                txtCtrlFbSustain.tStart = t  # local t and not account for scr refresh
                txtCtrlFbSustain.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(txtCtrlFbSustain, 'tStartRefresh')  # time at next scr refresh
                txtCtrlFbSustain.setAutoDraw(True)
            if txtCtrlFbSustain.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > txtCtrlFbSustain.tStartRefresh + ctrlfbdur-frameTolerance:
                    # keep track of stop time/frame for later
                    txtCtrlFbSustain.tStop = t  # not accounting for scr refresh
                    txtCtrlFbSustain.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(txtCtrlFbSustain, 'tStopRefresh')  # time at next scr refresh
                    txtCtrlFbSustain.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ctrlFbComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ctrlFb"-------
        for thisComponent in ctrlFbComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ctrlLoop.addData('txtCtrlFb.started', txtCtrlFb.tStartRefresh)
        ctrlLoop.addData('txtCtrlFb.stopped', txtCtrlFb.tStopRefresh)
        ctrlLoop.addData('txtCtrlFbSustain.started', txtCtrlFbSustain.tStartRefresh)
        ctrlLoop.addData('txtCtrlFbSustain.stopped', txtCtrlFbSustain.tStopRefresh)
        # the Routine "ctrlFb" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'ctrlLoop'
    
    
    # ------Prepare to start Routine "rest2"-------
    continueRoutine = True
    # update component parameters for each repeat
    #resets ctrl loop counter for next iteration
    ctrlloopc = 0 
    
    #declare vector of jittered rest times
    #assign duration based on blockloop index
    #5B x 24T x 2s
    r2_jitter = [20,18,16,14,12]
    r2_jitdur = r2_jitter[blockloopc]
    
    #add to blockloop counter
    blockloopc = blockloopc + 1
    
    #ends loop after once blocklimit is reached
    if blockloopc >= blockLim:
        blockLoop.finished = True
    
    
    txtFixation2.setText('+')
    # keep track of which components have finished
    rest2Components = [txtFixation2]
    for thisComponent in rest2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rest2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest2"-------
    while continueRoutine:
        # get current time
        t = rest2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rest2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *txtFixation2* updates
        if txtFixation2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            txtFixation2.frameNStart = frameN  # exact frame index
            txtFixation2.tStart = t  # local t and not account for scr refresh
            txtFixation2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(txtFixation2, 'tStartRefresh')  # time at next scr refresh
            txtFixation2.setAutoDraw(True)
        if txtFixation2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > txtFixation2.tStartRefresh + r2_jitdur-frameTolerance:
                # keep track of stop time/frame for later
                txtFixation2.tStop = t  # not accounting for scr refresh
                txtFixation2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(txtFixation2, 'tStopRefresh')  # time at next scr refresh
                txtFixation2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rest2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest2"-------
    for thisComponent in rest2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    blockLoop.addData('txtFixation2.started', txtFixation2.tStartRefresh)
    blockLoop.addData('txtFixation2.stopped', txtFixation2.tStopRefresh)
    # the Routine "rest2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 6.0 repeats of 'blockLoop'


# ------Prepare to start Routine "end"-------
continueRoutine = True
# update component parameters for each repeat
key_end.keys = []
key_end.rt = []
_key_end_allKeys = []
# keep track of which components have finished
endComponents = [text, key_end]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_end* updates
    waitOnFlip = False
    if key_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_end.frameNStart = frameN  # exact frame index
        key_end.tStart = t  # local t and not account for scr refresh
        key_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_end, 'tStartRefresh')  # time at next scr refresh
        key_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_end.status == STARTED and not waitOnFlip:
        theseKeys = key_end.getKeys(keyList=['q'], waitRelease=False)
        _key_end_allKeys.extend(theseKeys)
        if len(_key_end_allKeys):
            key_end.keys = _key_end_allKeys[-1].name  # just the last key pressed
            key_end.rt = _key_end_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_end.keys in ['', [], None]:  # No response was made
    key_end.keys = None
thisExp.addData('key_end.keys',key_end.keys)
if key_end.keys != None:  # we had a response
    thisExp.addData('key_end.rt', key_end.rt)
thisExp.addData('key_end.started', key_end.tStartRefresh)
thisExp.addData('key_end.stopped', key_end.tStopRefresh)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
