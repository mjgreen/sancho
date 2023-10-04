#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.2),
    on October 03, 2023, at 13:50
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.2'
expName = 'AssociativeLearning_v2'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'group': '',
    'session': '01',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\User\\Desktop\\Reward_emotion_exp_adjusted_19_10_22\\AssociativeLearning_v2_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=[1536, 864], fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units=None
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = None
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "intro" ---
    intro_text = visual.TextStim(win=win, name='intro_text',
        text='Welcome!\n\nIn this task you will be presented with some shapes and labels, and asked to remember them.\n\nYou will complete three different versions of this task.\n\nIn one version you will be shown different words relating to different directions. In another version you will be shown different amounts of money, and in another version you will be shown different facial expressions.\n\nPress space to start.',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=1.2, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    intro_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "instructions" ---
    # Run 'Begin Experiment' code from experiment_code
    import random
    import numpy as np
    instructions_text = visual.TextStim(win=win, name='instructions_text',
        text='',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=1.3, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    instructions_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "practice_fixation" ---
    practice_fixation_cross = visual.ShapeStim(
        win=win, name='practice_fixation_cross', vertices='cross',
        size=(0.06, 0.1),
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[255,0,0], fillColor=[255,0,0],
        opacity=1, depth=0.0, interpolate=True)
    
    # --- Initialize components for Routine "practice_target" ---
    practice_target_label = visual.TextStim(win=win, name='practice_target_label',
        text='',
        font='Arial',
        pos=(0, -0.3), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    practice_target_plus = visual.TextStim(win=win, name='practice_target_plus',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    practice_target_shape = visual.ImageStim(
        win=win,
        name='practice_target_shape', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0.3), size=(0.18, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-3.0)
    practice_resp = keyboard.Keyboard()
    practice_target_label_valence = visual.ImageStim(
        win=win,
        name='practice_target_label_valence', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, -0.3), size=(0.2, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "practice_ITI" ---
    ITI_text = visual.TextStim(win=win, name='ITI_text',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "practice_feedback" ---
    practice_feedback_text = visual.TextStim(win=win, name='practice_feedback_text',
        text='',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "practice_end" ---
    self_practice_end_text = visual.TextStim(win=win, name='self_practice_end_text',
        text="End of practice.\n\nPlease press 'SPACEBAR' to start the real experiment.\n\nPLEASE RESPOND AS QUICKLY AND ACCURATELY AS POSSIBLE.",
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    self_practice_end_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "trial_fixation" ---
    self_trial_fixation_cross = visual.ShapeStim(
        win=win, name='self_trial_fixation_cross', vertices='cross',
        size=(0.06, 0.1),
        ori=0, pos=(0, 0), anchor='center',
        lineWidth=1,     colorSpace='rgb',  lineColor=[255,0,0], fillColor=[255,0,0],
        opacity=1, depth=-1.0, interpolate=True)
    
    # --- Initialize components for Routine "trial_target" ---
    trial_target_label = visual.TextStim(win=win, name='trial_target_label',
        text='',
        font='Arial',
        pos=(0, -0.3), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    trial_target_plus = visual.TextStim(win=win, name='trial_target_plus',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    trial_target_shape = visual.ImageStim(
        win=win,
        name='trial_target_shape', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0.3), size=(0.18, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-3.0)
    trial_resp = keyboard.Keyboard()
    trial_target_label_valence = visual.ImageStim(
        win=win,
        name='trial_target_label_valence', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, -0.3), size=(0.2, 0.4),
        color=[1,1,1], colorSpace='rgb', opacity=1.0,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-5.0)
    
    # --- Initialize components for Routine "trial_ITI" ---
    self_trial_ITI_text = visual.TextStim(win=win, name='self_trial_ITI_text',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial_feedback" ---
    self_trial_feedback_text = visual.TextStim(win=win, name='self_trial_feedback_text',
        text='',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial_break" ---
    trial_break_text = visual.TextStim(win=win, name='trial_break_text',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    image = visual.ImageStim(
        win=win,
        name='image', 
        image=None, mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.5, 0.5),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "trials_end" ---
    trials_end_text = visual.TextStim(win=win, name='trials_end_text',
        text='Well done! You have completed these trials.\n\nPress the spacebar to continue.',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    trials_end_resp = keyboard.Keyboard()
    
    # --- Initialize components for Routine "end" ---
    text = visual.TextStim(win=win, name='text',
        text='Well done! You have finished the task!',
        font='Arial',
        pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # set up handler to look after randomisation of conditions etc
    key_commands = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('KeyboardCommand.xlsx', selection='np.random.choice(2, size=1, replace=False)'),
        seed=None, name='key_commands')
    thisExp.addLoop(key_commands)  # add the loop to the experiment
    thisKey_command = key_commands.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisKey_command.rgb)
    if thisKey_command != None:
        for paramName in thisKey_command:
            globals()[paramName] = thisKey_command[paramName]
    
    for thisKey_command in key_commands:
        currentLoop = key_commands
        thisExp.timestampOnFlip(win, 'thisRow.t')
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                inputs=inputs, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisKey_command.rgb)
        if thisKey_command != None:
            for paramName in thisKey_command:
                globals()[paramName] = thisKey_command[paramName]
        
        # --- Prepare to start Routine "intro" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('intro.started', globalClock.getTime())
        intro_resp.keys = []
        intro_resp.rt = []
        _intro_resp_allKeys = []
        # keep track of which components have finished
        introComponents = [intro_text, intro_resp]
        for thisComponent in introComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "intro" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *intro_text* updates
            
            # if intro_text is starting this frame...
            if intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intro_text.frameNStart = frameN  # exact frame index
                intro_text.tStart = t  # local t and not account for scr refresh
                intro_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intro_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'intro_text.started')
                # update status
                intro_text.status = STARTED
                intro_text.setAutoDraw(True)
            
            # if intro_text is active this frame...
            if intro_text.status == STARTED:
                # update params
                pass
            
            # *intro_resp* updates
            waitOnFlip = False
            
            # if intro_resp is starting this frame...
            if intro_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                intro_resp.frameNStart = frameN  # exact frame index
                intro_resp.tStart = t  # local t and not account for scr refresh
                intro_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(intro_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'intro_resp.started')
                # update status
                intro_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(intro_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(intro_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if intro_resp.status == STARTED and not waitOnFlip:
                theseKeys = intro_resp.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                _intro_resp_allKeys.extend(theseKeys)
                if len(_intro_resp_allKeys):
                    intro_resp.keys = _intro_resp_allKeys[-1].name  # just the last key pressed
                    intro_resp.rt = _intro_resp_allKeys[-1].rt
                    intro_resp.duration = _intro_resp_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in introComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "intro" ---
        for thisComponent in introComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('intro.stopped', globalClock.getTime())
        # the Routine "intro" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        task_order = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('Group' + expInfo['group'] + '.xlsx'),
            seed=None, name='task_order')
        thisExp.addLoop(task_order)  # add the loop to the experiment
        thisTask_order = task_order.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTask_order.rgb)
        if thisTask_order != None:
            for paramName in thisTask_order:
                globals()[paramName] = thisTask_order[paramName]
        
        for thisTask_order in task_order:
            currentLoop = task_order
            thisExp.timestampOnFlip(win, 'thisRow.t')
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    inputs=inputs, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTask_order.rgb)
            if thisTask_order != None:
                for paramName in thisTask_order:
                    globals()[paramName] = thisTask_order[paramName]
            
            # set up handler to look after randomisation of conditions etc
            task_block = data.TrialHandler(nReps=1, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=data.importConditions(Task + 'Task.xlsx', selection='np.random.choice(6, size=1, replace=False)'),
                seed=None, name='task_block')
            thisExp.addLoop(task_block)  # add the loop to the experiment
            thisTask_block = task_block.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTask_block.rgb)
            if thisTask_block != None:
                for paramName in thisTask_block:
                    globals()[paramName] = thisTask_block[paramName]
            
            for thisTask_block in task_block:
                currentLoop = task_block
                thisExp.timestampOnFlip(win, 'thisRow.t')
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        inputs=inputs, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                )
                # abbreviate parameter names if possible (e.g. rgb = thisTask_block.rgb)
                if thisTask_block != None:
                    for paramName in thisTask_block:
                        globals()[paramName] = thisTask_block[paramName]
                
                # --- Prepare to start Routine "instructions" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('instructions.started', globalClock.getTime())
                # Run 'Begin Routine' code from experiment_code
                #Changing the different labels...
                if Task == 'Control':
                    Label1_type = 'sky'
                    Label2_type = 'earth'
                    Label3_type = 'air'
                    Shape1_type = 'Triangle'
                    Shape2_type = 'Square'
                    Shape3_type = 'Circle'
                elif Task == 'Reward':
                    Label1_type = 'HighReward'
                    Label2_type = 'MediumReward'
                    Label3_type = 'LowReward'
                    Shape1_type = 'Pentagon'
                    Shape2_type = 'Diamond'
                    Shape3_type = 'Oval'
                elif Task == 'Valence':
                    Label1_type = 'Happy'
                    Label2_type = 'Neutral'
                    Label3_type = 'Sad'
                    Shape1_type = 'Hexagon'
                    Shape2_type = 'Rectangle'
                    Shape3_type = 'Star'
                
                
                instr_message = ("In this version of the task you will learn to associate the {} with {}, the {} with {}, and the {} with {}.\n\nTry to remember these! Take your time \n\nYou will be presented with different combinations of these shapes and {}. Your task is to judge whether the presented shape and {} match with what we have told you above. \n\nPress '{}' if the shape and {} match, and '{}' if they do not match. \n \n Place your fingers on these keys and then Press any key to start your practice" .format(Shape1_type, intro_label1, Shape2_type, intro_label2, Shape3_type, intro_label3, intro_label_type1, intro_label_type2, Yes, intro_label_type2, No))
                instructions_text.setText(instr_message)
                instructions_resp.keys = []
                instructions_resp.rt = []
                _instructions_resp_allKeys = []
                # keep track of which components have finished
                instructionsComponents = [instructions_text, instructions_resp]
                for thisComponent in instructionsComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "instructions" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *instructions_text* updates
                    
                    # if instructions_text is starting this frame...
                    if instructions_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        instructions_text.frameNStart = frameN  # exact frame index
                        instructions_text.tStart = t  # local t and not account for scr refresh
                        instructions_text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(instructions_text, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'instructions_text.started')
                        # update status
                        instructions_text.status = STARTED
                        instructions_text.setAutoDraw(True)
                    
                    # if instructions_text is active this frame...
                    if instructions_text.status == STARTED:
                        # update params
                        pass
                    
                    # *instructions_resp* updates
                    waitOnFlip = False
                    
                    # if instructions_resp is starting this frame...
                    if instructions_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        instructions_resp.frameNStart = frameN  # exact frame index
                        instructions_resp.tStart = t  # local t and not account for scr refresh
                        instructions_resp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(instructions_resp, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'instructions_resp.started')
                        # update status
                        instructions_resp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(instructions_resp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(instructions_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if instructions_resp.status == STARTED and not waitOnFlip:
                        theseKeys = instructions_resp.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                        _instructions_resp_allKeys.extend(theseKeys)
                        if len(_instructions_resp_allKeys):
                            instructions_resp.keys = _instructions_resp_allKeys[-1].name  # just the last key pressed
                            instructions_resp.rt = _instructions_resp_allKeys[-1].rt
                            instructions_resp.duration = _instructions_resp_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in instructionsComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "instructions" ---
                for thisComponent in instructionsComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('instructions.stopped', globalClock.getTime())
                # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # --- Prepare to start Routine "practice_fixation" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('practice_fixation.started', globalClock.getTime())
                # keep track of which components have finished
                practice_fixationComponents = [practice_fixation_cross]
                for thisComponent in practice_fixationComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "practice_fixation" ---
                routineForceEnded = not continueRoutine
                while continueRoutine and routineTimer.getTime() < 1.0:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *practice_fixation_cross* updates
                    
                    # if practice_fixation_cross is starting this frame...
                    if practice_fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        practice_fixation_cross.frameNStart = frameN  # exact frame index
                        practice_fixation_cross.tStart = t  # local t and not account for scr refresh
                        practice_fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(practice_fixation_cross, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'practice_fixation_cross.started')
                        # update status
                        practice_fixation_cross.status = STARTED
                        practice_fixation_cross.setAutoDraw(True)
                    
                    # if practice_fixation_cross is active this frame...
                    if practice_fixation_cross.status == STARTED:
                        # update params
                        pass
                    
                    # if practice_fixation_cross is stopping this frame...
                    if practice_fixation_cross.status == STARTED:
                        # is it time to stop? (based on global clock, using actual start)
                        if tThisFlipGlobal > practice_fixation_cross.tStartRefresh + 1-frameTolerance:
                            # keep track of stop time/frame for later
                            practice_fixation_cross.tStop = t  # not accounting for scr refresh
                            practice_fixation_cross.frameNStop = frameN  # exact frame index
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'practice_fixation_cross.stopped')
                            # update status
                            practice_fixation_cross.status = FINISHED
                            practice_fixation_cross.setAutoDraw(False)
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in practice_fixationComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "practice_fixation" ---
                for thisComponent in practice_fixationComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('practice_fixation.stopped', globalClock.getTime())
                # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                if routineForceEnded:
                    routineTimer.reset()
                else:
                    routineTimer.addTime(-1.000000)
                
                # set up handler to look after randomisation of conditions etc
                practice_trial = data.TrialHandler(nReps=2, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=data.importConditions(Task + 'TrialStim.xlsx'),
                    seed=None, name='practice_trial')
                thisExp.addLoop(practice_trial)  # add the loop to the experiment
                thisPractice_trial = practice_trial.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
                if thisPractice_trial != None:
                    for paramName in thisPractice_trial:
                        globals()[paramName] = thisPractice_trial[paramName]
                
                for thisPractice_trial in practice_trial:
                    currentLoop = practice_trial
                    thisExp.timestampOnFlip(win, 'thisRow.t')
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            inputs=inputs, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
                    if thisPractice_trial != None:
                        for paramName in thisPractice_trial:
                            globals()[paramName] = thisPractice_trial[paramName]
                    
                    # --- Prepare to start Routine "practice_target" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('practice_target.started', globalClock.getTime())
                    # Run 'Begin Routine' code from practice_code
                    #Assigning correct labels (valence isn't included as text because this is an image)
                    if Task == 'Valence':
                        label_text = ''
                    else:
                        label_text = Label
                    
                    #Using image for valence labels
                    if Task == 'Valence':
                        label_image = 'Stimuli/' + Label + '.bmp'
                    else:
                        label_image = 'Stimuli/Empty.bmp'
                    
                    #Setting opacity of image to be 0 if task isn't valence
                    if Task == 'Valence':
                        image_opacity = 1
                    else:
                        image_opacity = 0
                    
                    #Assigning correct shapes
                    if Task == 'Control':
                        if Target == 'sky':
                            shape = 'Stimuli/' + Label1 + '.bmp'
                        elif Target == 'earth':
                            shape = 'Stimuli/' + Label2 + '.bmp'
                        elif Target == 'air':
                            shape = 'Stimuli/' + Label3 + '.bmp'
                    elif Task == 'Reward':
                        if Target == 'HighReward':
                            shape = 'Stimuli/' + Label1 + '.bmp'
                        elif Target == 'MediumReward':
                            shape = 'Stimuli/' + Label2 + '.bmp'
                        elif Target == 'LowReward':
                            shape = 'Stimuli/' + Label3 + '.bmp'
                    elif Task == 'Valence':
                        if Target == 'Happy':
                            shape = 'Stimuli/' + Label1 + '.bmp'
                        elif Target == 'Neutral':
                            shape = 'Stimuli/' + Label2 + '.bmp'
                        elif Target == 'Sad':
                            shape = 'Stimuli/' + Label3 + '.bmp'
                    
                    #Assigning correct responses
                    if CorrectAnswer == 'Yes':
                        if Yes == 'n':
                            corrAns = 'n'
                        elif Yes == 'm':
                            corrAns = 'm'
                    elif CorrectAnswer == 'No':
                        if No == 'm':
                            corrAns = 'm'
                        elif No == 'n':
                            corrAns = 'n'
                    
                    #Varying ITI Duration to be between 900 ms and 1300 ms (/1000 part is there to convert to seconds)
                    ITI_dur = random.randint(500,900)/1000
                    
                    #Varying target duration so that it's longer for valence trials (150 ms rather than 100)
                    if Task == 'Valence':
                        target_dur = 250/1000
                    else:
                        target_dur = 150/1000
                    practice_target_label.setText(label_text)
                    practice_target_shape.setImage(shape)
                    practice_resp.keys = []
                    practice_resp.rt = []
                    _practice_resp_allKeys = []
                    practice_target_label_valence.setOpacity(image_opacity)
                    practice_target_label_valence.setImage(label_image)
                    # keep track of which components have finished
                    practice_targetComponents = [practice_target_label, practice_target_plus, practice_target_shape, practice_resp, practice_target_label_valence]
                    for thisComponent in practice_targetComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "practice_target" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *practice_target_label* updates
                        
                        # if practice_target_label is starting this frame...
                        if practice_target_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            practice_target_label.frameNStart = frameN  # exact frame index
                            practice_target_label.tStart = t  # local t and not account for scr refresh
                            practice_target_label.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(practice_target_label, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'practice_target_label.started')
                            # update status
                            practice_target_label.status = STARTED
                            practice_target_label.setAutoDraw(True)
                        
                        # if practice_target_label is active this frame...
                        if practice_target_label.status == STARTED:
                            # update params
                            pass
                        
                        # if practice_target_label is stopping this frame...
                        if practice_target_label.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > practice_target_label.tStartRefresh + target_dur-frameTolerance:
                                # keep track of stop time/frame for later
                                practice_target_label.tStop = t  # not accounting for scr refresh
                                practice_target_label.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'practice_target_label.stopped')
                                # update status
                                practice_target_label.status = FINISHED
                                practice_target_label.setAutoDraw(False)
                        
                        # *practice_target_plus* updates
                        
                        # if practice_target_plus is starting this frame...
                        if practice_target_plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            practice_target_plus.frameNStart = frameN  # exact frame index
                            practice_target_plus.tStart = t  # local t and not account for scr refresh
                            practice_target_plus.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(practice_target_plus, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'practice_target_plus.started')
                            # update status
                            practice_target_plus.status = STARTED
                            practice_target_plus.setAutoDraw(True)
                        
                        # if practice_target_plus is active this frame...
                        if practice_target_plus.status == STARTED:
                            # update params
                            pass
                        
                        # if practice_target_plus is stopping this frame...
                        if practice_target_plus.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > practice_target_plus.tStartRefresh + target_dur-frameTolerance:
                                # keep track of stop time/frame for later
                                practice_target_plus.tStop = t  # not accounting for scr refresh
                                practice_target_plus.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'practice_target_plus.stopped')
                                # update status
                                practice_target_plus.status = FINISHED
                                practice_target_plus.setAutoDraw(False)
                        
                        # *practice_target_shape* updates
                        
                        # if practice_target_shape is starting this frame...
                        if practice_target_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            practice_target_shape.frameNStart = frameN  # exact frame index
                            practice_target_shape.tStart = t  # local t and not account for scr refresh
                            practice_target_shape.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(practice_target_shape, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'practice_target_shape.started')
                            # update status
                            practice_target_shape.status = STARTED
                            practice_target_shape.setAutoDraw(True)
                        
                        # if practice_target_shape is active this frame...
                        if practice_target_shape.status == STARTED:
                            # update params
                            pass
                        
                        # if practice_target_shape is stopping this frame...
                        if practice_target_shape.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > practice_target_shape.tStartRefresh + target_dur-frameTolerance:
                                # keep track of stop time/frame for later
                                practice_target_shape.tStop = t  # not accounting for scr refresh
                                practice_target_shape.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'practice_target_shape.stopped')
                                # update status
                                practice_target_shape.status = FINISHED
                                practice_target_shape.setAutoDraw(False)
                        
                        # *practice_resp* updates
                        waitOnFlip = False
                        
                        # if practice_resp is starting this frame...
                        if practice_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            practice_resp.frameNStart = frameN  # exact frame index
                            practice_resp.tStart = t  # local t and not account for scr refresh
                            practice_resp.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(practice_resp, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'practice_resp.started')
                            # update status
                            practice_resp.status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(practice_resp.clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(practice_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                        
                        # if practice_resp is stopping this frame...
                        if practice_resp.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > practice_resp.tStartRefresh + 1.5-frameTolerance:
                                # keep track of stop time/frame for later
                                practice_resp.tStop = t  # not accounting for scr refresh
                                practice_resp.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'practice_resp.stopped')
                                # update status
                                practice_resp.status = FINISHED
                                practice_resp.status = FINISHED
                        if practice_resp.status == STARTED and not waitOnFlip:
                            theseKeys = practice_resp.getKeys(keyList=['m','n'], ignoreKeys=["escape"], waitRelease=False)
                            _practice_resp_allKeys.extend(theseKeys)
                            if len(_practice_resp_allKeys):
                                practice_resp.keys = _practice_resp_allKeys[-1].name  # just the last key pressed
                                practice_resp.rt = _practice_resp_allKeys[-1].rt
                                practice_resp.duration = _practice_resp_allKeys[-1].duration
                                # was this correct?
                                if (practice_resp.keys == str(corrAns)) or (practice_resp.keys == corrAns):
                                    practice_resp.corr = 1
                                else:
                                    practice_resp.corr = 0
                                # a response ends the routine
                                continueRoutine = False
                        
                        # *practice_target_label_valence* updates
                        
                        # if practice_target_label_valence is starting this frame...
                        if practice_target_label_valence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            practice_target_label_valence.frameNStart = frameN  # exact frame index
                            practice_target_label_valence.tStart = t  # local t and not account for scr refresh
                            practice_target_label_valence.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(practice_target_label_valence, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'practice_target_label_valence.started')
                            # update status
                            practice_target_label_valence.status = STARTED
                            practice_target_label_valence.setAutoDraw(True)
                        
                        # if practice_target_label_valence is active this frame...
                        if practice_target_label_valence.status == STARTED:
                            # update params
                            pass
                        
                        # if practice_target_label_valence is stopping this frame...
                        if practice_target_label_valence.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > practice_target_label_valence.tStartRefresh + target_dur-frameTolerance:
                                # keep track of stop time/frame for later
                                practice_target_label_valence.tStop = t  # not accounting for scr refresh
                                practice_target_label_valence.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'practice_target_label_valence.stopped')
                                # update status
                                practice_target_label_valence.status = FINISHED
                                practice_target_label_valence.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in practice_targetComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "practice_target" ---
                    for thisComponent in practice_targetComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('practice_target.stopped', globalClock.getTime())
                    # check responses
                    if practice_resp.keys in ['', [], None]:  # No response was made
                        practice_resp.keys = None
                        # was no response the correct answer?!
                        if str(corrAns).lower() == 'none':
                           practice_resp.corr = 1;  # correct non-response
                        else:
                           practice_resp.corr = 0;  # failed to respond (incorrectly)
                    # store data for practice_trial (TrialHandler)
                    practice_trial.addData('practice_resp.keys',practice_resp.keys)
                    practice_trial.addData('practice_resp.corr', practice_resp.corr)
                    if practice_resp.keys != None:  # we had a response
                        practice_trial.addData('practice_resp.rt', practice_resp.rt)
                        practice_trial.addData('practice_resp.duration', practice_resp.duration)
                    # the Routine "practice_target" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    
                    # --- Prepare to start Routine "practice_ITI" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('practice_ITI.started', globalClock.getTime())
                    # keep track of which components have finished
                    practice_ITIComponents = [ITI_text]
                    for thisComponent in practice_ITIComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "practice_ITI" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *ITI_text* updates
                        
                        # if ITI_text is starting this frame...
                        if ITI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            ITI_text.frameNStart = frameN  # exact frame index
                            ITI_text.tStart = t  # local t and not account for scr refresh
                            ITI_text.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(ITI_text, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'ITI_text.started')
                            # update status
                            ITI_text.status = STARTED
                            ITI_text.setAutoDraw(True)
                        
                        # if ITI_text is active this frame...
                        if ITI_text.status == STARTED:
                            # update params
                            pass
                        
                        # if ITI_text is stopping this frame...
                        if ITI_text.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > ITI_text.tStartRefresh + ITI_dur-frameTolerance:
                                # keep track of stop time/frame for later
                                ITI_text.tStop = t  # not accounting for scr refresh
                                ITI_text.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'ITI_text.stopped')
                                # update status
                                ITI_text.status = FINISHED
                                ITI_text.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in practice_ITIComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "practice_ITI" ---
                    for thisComponent in practice_ITIComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('practice_ITI.stopped', globalClock.getTime())
                    # the Routine "practice_ITI" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    
                    # --- Prepare to start Routine "practice_feedback" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('practice_feedback.started', globalClock.getTime())
                    # Run 'Begin Routine' code from practice_feedback_code
                    #Feedback response
                    if not practice_resp.rt:
                        practice_feedback_msg = 'Too Slow!'
                        practice_feedback_colour = 'yellow'
                    elif practice_resp.corr:
                        practice_feedback_msg = 'Correct!'
                        practice_feedback_colour = 'green'
                    else:
                        practice_feedback_msg = 'Incorrect!'
                        practice_feedback_colour = 'red'
                    practice_feedback_text.setColor(practice_feedback_colour, colorSpace='rgb')
                    practice_feedback_text.setText(practice_feedback_msg)
                    # keep track of which components have finished
                    practice_feedbackComponents = [practice_feedback_text]
                    for thisComponent in practice_feedbackComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "practice_feedback" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 0.5:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *practice_feedback_text* updates
                        
                        # if practice_feedback_text is starting this frame...
                        if practice_feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            practice_feedback_text.frameNStart = frameN  # exact frame index
                            practice_feedback_text.tStart = t  # local t and not account for scr refresh
                            practice_feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(practice_feedback_text, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'practice_feedback_text.started')
                            # update status
                            practice_feedback_text.status = STARTED
                            practice_feedback_text.setAutoDraw(True)
                        
                        # if practice_feedback_text is active this frame...
                        if practice_feedback_text.status == STARTED:
                            # update params
                            pass
                        
                        # if practice_feedback_text is stopping this frame...
                        if practice_feedback_text.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > practice_feedback_text.tStartRefresh + 0.5-frameTolerance:
                                # keep track of stop time/frame for later
                                practice_feedback_text.tStop = t  # not accounting for scr refresh
                                practice_feedback_text.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'practice_feedback_text.stopped')
                                # update status
                                practice_feedback_text.status = FINISHED
                                practice_feedback_text.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in practice_feedbackComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "practice_feedback" ---
                    for thisComponent in practice_feedbackComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('practice_feedback.stopped', globalClock.getTime())
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-0.500000)
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed 2 repeats of 'practice_trial'
                
                # get names of stimulus parameters
                if practice_trial.trialList in ([], [None], None):
                    params = []
                else:
                    params = practice_trial.trialList[0].keys()
                # save data for this loop
                practice_trial.saveAsExcel(filename + '.xlsx', sheetName='practice_trial',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                practice_trial.saveAsText(filename + 'practice_trial.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                
                # --- Prepare to start Routine "practice_end" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('practice_end.started', globalClock.getTime())
                self_practice_end_resp.keys = []
                self_practice_end_resp.rt = []
                _self_practice_end_resp_allKeys = []
                # keep track of which components have finished
                practice_endComponents = [self_practice_end_text, self_practice_end_resp]
                for thisComponent in practice_endComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "practice_end" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *self_practice_end_text* updates
                    
                    # if self_practice_end_text is starting this frame...
                    if self_practice_end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        self_practice_end_text.frameNStart = frameN  # exact frame index
                        self_practice_end_text.tStart = t  # local t and not account for scr refresh
                        self_practice_end_text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(self_practice_end_text, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'self_practice_end_text.started')
                        # update status
                        self_practice_end_text.status = STARTED
                        self_practice_end_text.setAutoDraw(True)
                    
                    # if self_practice_end_text is active this frame...
                    if self_practice_end_text.status == STARTED:
                        # update params
                        pass
                    
                    # *self_practice_end_resp* updates
                    waitOnFlip = False
                    
                    # if self_practice_end_resp is starting this frame...
                    if self_practice_end_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        self_practice_end_resp.frameNStart = frameN  # exact frame index
                        self_practice_end_resp.tStart = t  # local t and not account for scr refresh
                        self_practice_end_resp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(self_practice_end_resp, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'self_practice_end_resp.started')
                        # update status
                        self_practice_end_resp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(self_practice_end_resp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(self_practice_end_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if self_practice_end_resp.status == STARTED and not waitOnFlip:
                        theseKeys = self_practice_end_resp.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                        _self_practice_end_resp_allKeys.extend(theseKeys)
                        if len(_self_practice_end_resp_allKeys):
                            self_practice_end_resp.keys = _self_practice_end_resp_allKeys[-1].name  # just the last key pressed
                            self_practice_end_resp.rt = _self_practice_end_resp_allKeys[-1].rt
                            self_practice_end_resp.duration = _self_practice_end_resp_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in practice_endComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "practice_end" ---
                for thisComponent in practice_endComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('practice_end.stopped', globalClock.getTime())
                # the Routine "practice_end" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                
                # set up handler to look after randomisation of conditions etc
                trials = data.TrialHandler(nReps=30, method='random', 
                    extraInfo=expInfo, originPath=-1,
                    trialList=data.importConditions(Task + 'TrialStim.xlsx'),
                    seed=None, name='trials')
                thisExp.addLoop(trials)  # add the loop to the experiment
                thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
                # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
                if thisTrial != None:
                    for paramName in thisTrial:
                        globals()[paramName] = thisTrial[paramName]
                
                for thisTrial in trials:
                    currentLoop = trials
                    thisExp.timestampOnFlip(win, 'thisRow.t')
                    # pause experiment here if requested
                    if thisExp.status == PAUSED:
                        pauseExperiment(
                            thisExp=thisExp, 
                            inputs=inputs, 
                            win=win, 
                            timers=[routineTimer], 
                            playbackComponents=[]
                    )
                    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
                    if thisTrial != None:
                        for paramName in thisTrial:
                            globals()[paramName] = thisTrial[paramName]
                    
                    # --- Prepare to start Routine "trial_fixation" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('trial_fixation.started', globalClock.getTime())
                    # Run 'Begin Routine' code from trial_fixation_code
                    if not trials.thisN in [0,60]:
                        continueRoutine=False
                    # keep track of which components have finished
                    trial_fixationComponents = [self_trial_fixation_cross]
                    for thisComponent in trial_fixationComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "trial_fixation" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 0.25:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *self_trial_fixation_cross* updates
                        
                        # if self_trial_fixation_cross is starting this frame...
                        if self_trial_fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            self_trial_fixation_cross.frameNStart = frameN  # exact frame index
                            self_trial_fixation_cross.tStart = t  # local t and not account for scr refresh
                            self_trial_fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(self_trial_fixation_cross, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'self_trial_fixation_cross.started')
                            # update status
                            self_trial_fixation_cross.status = STARTED
                            self_trial_fixation_cross.setAutoDraw(True)
                        
                        # if self_trial_fixation_cross is active this frame...
                        if self_trial_fixation_cross.status == STARTED:
                            # update params
                            pass
                        
                        # if self_trial_fixation_cross is stopping this frame...
                        if self_trial_fixation_cross.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > self_trial_fixation_cross.tStartRefresh + 0.25-frameTolerance:
                                # keep track of stop time/frame for later
                                self_trial_fixation_cross.tStop = t  # not accounting for scr refresh
                                self_trial_fixation_cross.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'self_trial_fixation_cross.stopped')
                                # update status
                                self_trial_fixation_cross.status = FINISHED
                                self_trial_fixation_cross.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in trial_fixationComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "trial_fixation" ---
                    for thisComponent in trial_fixationComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('trial_fixation.stopped', globalClock.getTime())
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-0.250000)
                    
                    # --- Prepare to start Routine "trial_target" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('trial_target.started', globalClock.getTime())
                    # Run 'Begin Routine' code from trial_code
                    #Assigning correct labels (valence isn't included as text because this is an image)
                    if Task == 'Valence':
                        label_text = ''
                    else:
                        label_text = Label
                    
                    #Using image for valence labels
                    if Task == 'Valence':
                        label_image = 'Stimuli/' + Label + '.bmp'
                    else:
                        label_image = 'Stimuli/Empty.bmp'
                    
                    #Setting opacity of image to be 0 if task isn't valence
                    if Task == 'Valence':
                        image_opacity = 1
                    else:
                        image_opacity = 0
                    
                    #Assigning correct shapes
                    if Task == 'Control':
                        if Target == 'sky':
                            shape = 'Stimuli/' + Label1 + '.bmp'
                        elif Target == 'earth':
                            shape = 'Stimuli/' + Label2 + '.bmp'
                        elif Target == 'air':
                            shape = 'Stimuli/' + Label3 + '.bmp'
                    elif Task == 'Reward':
                        if Target == 'HighReward':
                            shape = 'Stimuli/' + Label1 + '.bmp'
                        elif Target == 'MediumReward':
                            shape = 'Stimuli/' + Label2 + '.bmp'
                        elif Target == 'LowReward':
                            shape = 'Stimuli/' + Label3 + '.bmp'
                    elif Task == 'Valence':
                        if Target == 'Happy':
                            shape = 'Stimuli/' + Label1 + '.bmp'
                        elif Target == 'Neutral':
                            shape = 'Stimuli/' + Label2 + '.bmp'
                        elif Target == 'Sad':
                            shape = 'Stimuli/' + Label3 + '.bmp'
                    
                    #Assigning correct responses
                    if CorrectAnswer == 'Yes':
                        if Yes == 'n':
                            corrAns = 'n'
                        elif Yes == 'm':
                            corrAns = 'm'
                    elif CorrectAnswer == 'No':
                        if No == 'm':
                            corrAns = 'm'
                        elif No == 'n':
                            corrAns = 'n'
                    
                    #Varying ITI Duration to be between 900 ms and 1300 ms (/1000 part is there to convert to seconds)
                    ITI_dur = random.randint(500,900)/1000
                    
                    #Varying target duration so that it's longer for valence trials (150 ms rather than 100)
                    if Task == 'Valence':
                        target_dur = 250/1000
                    else:
                        target_dur = 150/1000
                    trial_target_label.setText(label_text)
                    trial_target_shape.setImage(shape)
                    trial_resp.keys = []
                    trial_resp.rt = []
                    _trial_resp_allKeys = []
                    trial_target_label_valence.setOpacity(image_opacity)
                    trial_target_label_valence.setImage(label_image)
                    # keep track of which components have finished
                    trial_targetComponents = [trial_target_label, trial_target_plus, trial_target_shape, trial_resp, trial_target_label_valence]
                    for thisComponent in trial_targetComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "trial_target" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *trial_target_label* updates
                        
                        # if trial_target_label is starting this frame...
                        if trial_target_label.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            trial_target_label.frameNStart = frameN  # exact frame index
                            trial_target_label.tStart = t  # local t and not account for scr refresh
                            trial_target_label.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(trial_target_label, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'trial_target_label.started')
                            # update status
                            trial_target_label.status = STARTED
                            trial_target_label.setAutoDraw(True)
                        
                        # if trial_target_label is active this frame...
                        if trial_target_label.status == STARTED:
                            # update params
                            pass
                        
                        # if trial_target_label is stopping this frame...
                        if trial_target_label.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > trial_target_label.tStartRefresh + target_dur-frameTolerance:
                                # keep track of stop time/frame for later
                                trial_target_label.tStop = t  # not accounting for scr refresh
                                trial_target_label.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'trial_target_label.stopped')
                                # update status
                                trial_target_label.status = FINISHED
                                trial_target_label.setAutoDraw(False)
                        
                        # *trial_target_plus* updates
                        
                        # if trial_target_plus is starting this frame...
                        if trial_target_plus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            trial_target_plus.frameNStart = frameN  # exact frame index
                            trial_target_plus.tStart = t  # local t and not account for scr refresh
                            trial_target_plus.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(trial_target_plus, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'trial_target_plus.started')
                            # update status
                            trial_target_plus.status = STARTED
                            trial_target_plus.setAutoDraw(True)
                        
                        # if trial_target_plus is active this frame...
                        if trial_target_plus.status == STARTED:
                            # update params
                            pass
                        
                        # if trial_target_plus is stopping this frame...
                        if trial_target_plus.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > trial_target_plus.tStartRefresh + target_dur-frameTolerance:
                                # keep track of stop time/frame for later
                                trial_target_plus.tStop = t  # not accounting for scr refresh
                                trial_target_plus.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'trial_target_plus.stopped')
                                # update status
                                trial_target_plus.status = FINISHED
                                trial_target_plus.setAutoDraw(False)
                        
                        # *trial_target_shape* updates
                        
                        # if trial_target_shape is starting this frame...
                        if trial_target_shape.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            trial_target_shape.frameNStart = frameN  # exact frame index
                            trial_target_shape.tStart = t  # local t and not account for scr refresh
                            trial_target_shape.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(trial_target_shape, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'trial_target_shape.started')
                            # update status
                            trial_target_shape.status = STARTED
                            trial_target_shape.setAutoDraw(True)
                        
                        # if trial_target_shape is active this frame...
                        if trial_target_shape.status == STARTED:
                            # update params
                            pass
                        
                        # if trial_target_shape is stopping this frame...
                        if trial_target_shape.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > trial_target_shape.tStartRefresh + target_dur-frameTolerance:
                                # keep track of stop time/frame for later
                                trial_target_shape.tStop = t  # not accounting for scr refresh
                                trial_target_shape.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'trial_target_shape.stopped')
                                # update status
                                trial_target_shape.status = FINISHED
                                trial_target_shape.setAutoDraw(False)
                        
                        # *trial_resp* updates
                        waitOnFlip = False
                        
                        # if trial_resp is starting this frame...
                        if trial_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            trial_resp.frameNStart = frameN  # exact frame index
                            trial_resp.tStart = t  # local t and not account for scr refresh
                            trial_resp.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(trial_resp, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'trial_resp.started')
                            # update status
                            trial_resp.status = STARTED
                            # keyboard checking is just starting
                            waitOnFlip = True
                            win.callOnFlip(trial_resp.clock.reset)  # t=0 on next screen flip
                            win.callOnFlip(trial_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                        
                        # if trial_resp is stopping this frame...
                        if trial_resp.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > trial_resp.tStartRefresh + 1.5-frameTolerance:
                                # keep track of stop time/frame for later
                                trial_resp.tStop = t  # not accounting for scr refresh
                                trial_resp.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'trial_resp.stopped')
                                # update status
                                trial_resp.status = FINISHED
                                trial_resp.status = FINISHED
                        if trial_resp.status == STARTED and not waitOnFlip:
                            theseKeys = trial_resp.getKeys(keyList=['m','n'], ignoreKeys=["escape"], waitRelease=False)
                            _trial_resp_allKeys.extend(theseKeys)
                            if len(_trial_resp_allKeys):
                                trial_resp.keys = _trial_resp_allKeys[-1].name  # just the last key pressed
                                trial_resp.rt = _trial_resp_allKeys[-1].rt
                                trial_resp.duration = _trial_resp_allKeys[-1].duration
                                # was this correct?
                                if (trial_resp.keys == str(corrAns)) or (trial_resp.keys == corrAns):
                                    trial_resp.corr = 1
                                else:
                                    trial_resp.corr = 0
                                # a response ends the routine
                                continueRoutine = False
                        
                        # *trial_target_label_valence* updates
                        
                        # if trial_target_label_valence is starting this frame...
                        if trial_target_label_valence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            trial_target_label_valence.frameNStart = frameN  # exact frame index
                            trial_target_label_valence.tStart = t  # local t and not account for scr refresh
                            trial_target_label_valence.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(trial_target_label_valence, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'trial_target_label_valence.started')
                            # update status
                            trial_target_label_valence.status = STARTED
                            trial_target_label_valence.setAutoDraw(True)
                        
                        # if trial_target_label_valence is active this frame...
                        if trial_target_label_valence.status == STARTED:
                            # update params
                            pass
                        
                        # if trial_target_label_valence is stopping this frame...
                        if trial_target_label_valence.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > trial_target_label_valence.tStartRefresh + target_dur-frameTolerance:
                                # keep track of stop time/frame for later
                                trial_target_label_valence.tStop = t  # not accounting for scr refresh
                                trial_target_label_valence.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'trial_target_label_valence.stopped')
                                # update status
                                trial_target_label_valence.status = FINISHED
                                trial_target_label_valence.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in trial_targetComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "trial_target" ---
                    for thisComponent in trial_targetComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('trial_target.stopped', globalClock.getTime())
                    # check responses
                    if trial_resp.keys in ['', [], None]:  # No response was made
                        trial_resp.keys = None
                        # was no response the correct answer?!
                        if str(corrAns).lower() == 'none':
                           trial_resp.corr = 1;  # correct non-response
                        else:
                           trial_resp.corr = 0;  # failed to respond (incorrectly)
                    # store data for trials (TrialHandler)
                    trials.addData('trial_resp.keys',trial_resp.keys)
                    trials.addData('trial_resp.corr', trial_resp.corr)
                    if trial_resp.keys != None:  # we had a response
                        trials.addData('trial_resp.rt', trial_resp.rt)
                        trials.addData('trial_resp.duration', trial_resp.duration)
                    # the Routine "trial_target" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    
                    # --- Prepare to start Routine "trial_ITI" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('trial_ITI.started', globalClock.getTime())
                    # keep track of which components have finished
                    trial_ITIComponents = [self_trial_ITI_text]
                    for thisComponent in trial_ITIComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "trial_ITI" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *self_trial_ITI_text* updates
                        
                        # if self_trial_ITI_text is starting this frame...
                        if self_trial_ITI_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            self_trial_ITI_text.frameNStart = frameN  # exact frame index
                            self_trial_ITI_text.tStart = t  # local t and not account for scr refresh
                            self_trial_ITI_text.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(self_trial_ITI_text, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'self_trial_ITI_text.started')
                            # update status
                            self_trial_ITI_text.status = STARTED
                            self_trial_ITI_text.setAutoDraw(True)
                        
                        # if self_trial_ITI_text is active this frame...
                        if self_trial_ITI_text.status == STARTED:
                            # update params
                            pass
                        
                        # if self_trial_ITI_text is stopping this frame...
                        if self_trial_ITI_text.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > self_trial_ITI_text.tStartRefresh + ITI_dur-frameTolerance:
                                # keep track of stop time/frame for later
                                self_trial_ITI_text.tStop = t  # not accounting for scr refresh
                                self_trial_ITI_text.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'self_trial_ITI_text.stopped')
                                # update status
                                self_trial_ITI_text.status = FINISHED
                                self_trial_ITI_text.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in trial_ITIComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "trial_ITI" ---
                    for thisComponent in trial_ITIComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('trial_ITI.stopped', globalClock.getTime())
                    # Run 'End Routine' code from ITI_code
                    #Adding ITI duration to data file
                    trials.addData('ITI_duration', ITI_dur)
                    # the Routine "trial_ITI" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    
                    # --- Prepare to start Routine "trial_feedback" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('trial_feedback.started', globalClock.getTime())
                    # Run 'Begin Routine' code from trial_feedback_code
                    #Feedback response
                    if not trial_resp.rt:
                        trial_feedback_msg = 'Too Slow!'
                        trial_feedback_colour = 'yellow'
                    elif trial_resp.corr:
                        trial_feedback_msg = 'Correct!'
                        trial_feedback_colour = 'green'
                    else:
                        trial_feedback_msg = 'Incorrect!'
                        trial_feedback_colour = 'red'
                    
                    
                    self_trial_feedback_text.setColor(trial_feedback_colour, colorSpace='rgb')
                    self_trial_feedback_text.setText(trial_feedback_msg)
                    # keep track of which components have finished
                    trial_feedbackComponents = [self_trial_feedback_text]
                    for thisComponent in trial_feedbackComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "trial_feedback" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine and routineTimer.getTime() < 0.25:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *self_trial_feedback_text* updates
                        
                        # if self_trial_feedback_text is starting this frame...
                        if self_trial_feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            self_trial_feedback_text.frameNStart = frameN  # exact frame index
                            self_trial_feedback_text.tStart = t  # local t and not account for scr refresh
                            self_trial_feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(self_trial_feedback_text, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'self_trial_feedback_text.started')
                            # update status
                            self_trial_feedback_text.status = STARTED
                            self_trial_feedback_text.setAutoDraw(True)
                        
                        # if self_trial_feedback_text is active this frame...
                        if self_trial_feedback_text.status == STARTED:
                            # update params
                            pass
                        
                        # if self_trial_feedback_text is stopping this frame...
                        if self_trial_feedback_text.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > self_trial_feedback_text.tStartRefresh + 0.25-frameTolerance:
                                # keep track of stop time/frame for later
                                self_trial_feedback_text.tStop = t  # not accounting for scr refresh
                                self_trial_feedback_text.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'self_trial_feedback_text.stopped')
                                # update status
                                self_trial_feedback_text.status = FINISHED
                                self_trial_feedback_text.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in trial_feedbackComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "trial_feedback" ---
                    for thisComponent in trial_feedbackComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('trial_feedback.stopped', globalClock.getTime())
                    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
                    if routineForceEnded:
                        routineTimer.reset()
                    else:
                        routineTimer.addTime(-0.250000)
                    
                    # --- Prepare to start Routine "trial_break" ---
                    continueRoutine = True
                    # update component parameters for each repeat
                    thisExp.addData('trial_break.started', globalClock.getTime())
                    # Run 'Begin Routine' code from trial_break_code
                    if not trials.thisN in [72,144,216,288,360]:
                        continueRoutine=False
                    
                    trial_accuracy = int((trials.data['trial_resp.corr'].mean())*100)
                    trial_break_text.setText('')
                    # keep track of which components have finished
                    trial_breakComponents = [trial_break_text, image]
                    for thisComponent in trial_breakComponents:
                        thisComponent.tStart = None
                        thisComponent.tStop = None
                        thisComponent.tStartRefresh = None
                        thisComponent.tStopRefresh = None
                        if hasattr(thisComponent, 'status'):
                            thisComponent.status = NOT_STARTED
                    # reset timers
                    t = 0
                    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                    frameN = -1
                    
                    # --- Run Routine "trial_break" ---
                    routineForceEnded = not continueRoutine
                    while continueRoutine:
                        # get current time
                        t = routineTimer.getTime()
                        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                        # update/draw components on each frame
                        
                        # *trial_break_text* updates
                        
                        # if trial_break_text is starting this frame...
                        if trial_break_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            trial_break_text.frameNStart = frameN  # exact frame index
                            trial_break_text.tStart = t  # local t and not account for scr refresh
                            trial_break_text.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(trial_break_text, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'trial_break_text.started')
                            # update status
                            trial_break_text.status = STARTED
                            trial_break_text.setAutoDraw(True)
                        
                        # if trial_break_text is active this frame...
                        if trial_break_text.status == STARTED:
                            # update params
                            pass
                        
                        # if trial_break_text is stopping this frame...
                        if trial_break_text.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > trial_break_text.tStartRefresh + 0-frameTolerance:
                                # keep track of stop time/frame for later
                                trial_break_text.tStop = t  # not accounting for scr refresh
                                trial_break_text.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'trial_break_text.stopped')
                                # update status
                                trial_break_text.status = FINISHED
                                trial_break_text.setAutoDraw(False)
                        
                        # *image* updates
                        
                        # if image is starting this frame...
                        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                            # keep track of start time/frame for later
                            image.frameNStart = frameN  # exact frame index
                            image.tStart = t  # local t and not account for scr refresh
                            image.tStartRefresh = tThisFlipGlobal  # on global time
                            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                            # add timestamp to datafile
                            thisExp.timestampOnFlip(win, 'image.started')
                            # update status
                            image.status = STARTED
                            image.setAutoDraw(True)
                        
                        # if image is active this frame...
                        if image.status == STARTED:
                            # update params
                            pass
                        
                        # if image is stopping this frame...
                        if image.status == STARTED:
                            # is it time to stop? (based on global clock, using actual start)
                            if tThisFlipGlobal > image.tStartRefresh + 0-frameTolerance:
                                # keep track of stop time/frame for later
                                image.tStop = t  # not accounting for scr refresh
                                image.frameNStop = frameN  # exact frame index
                                # add timestamp to datafile
                                thisExp.timestampOnFlip(win, 'image.stopped')
                                # update status
                                image.status = FINISHED
                                image.setAutoDraw(False)
                        
                        # check for quit (typically the Esc key)
                        if defaultKeyboard.getKeys(keyList=["escape"]):
                            thisExp.status = FINISHED
                        if thisExp.status == FINISHED or endExpNow:
                            endExperiment(thisExp, inputs=inputs, win=win)
                            return
                        
                        # check if all components have finished
                        if not continueRoutine:  # a component has requested a forced-end of Routine
                            routineForceEnded = True
                            break
                        continueRoutine = False  # will revert to True if at least one component still running
                        for thisComponent in trial_breakComponents:
                            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                                continueRoutine = True
                                break  # at least one component has not yet finished
                        
                        # refresh the screen
                        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                            win.flip()
                    
                    # --- Ending Routine "trial_break" ---
                    for thisComponent in trial_breakComponents:
                        if hasattr(thisComponent, "setAutoDraw"):
                            thisComponent.setAutoDraw(False)
                    thisExp.addData('trial_break.stopped', globalClock.getTime())
                    # the Routine "trial_break" was not non-slip safe, so reset the non-slip timer
                    routineTimer.reset()
                    thisExp.nextEntry()
                    
                    if thisSession is not None:
                        # if running in a Session with a Liaison client, send data up to now
                        thisSession.sendExperimentData()
                # completed 30 repeats of 'trials'
                
                # get names of stimulus parameters
                if trials.trialList in ([], [None], None):
                    params = []
                else:
                    params = trials.trialList[0].keys()
                # save data for this loop
                trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                trials.saveAsText(filename + 'trials.csv', delim=',',
                    stimOut=params,
                    dataOut=['n','all_mean','all_std', 'all_raw'])
                
                # --- Prepare to start Routine "trials_end" ---
                continueRoutine = True
                # update component parameters for each repeat
                thisExp.addData('trials_end.started', globalClock.getTime())
                trials_end_resp.keys = []
                trials_end_resp.rt = []
                _trials_end_resp_allKeys = []
                # keep track of which components have finished
                trials_endComponents = [trials_end_text, trials_end_resp]
                for thisComponent in trials_endComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                # reset timers
                t = 0
                _timeToFirstFrame = win.getFutureFlipTime(clock="now")
                frameN = -1
                
                # --- Run Routine "trials_end" ---
                routineForceEnded = not continueRoutine
                while continueRoutine:
                    # get current time
                    t = routineTimer.getTime()
                    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *trials_end_text* updates
                    
                    # if trials_end_text is starting this frame...
                    if trials_end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        trials_end_text.frameNStart = frameN  # exact frame index
                        trials_end_text.tStart = t  # local t and not account for scr refresh
                        trials_end_text.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(trials_end_text, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'trials_end_text.started')
                        # update status
                        trials_end_text.status = STARTED
                        trials_end_text.setAutoDraw(True)
                    
                    # if trials_end_text is active this frame...
                    if trials_end_text.status == STARTED:
                        # update params
                        pass
                    
                    # *trials_end_resp* updates
                    waitOnFlip = False
                    
                    # if trials_end_resp is starting this frame...
                    if trials_end_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                        # keep track of start time/frame for later
                        trials_end_resp.frameNStart = frameN  # exact frame index
                        trials_end_resp.tStart = t  # local t and not account for scr refresh
                        trials_end_resp.tStartRefresh = tThisFlipGlobal  # on global time
                        win.timeOnFlip(trials_end_resp, 'tStartRefresh')  # time at next scr refresh
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'trials_end_resp.started')
                        # update status
                        trials_end_resp.status = STARTED
                        # keyboard checking is just starting
                        waitOnFlip = True
                        win.callOnFlip(trials_end_resp.clock.reset)  # t=0 on next screen flip
                        win.callOnFlip(trials_end_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    if trials_end_resp.status == STARTED and not waitOnFlip:
                        theseKeys = trials_end_resp.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                        _trials_end_resp_allKeys.extend(theseKeys)
                        if len(_trials_end_resp_allKeys):
                            trials_end_resp.keys = _trials_end_resp_allKeys[-1].name  # just the last key pressed
                            trials_end_resp.rt = _trials_end_resp_allKeys[-1].rt
                            trials_end_resp.duration = _trials_end_resp_allKeys[-1].duration
                            # a response ends the routine
                            continueRoutine = False
                    
                    # check for quit (typically the Esc key)
                    if defaultKeyboard.getKeys(keyList=["escape"]):
                        thisExp.status = FINISHED
                    if thisExp.status == FINISHED or endExpNow:
                        endExperiment(thisExp, inputs=inputs, win=win)
                        return
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        routineForceEnded = True
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in trials_endComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # --- Ending Routine "trials_end" ---
                for thisComponent in trials_endComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                thisExp.addData('trials_end.stopped', globalClock.getTime())
                # check responses
                if trials_end_resp.keys in ['', [], None]:  # No response was made
                    trials_end_resp.keys = None
                task_block.addData('trials_end_resp.keys',trials_end_resp.keys)
                if trials_end_resp.keys != None:  # we had a response
                    task_block.addData('trials_end_resp.rt', trials_end_resp.rt)
                    task_block.addData('trials_end_resp.duration', trials_end_resp.duration)
                # the Routine "trials_end" was not non-slip safe, so reset the non-slip timer
                routineTimer.reset()
                thisExp.nextEntry()
                
                if thisSession is not None:
                    # if running in a Session with a Liaison client, send data up to now
                    thisSession.sendExperimentData()
            # completed 1 repeats of 'task_block'
            
            # get names of stimulus parameters
            if task_block.trialList in ([], [None], None):
                params = []
            else:
                params = task_block.trialList[0].keys()
            # save data for this loop
            task_block.saveAsExcel(filename + '.xlsx', sheetName='task_block',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            task_block.saveAsText(filename + 'task_block.csv', delim=',',
                stimOut=params,
                dataOut=['n','all_mean','all_std', 'all_raw'])
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1 repeats of 'task_order'
        
        # get names of stimulus parameters
        if task_order.trialList in ([], [None], None):
            params = []
        else:
            params = task_order.trialList[0].keys()
        # save data for this loop
        task_order.saveAsExcel(filename + '.xlsx', sheetName='task_order',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        task_order.saveAsText(filename + 'task_order.csv', delim=',',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
        
        # --- Prepare to start Routine "end" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('end.started', globalClock.getTime())
        # keep track of which components have finished
        endComponents = [text]
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
        frameN = -1
        
        # --- Run Routine "end" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 2-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, inputs=inputs, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in endComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "end" ---
        for thisComponent in endComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('end.stopped', globalClock.getTime())
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1 repeats of 'key_commands'
    
    # get names of stimulus parameters
    if key_commands.trialList in ([], [None], None):
        params = []
    else:
        params = key_commands.trialList[0].keys()
    # save data for this loop
    key_commands.saveAsExcel(filename + '.xlsx', sheetName='key_commands',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    key_commands.saveAsText(filename + 'key_commands.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
