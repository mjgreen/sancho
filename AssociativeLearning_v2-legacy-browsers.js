/******************************* 
 * Associativelearning_V2 *
 *******************************/


// store info about the experiment session:
let expName = 'AssociativeLearning_v2';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'group': '',
    'session': '01',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const key_commandsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(key_commandsLoopBegin(key_commandsLoopScheduler));
flowScheduler.add(key_commandsLoopScheduler);
flowScheduler.add(key_commandsLoopEnd);























flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'KeyboardCommand.xlsx', 'path': 'KeyboardCommand.xlsx'},
    {'name': 'ControlTask.xlsx', 'path': 'ControlTask.xlsx'},
    {'name': 'ControlTrialStim.xlsx', 'path': 'ControlTrialStim.xlsx'},
    {'name': 'GroupA.xlsx', 'path': 'GroupA.xlsx'},
    {'name': 'GroupB.xlsx', 'path': 'GroupB.xlsx'},
    {'name': 'GroupC.xlsx', 'path': 'GroupC.xlsx'},
    {'name': 'GroupD.xlsx', 'path': 'GroupD.xlsx'},
    {'name': 'GroupE.xlsx', 'path': 'GroupE.xlsx'},
    {'name': 'GroupF.xlsx', 'path': 'GroupF.xlsx'},
    {'name': 'KeyboardCommand.xlsx', 'path': 'KeyboardCommand.xlsx'},
    {'name': 'RewardTask.xlsx', 'path': 'RewardTask.xlsx'},
    {'name': 'RewardTrialStim.xlsx', 'path': 'RewardTrialStim.xlsx'},
    {'name': 'TaskOrder.xlsx', 'path': 'TaskOrder.xlsx'},
    {'name': 'ValenceTask.xlsx', 'path': 'ValenceTask.xlsx'},
    {'name': 'ValenceTrialStim.xlsx', 'path': 'ValenceTrialStim.xlsx'},
    {'name': 'ControlTask.xlsx', 'path': 'ControlTask.xlsx'},
    {'name': 'ControlTrialStim.xlsx', 'path': 'ControlTrialStim.xlsx'},
    {'name': 'GroupA.xlsx', 'path': 'GroupA.xlsx'},
    {'name': 'GroupB.xlsx', 'path': 'GroupB.xlsx'},
    {'name': 'GroupC.xlsx', 'path': 'GroupC.xlsx'},
    {'name': 'GroupD.xlsx', 'path': 'GroupD.xlsx'},
    {'name': 'GroupE.xlsx', 'path': 'GroupE.xlsx'},
    {'name': 'GroupF.xlsx', 'path': 'GroupF.xlsx'},
    {'name': 'KeyboardCommand.xlsx', 'path': 'KeyboardCommand.xlsx'},
    {'name': 'RewardTask.xlsx', 'path': 'RewardTask.xlsx'},
    {'name': 'RewardTrialStim.xlsx', 'path': 'RewardTrialStim.xlsx'},
    {'name': 'TaskOrder.xlsx', 'path': 'TaskOrder.xlsx'},
    {'name': 'ValenceTask.xlsx', 'path': 'ValenceTask.xlsx'},
    {'name': 'ValenceTrialStim.xlsx', 'path': 'ValenceTrialStim.xlsx'},
    {'name': 'ControlTask.xlsx', 'path': 'ControlTask.xlsx'},
    {'name': 'ControlTrialStim.xlsx', 'path': 'ControlTrialStim.xlsx'},
    {'name': 'GroupA.xlsx', 'path': 'GroupA.xlsx'},
    {'name': 'GroupB.xlsx', 'path': 'GroupB.xlsx'},
    {'name': 'GroupC.xlsx', 'path': 'GroupC.xlsx'},
    {'name': 'GroupD.xlsx', 'path': 'GroupD.xlsx'},
    {'name': 'GroupE.xlsx', 'path': 'GroupE.xlsx'},
    {'name': 'GroupF.xlsx', 'path': 'GroupF.xlsx'},
    {'name': 'KeyboardCommand.xlsx', 'path': 'KeyboardCommand.xlsx'},
    {'name': 'RewardTask.xlsx', 'path': 'RewardTask.xlsx'},
    {'name': 'RewardTrialStim.xlsx', 'path': 'RewardTrialStim.xlsx'},
    {'name': 'TaskOrder.xlsx', 'path': 'TaskOrder.xlsx'},
    {'name': 'ValenceTask.xlsx', 'path': 'ValenceTask.xlsx'},
    {'name': 'ValenceTrialStim.xlsx', 'path': 'ValenceTrialStim.xlsx'},
    {'name': 'ControlTask.xlsx', 'path': 'ControlTask.xlsx'},
    {'name': 'ControlTrialStim.xlsx', 'path': 'ControlTrialStim.xlsx'},
    {'name': 'GroupA.xlsx', 'path': 'GroupA.xlsx'},
    {'name': 'GroupB.xlsx', 'path': 'GroupB.xlsx'},
    {'name': 'GroupC.xlsx', 'path': 'GroupC.xlsx'},
    {'name': 'GroupD.xlsx', 'path': 'GroupD.xlsx'},
    {'name': 'GroupE.xlsx', 'path': 'GroupE.xlsx'},
    {'name': 'GroupF.xlsx', 'path': 'GroupF.xlsx'},
    {'name': 'KeyboardCommand.xlsx', 'path': 'KeyboardCommand.xlsx'},
    {'name': 'RewardTask.xlsx', 'path': 'RewardTask.xlsx'},
    {'name': 'RewardTrialStim.xlsx', 'path': 'RewardTrialStim.xlsx'},
    {'name': 'TaskOrder.xlsx', 'path': 'TaskOrder.xlsx'},
    {'name': 'ValenceTask.xlsx', 'path': 'ValenceTask.xlsx'},
    {'name': 'ValenceTrialStim.xlsx', 'path': 'ValenceTrialStim.xlsx'},
    {'name': 'default.png', 'path': 'https://pavlovia.org/assets/default/default.png'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2023.2.2';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}


var introClock;
var intro_text;
var intro_resp;
var instructionsClock;
var instructions_text;
var instructions_resp;
var practice_fixationClock;
var practice_fixation_cross;
var practice_targetClock;
var practice_target_label;
var practice_target_plus;
var practice_target_shape;
var practice_resp;
var practice_target_label_valence;
var practice_ITIClock;
var ITI_text;
var practice_feedbackClock;
var practice_feedback_text;
var practice_endClock;
var self_practice_end_text;
var self_practice_end_resp;
var trial_fixationClock;
var self_trial_fixation_cross;
var trial_targetClock;
var trial_target_label;
var trial_target_plus;
var trial_target_shape;
var trial_resp;
var trial_target_label_valence;
var trial_ITIClock;
var self_trial_ITI_text;
var trial_feedbackClock;
var self_trial_feedback_text;
var trial_breakClock;
var trial_break_text;
var image;
var trials_endClock;
var trials_end_text;
var trials_end_resp;
var endClock;
var text;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "intro"
  introClock = new util.Clock();
  intro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'intro_text',
    text: 'Welcome!\n\nIn this task you will be presented with some shapes and labels, and asked to remember them.\n\nYou will complete three different versions of this task.\n\nIn one version you will be shown different words relating to different directions. In another version you will be shown different amounts of money, and in another version you will be shown different facial expressions.\n\nPress space to start.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.2, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  intro_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  instructions_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: 1.3, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  instructions_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_fixation"
  practice_fixationClock = new util.Clock();
  practice_fixation_cross = new visual.ShapeStim ({
    win: psychoJS.window, name: 'practice_fixation_cross', 
    vertices: 'cross', size:[0.06, 0.1],
    ori: 0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([255, 0, 0]),
    fillColor: new util.Color([255, 0, 0]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "practice_target"
  practice_targetClock = new util.Clock();
  practice_target_label = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_target_label',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  practice_target_plus = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_target_plus',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  practice_target_shape = new visual.ImageStim({
    win : psychoJS.window,
    name : 'practice_target_shape', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0.3], size : [0.18, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  practice_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  practice_target_label_valence = new visual.ImageStim({
    win : psychoJS.window,
    name : 'practice_target_label_valence', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, (- 0.3)], size : [0.2, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "practice_ITI"
  practice_ITIClock = new util.Clock();
  ITI_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'ITI_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "practice_feedback"
  practice_feedbackClock = new util.Clock();
  practice_feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'practice_feedback_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "practice_end"
  practice_endClock = new util.Clock();
  self_practice_end_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'self_practice_end_text',
    text: "End of practice.\n\nPlease press 'SPACEBAR' to start the real experiment.\n\nPLEASE RESPOND AS QUICKLY AND ACCURATELY AS POSSIBLE.",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  self_practice_end_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "trial_fixation"
  trial_fixationClock = new util.Clock();
  self_trial_fixation_cross = new visual.ShapeStim ({
    win: psychoJS.window, name: 'self_trial_fixation_cross', 
    vertices: 'cross', size:[0.06, 0.1],
    ori: 0, pos: [0, 0],
    anchor: 'center',
    lineWidth: 1, 
    colorSpace: 'rgb',
    lineColor: new util.Color([255, 0, 0]),
    fillColor: new util.Color([255, 0, 0]),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  // Initialize components for Routine "trial_target"
  trial_targetClock = new util.Clock();
  trial_target_label = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial_target_label',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  trial_target_plus = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial_target_plus',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  trial_target_shape = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial_target_shape', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, 0.3], size : [0.18, 0.3],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -3.0 
  });
  trial_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  trial_target_label_valence = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trial_target_label_valence', units : undefined, 
    image : 'default.png', mask : undefined,
    anchor : 'center',
    ori : 0, pos : [0, (- 0.3)], size : [0.2, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1.0,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -5.0 
  });
  // Initialize components for Routine "trial_ITI"
  trial_ITIClock = new util.Clock();
  self_trial_ITI_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'self_trial_ITI_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "trial_feedback"
  trial_feedbackClock = new util.Clock();
  self_trial_feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'self_trial_feedback_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "trial_break"
  trial_breakClock = new util.Clock();
  trial_break_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial_break_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
    image : undefined, mask : undefined,
    anchor : 'center',
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "trials_end"
  trials_endClock = new util.Clock();
  trials_end_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'trials_end_text',
    text: 'Well done! You have completed these trials.\n\nPress the spacebar to continue.',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  trials_end_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "end"
  endClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Well done! You have finished the task!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var key_commands;
function key_commandsLoopBegin(key_commandsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    key_commands = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'KeyboardCommand.xlsx', 'np.random.choice(2, size=1, replace=False)'),
      seed: undefined, name: 'key_commands'
    });
    psychoJS.experiment.addLoop(key_commands); // add the loop to the experiment
    currentLoop = key_commands;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    key_commands.forEach(function() {
      snapshot = key_commands.getSnapshot();
    
      key_commandsLoopScheduler.add(importConditions(snapshot));
      key_commandsLoopScheduler.add(introRoutineBegin(snapshot));
      key_commandsLoopScheduler.add(introRoutineEachFrame());
      key_commandsLoopScheduler.add(introRoutineEnd(snapshot));
      const task_orderLoopScheduler = new Scheduler(psychoJS);
      key_commandsLoopScheduler.add(task_orderLoopBegin(task_orderLoopScheduler, snapshot));
      key_commandsLoopScheduler.add(task_orderLoopScheduler);
      key_commandsLoopScheduler.add(task_orderLoopEnd);
      key_commandsLoopScheduler.add(endRoutineBegin(snapshot));
      key_commandsLoopScheduler.add(endRoutineEachFrame());
      key_commandsLoopScheduler.add(endRoutineEnd(snapshot));
      key_commandsLoopScheduler.add(key_commandsLoopEndIteration(key_commandsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var task_order;
function task_orderLoopBegin(task_orderLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    task_order = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: (("Group" + expInfo["group"]) + ".xlsx"),
      seed: undefined, name: 'task_order'
    });
    psychoJS.experiment.addLoop(task_order); // add the loop to the experiment
    currentLoop = task_order;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    task_order.forEach(function() {
      snapshot = task_order.getSnapshot();
    
      task_orderLoopScheduler.add(importConditions(snapshot));
      const task_blockLoopScheduler = new Scheduler(psychoJS);
      task_orderLoopScheduler.add(task_blockLoopBegin(task_blockLoopScheduler, snapshot));
      task_orderLoopScheduler.add(task_blockLoopScheduler);
      task_orderLoopScheduler.add(task_blockLoopEnd);
      task_orderLoopScheduler.add(task_orderLoopEndIteration(task_orderLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var task_block;
function task_blockLoopBegin(task_blockLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    task_block = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, (Task + "Task.xlsx"), 'np.random.choice(6, size=1, replace=False)'),
      seed: undefined, name: 'task_block'
    });
    psychoJS.experiment.addLoop(task_block); // add the loop to the experiment
    currentLoop = task_block;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    task_block.forEach(function() {
      snapshot = task_block.getSnapshot();
    
      task_blockLoopScheduler.add(importConditions(snapshot));
      task_blockLoopScheduler.add(instructionsRoutineBegin(snapshot));
      task_blockLoopScheduler.add(instructionsRoutineEachFrame());
      task_blockLoopScheduler.add(instructionsRoutineEnd(snapshot));
      task_blockLoopScheduler.add(practice_fixationRoutineBegin(snapshot));
      task_blockLoopScheduler.add(practice_fixationRoutineEachFrame());
      task_blockLoopScheduler.add(practice_fixationRoutineEnd(snapshot));
      const practice_trialLoopScheduler = new Scheduler(psychoJS);
      task_blockLoopScheduler.add(practice_trialLoopBegin(practice_trialLoopScheduler, snapshot));
      task_blockLoopScheduler.add(practice_trialLoopScheduler);
      task_blockLoopScheduler.add(practice_trialLoopEnd);
      task_blockLoopScheduler.add(practice_endRoutineBegin(snapshot));
      task_blockLoopScheduler.add(practice_endRoutineEachFrame());
      task_blockLoopScheduler.add(practice_endRoutineEnd(snapshot));
      const trialsLoopScheduler = new Scheduler(psychoJS);
      task_blockLoopScheduler.add(trialsLoopBegin(trialsLoopScheduler, snapshot));
      task_blockLoopScheduler.add(trialsLoopScheduler);
      task_blockLoopScheduler.add(trialsLoopEnd);
      task_blockLoopScheduler.add(trials_endRoutineBegin(snapshot));
      task_blockLoopScheduler.add(trials_endRoutineEachFrame());
      task_blockLoopScheduler.add(trials_endRoutineEnd(snapshot));
      task_blockLoopScheduler.add(task_blockLoopEndIteration(task_blockLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var practice_trial;
function practice_trialLoopBegin(practice_trialLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practice_trial = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 2, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: (Task + "TrialStim.xlsx"),
      seed: undefined, name: 'practice_trial'
    });
    psychoJS.experiment.addLoop(practice_trial); // add the loop to the experiment
    currentLoop = practice_trial;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practice_trial.forEach(function() {
      snapshot = practice_trial.getSnapshot();
    
      practice_trialLoopScheduler.add(importConditions(snapshot));
      practice_trialLoopScheduler.add(practice_targetRoutineBegin(snapshot));
      practice_trialLoopScheduler.add(practice_targetRoutineEachFrame());
      practice_trialLoopScheduler.add(practice_targetRoutineEnd(snapshot));
      practice_trialLoopScheduler.add(practice_ITIRoutineBegin(snapshot));
      practice_trialLoopScheduler.add(practice_ITIRoutineEachFrame());
      practice_trialLoopScheduler.add(practice_ITIRoutineEnd(snapshot));
      practice_trialLoopScheduler.add(practice_feedbackRoutineBegin(snapshot));
      practice_trialLoopScheduler.add(practice_feedbackRoutineEachFrame());
      practice_trialLoopScheduler.add(practice_feedbackRoutineEnd(snapshot));
      practice_trialLoopScheduler.add(practice_trialLoopEndIteration(practice_trialLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practice_trialLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practice_trial);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practice_trialLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 30, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: (Task + "TrialStim.xlsx"),
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(trial_fixationRoutineBegin(snapshot));
      trialsLoopScheduler.add(trial_fixationRoutineEachFrame());
      trialsLoopScheduler.add(trial_fixationRoutineEnd(snapshot));
      trialsLoopScheduler.add(trial_targetRoutineBegin(snapshot));
      trialsLoopScheduler.add(trial_targetRoutineEachFrame());
      trialsLoopScheduler.add(trial_targetRoutineEnd(snapshot));
      trialsLoopScheduler.add(trial_ITIRoutineBegin(snapshot));
      trialsLoopScheduler.add(trial_ITIRoutineEachFrame());
      trialsLoopScheduler.add(trial_ITIRoutineEnd(snapshot));
      trialsLoopScheduler.add(trial_feedbackRoutineBegin(snapshot));
      trialsLoopScheduler.add(trial_feedbackRoutineEachFrame());
      trialsLoopScheduler.add(trial_feedbackRoutineEnd(snapshot));
      trialsLoopScheduler.add(trial_breakRoutineBegin(snapshot));
      trialsLoopScheduler.add(trial_breakRoutineEachFrame());
      trialsLoopScheduler.add(trial_breakRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function task_blockLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(task_block);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function task_blockLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function task_orderLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(task_order);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function task_orderLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function key_commandsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(key_commands);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function key_commandsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var t;
var frameN;
var continueRoutine;
var _intro_resp_allKeys;
var introComponents;
function introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'intro' ---
    t = 0;
    introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('intro.started', globalClock.getTime());
    intro_resp.keys = undefined;
    intro_resp.rt = undefined;
    _intro_resp_allKeys = [];
    // keep track of which components have finished
    introComponents = [];
    introComponents.push(intro_text);
    introComponents.push(intro_resp);
    
    introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function introRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'intro' ---
    // get current time
    t = introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *intro_text* updates
    if (t >= 0.0 && intro_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_text.tStart = t;  // (not accounting for frame time here)
      intro_text.frameNStart = frameN;  // exact frame index
      
      intro_text.setAutoDraw(true);
    }
    
    
    // *intro_resp* updates
    if (t >= 0.0 && intro_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      intro_resp.tStart = t;  // (not accounting for frame time here)
      intro_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { intro_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { intro_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { intro_resp.clearEvents(); });
    }
    
    if (intro_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = intro_resp.getKeys({keyList: [], waitRelease: false});
      _intro_resp_allKeys = _intro_resp_allKeys.concat(theseKeys);
      if (_intro_resp_allKeys.length > 0) {
        intro_resp.keys = _intro_resp_allKeys[_intro_resp_allKeys.length - 1].name;  // just the last key pressed
        intro_resp.rt = _intro_resp_allKeys[_intro_resp_allKeys.length - 1].rt;
        intro_resp.duration = _intro_resp_allKeys[_intro_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function introRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'intro' ---
    introComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('intro.stopped', globalClock.getTime());
    intro_resp.stop();
    // the Routine "intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _instructions_resp_allKeys;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('instructions.started', globalClock.getTime());
    // Run 'Begin Routine' code from experiment_code
    /* Syntax Error: Fix Python code */
    instructions_text.setText(instr_message);
    instructions_resp.keys = undefined;
    instructions_resp.rt = undefined;
    _instructions_resp_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(instructions_text);
    instructionsComponents.push(instructions_resp);
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_text* updates
    if (t >= 0.0 && instructions_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_text.tStart = t;  // (not accounting for frame time here)
      instructions_text.frameNStart = frameN;  // exact frame index
      
      instructions_text.setAutoDraw(true);
    }
    
    
    // *instructions_resp* updates
    if (t >= 0.0 && instructions_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_resp.tStart = t;  // (not accounting for frame time here)
      instructions_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructions_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructions_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructions_resp.clearEvents(); });
    }
    
    if (instructions_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructions_resp.getKeys({keyList: [], waitRelease: false});
      _instructions_resp_allKeys = _instructions_resp_allKeys.concat(theseKeys);
      if (_instructions_resp_allKeys.length > 0) {
        instructions_resp.keys = _instructions_resp_allKeys[_instructions_resp_allKeys.length - 1].name;  // just the last key pressed
        instructions_resp.rt = _instructions_resp_allKeys[_instructions_resp_allKeys.length - 1].rt;
        instructions_resp.duration = _instructions_resp_allKeys[_instructions_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instructions.stopped', globalClock.getTime());
    instructions_resp.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_fixationComponents;
function practice_fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_fixation' ---
    t = 0;
    practice_fixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('practice_fixation.started', globalClock.getTime());
    // keep track of which components have finished
    practice_fixationComponents = [];
    practice_fixationComponents.push(practice_fixation_cross);
    
    practice_fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function practice_fixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_fixation' ---
    // get current time
    t = practice_fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practice_fixation_cross* updates
    if (t >= 0.0 && practice_fixation_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_fixation_cross.tStart = t;  // (not accounting for frame time here)
      practice_fixation_cross.frameNStart = frameN;  // exact frame index
      
      practice_fixation_cross.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practice_fixation_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_fixation_cross.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice_fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_fixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_fixation' ---
    practice_fixationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice_fixation.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var label_text;
var label_image;
var image_opacity;
var shape;
var corrAns;
var ITI_dur;
var target_dur;
var _practice_resp_allKeys;
var practice_targetComponents;
function practice_targetRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_target' ---
    t = 0;
    practice_targetClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('practice_target.started', globalClock.getTime());
    // Run 'Begin Routine' code from practice_code
    if ((Task === "Valence")) {
        label_text = "";
    } else {
        label_text = Label;
    }
    if ((Task === "Valence")) {
        label_image = (("Stimuli/" + Label) + ".bmp");
    } else {
        label_image = "Stimuli/Empty.bmp";
    }
    if ((Task === "Valence")) {
        image_opacity = 1;
    } else {
        image_opacity = 0;
    }
    if ((Task === "Control")) {
        if ((Target === "sky")) {
            shape = (("Stimuli/" + Label1) + ".bmp");
        } else {
            if ((Target === "earth")) {
                shape = (("Stimuli/" + Label2) + ".bmp");
            } else {
                if ((Target === "air")) {
                    shape = (("Stimuli/" + Label3) + ".bmp");
                }
            }
        }
    } else {
        if ((Task === "Reward")) {
            if ((Target === "HighReward")) {
                shape = (("Stimuli/" + Label1) + ".bmp");
            } else {
                if ((Target === "MediumReward")) {
                    shape = (("Stimuli/" + Label2) + ".bmp");
                } else {
                    if ((Target === "LowReward")) {
                        shape = (("Stimuli/" + Label3) + ".bmp");
                    }
                }
            }
        } else {
            if ((Task === "Valence")) {
                if ((Target === "Happy")) {
                    shape = (("Stimuli/" + Label1) + ".bmp");
                } else {
                    if ((Target === "Neutral")) {
                        shape = (("Stimuli/" + Label2) + ".bmp");
                    } else {
                        if ((Target === "Sad")) {
                            shape = (("Stimuli/" + Label3) + ".bmp");
                        }
                    }
                }
            }
        }
    }
    if ((CorrectAnswer === "Yes")) {
        if ((Yes === "n")) {
            corrAns = "n";
        } else {
            if ((Yes === "m")) {
                corrAns = "m";
            }
        }
    } else {
        if ((CorrectAnswer === "No")) {
            if ((No === "m")) {
                corrAns = "m";
            } else {
                if ((No === "n")) {
                    corrAns = "n";
                }
            }
        }
    }
    ITI_dur = (random.randint(500, 900) / 1000);
    if ((Task === "Valence")) {
        target_dur = (250 / 1000);
    } else {
        target_dur = (150 / 1000);
    }
    
    practice_target_label.setText(label_text);
    practice_target_shape.setImage(shape);
    practice_resp.keys = undefined;
    practice_resp.rt = undefined;
    _practice_resp_allKeys = [];
    practice_target_label_valence.setOpacity(image_opacity);
    practice_target_label_valence.setImage(label_image);
    // keep track of which components have finished
    practice_targetComponents = [];
    practice_targetComponents.push(practice_target_label);
    practice_targetComponents.push(practice_target_plus);
    practice_targetComponents.push(practice_target_shape);
    practice_targetComponents.push(practice_resp);
    practice_targetComponents.push(practice_target_label_valence);
    
    practice_targetComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice_targetRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_target' ---
    // get current time
    t = practice_targetClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practice_target_label* updates
    if (t >= 0.0 && practice_target_label.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_target_label.tStart = t;  // (not accounting for frame time here)
      practice_target_label.frameNStart = frameN;  // exact frame index
      
      practice_target_label.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + target_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practice_target_label.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_target_label.setAutoDraw(false);
    }
    
    // *practice_target_plus* updates
    if (t >= 0.0 && practice_target_plus.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_target_plus.tStart = t;  // (not accounting for frame time here)
      practice_target_plus.frameNStart = frameN;  // exact frame index
      
      practice_target_plus.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + target_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practice_target_plus.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_target_plus.setAutoDraw(false);
    }
    
    // *practice_target_shape* updates
    if (t >= 0.0 && practice_target_shape.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_target_shape.tStart = t;  // (not accounting for frame time here)
      practice_target_shape.frameNStart = frameN;  // exact frame index
      
      practice_target_shape.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + target_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practice_target_shape.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_target_shape.setAutoDraw(false);
    }
    
    // *practice_resp* updates
    if (t >= 0.0 && practice_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_resp.tStart = t;  // (not accounting for frame time here)
      practice_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { practice_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { practice_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { practice_resp.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practice_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (practice_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = practice_resp.getKeys({keyList: ['m', 'n'], waitRelease: false});
      _practice_resp_allKeys = _practice_resp_allKeys.concat(theseKeys);
      if (_practice_resp_allKeys.length > 0) {
        practice_resp.keys = _practice_resp_allKeys[_practice_resp_allKeys.length - 1].name;  // just the last key pressed
        practice_resp.rt = _practice_resp_allKeys[_practice_resp_allKeys.length - 1].rt;
        practice_resp.duration = _practice_resp_allKeys[_practice_resp_allKeys.length - 1].duration;
        // was this correct?
        if (practice_resp.keys == corrAns) {
            practice_resp.corr = 1;
        } else {
            practice_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *practice_target_label_valence* updates
    if (t >= 0.0 && practice_target_label_valence.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_target_label_valence.tStart = t;  // (not accounting for frame time here)
      practice_target_label_valence.frameNStart = frameN;  // exact frame index
      
      practice_target_label_valence.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + target_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practice_target_label_valence.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_target_label_valence.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice_targetComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_targetRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_target' ---
    practice_targetComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice_target.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (practice_resp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         practice_resp.corr = 1;  // correct non-response
      } else {
         practice_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(practice_resp.corr, level);
    }
    psychoJS.experiment.addData('practice_resp.keys', practice_resp.keys);
    psychoJS.experiment.addData('practice_resp.corr', practice_resp.corr);
    if (typeof practice_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('practice_resp.rt', practice_resp.rt);
        psychoJS.experiment.addData('practice_resp.duration', practice_resp.duration);
        routineTimer.reset();
        }
    
    practice_resp.stop();
    // the Routine "practice_target" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_ITIComponents;
function practice_ITIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_ITI' ---
    t = 0;
    practice_ITIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('practice_ITI.started', globalClock.getTime());
    // keep track of which components have finished
    practice_ITIComponents = [];
    practice_ITIComponents.push(ITI_text);
    
    practice_ITIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice_ITIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_ITI' ---
    // get current time
    t = practice_ITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ITI_text* updates
    if (t >= 0.0 && ITI_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ITI_text.tStart = t;  // (not accounting for frame time here)
      ITI_text.frameNStart = frameN;  // exact frame index
      
      ITI_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + ITI_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ITI_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ITI_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice_ITIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_ITIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_ITI' ---
    practice_ITIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice_ITI.stopped', globalClock.getTime());
    // the Routine "practice_ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practice_feedbackComponents;
function practice_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_feedback' ---
    t = 0;
    practice_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.500000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('practice_feedback.started', globalClock.getTime());
    practice_feedback_text.setColor(new util.Color(practice_feedback_colour));
    practice_feedback_text.setText(practice_feedback_msg);
    // keep track of which components have finished
    practice_feedbackComponents = [];
    practice_feedbackComponents.push(practice_feedback_text);
    
    practice_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_feedback' ---
    // get current time
    t = practice_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *practice_feedback_text* updates
    if (t >= 0.0 && practice_feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_feedback_text.tStart = t;  // (not accounting for frame time here)
      practice_feedback_text.frameNStart = frameN;  // exact frame index
      
      practice_feedback_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (practice_feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      practice_feedback_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_feedback' ---
    practice_feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice_feedback.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _self_practice_end_resp_allKeys;
var practice_endComponents;
function practice_endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_end' ---
    t = 0;
    practice_endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('practice_end.started', globalClock.getTime());
    self_practice_end_resp.keys = undefined;
    self_practice_end_resp.rt = undefined;
    _self_practice_end_resp_allKeys = [];
    // keep track of which components have finished
    practice_endComponents = [];
    practice_endComponents.push(self_practice_end_text);
    practice_endComponents.push(self_practice_end_resp);
    
    practice_endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice_endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_end' ---
    // get current time
    t = practice_endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *self_practice_end_text* updates
    if (t >= 0.0 && self_practice_end_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      self_practice_end_text.tStart = t;  // (not accounting for frame time here)
      self_practice_end_text.frameNStart = frameN;  // exact frame index
      
      self_practice_end_text.setAutoDraw(true);
    }
    
    
    // *self_practice_end_resp* updates
    if (t >= 0.0 && self_practice_end_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      self_practice_end_resp.tStart = t;  // (not accounting for frame time here)
      self_practice_end_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { self_practice_end_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { self_practice_end_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { self_practice_end_resp.clearEvents(); });
    }
    
    if (self_practice_end_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = self_practice_end_resp.getKeys({keyList: [], waitRelease: false});
      _self_practice_end_resp_allKeys = _self_practice_end_resp_allKeys.concat(theseKeys);
      if (_self_practice_end_resp_allKeys.length > 0) {
        self_practice_end_resp.keys = _self_practice_end_resp_allKeys[_self_practice_end_resp_allKeys.length - 1].name;  // just the last key pressed
        self_practice_end_resp.rt = _self_practice_end_resp_allKeys[_self_practice_end_resp_allKeys.length - 1].rt;
        self_practice_end_resp.duration = _self_practice_end_resp_allKeys[_self_practice_end_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    practice_endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_end' ---
    practice_endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('practice_end.stopped', globalClock.getTime());
    self_practice_end_resp.stop();
    // the Routine "practice_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trial_fixationComponents;
function trial_fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_fixation' ---
    t = 0;
    trial_fixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.250000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial_fixation.started', globalClock.getTime());
    // keep track of which components have finished
    trial_fixationComponents = [];
    trial_fixationComponents.push(self_trial_fixation_cross);
    
    trial_fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trial_fixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_fixation' ---
    // get current time
    t = trial_fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *self_trial_fixation_cross* updates
    if (t >= 0.0 && self_trial_fixation_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      self_trial_fixation_cross.tStart = t;  // (not accounting for frame time here)
      self_trial_fixation_cross.frameNStart = frameN;  // exact frame index
      
      self_trial_fixation_cross.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (self_trial_fixation_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      self_trial_fixation_cross.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial_fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial_fixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_fixation' ---
    trial_fixationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial_fixation.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _trial_resp_allKeys;
var trial_targetComponents;
function trial_targetRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_target' ---
    t = 0;
    trial_targetClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial_target.started', globalClock.getTime());
    // Run 'Begin Routine' code from trial_code
    if ((Task === "Valence")) {
        label_text = "";
    } else {
        label_text = Label;
    }
    if ((Task === "Valence")) {
        label_image = (("Stimuli/" + Label) + ".bmp");
    } else {
        label_image = "Stimuli/Empty.bmp";
    }
    if ((Task === "Valence")) {
        image_opacity = 1;
    } else {
        image_opacity = 0;
    }
    if ((Task === "Control")) {
        if ((Target === "sky")) {
            shape = (("Stimuli/" + Label1) + ".bmp");
        } else {
            if ((Target === "earth")) {
                shape = (("Stimuli/" + Label2) + ".bmp");
            } else {
                if ((Target === "air")) {
                    shape = (("Stimuli/" + Label3) + ".bmp");
                }
            }
        }
    } else {
        if ((Task === "Reward")) {
            if ((Target === "HighReward")) {
                shape = (("Stimuli/" + Label1) + ".bmp");
            } else {
                if ((Target === "MediumReward")) {
                    shape = (("Stimuli/" + Label2) + ".bmp");
                } else {
                    if ((Target === "LowReward")) {
                        shape = (("Stimuli/" + Label3) + ".bmp");
                    }
                }
            }
        } else {
            if ((Task === "Valence")) {
                if ((Target === "Happy")) {
                    shape = (("Stimuli/" + Label1) + ".bmp");
                } else {
                    if ((Target === "Neutral")) {
                        shape = (("Stimuli/" + Label2) + ".bmp");
                    } else {
                        if ((Target === "Sad")) {
                            shape = (("Stimuli/" + Label3) + ".bmp");
                        }
                    }
                }
            }
        }
    }
    if ((CorrectAnswer === "Yes")) {
        if ((Yes === "n")) {
            corrAns = "n";
        } else {
            if ((Yes === "m")) {
                corrAns = "m";
            }
        }
    } else {
        if ((CorrectAnswer === "No")) {
            if ((No === "m")) {
                corrAns = "m";
            } else {
                if ((No === "n")) {
                    corrAns = "n";
                }
            }
        }
    }
    ITI_dur = (random.randint(500, 900) / 1000);
    if ((Task === "Valence")) {
        target_dur = (250 / 1000);
    } else {
        target_dur = (150 / 1000);
    }
    
    trial_target_label.setText(label_text);
    trial_target_shape.setImage(shape);
    trial_resp.keys = undefined;
    trial_resp.rt = undefined;
    _trial_resp_allKeys = [];
    trial_target_label_valence.setOpacity(image_opacity);
    trial_target_label_valence.setImage(label_image);
    // keep track of which components have finished
    trial_targetComponents = [];
    trial_targetComponents.push(trial_target_label);
    trial_targetComponents.push(trial_target_plus);
    trial_targetComponents.push(trial_target_shape);
    trial_targetComponents.push(trial_resp);
    trial_targetComponents.push(trial_target_label_valence);
    
    trial_targetComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trial_targetRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_target' ---
    // get current time
    t = trial_targetClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trial_target_label* updates
    if (t >= 0.0 && trial_target_label.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_target_label.tStart = t;  // (not accounting for frame time here)
      trial_target_label.frameNStart = frameN;  // exact frame index
      
      trial_target_label.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + target_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_target_label.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_target_label.setAutoDraw(false);
    }
    
    // *trial_target_plus* updates
    if (t >= 0.0 && trial_target_plus.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_target_plus.tStart = t;  // (not accounting for frame time here)
      trial_target_plus.frameNStart = frameN;  // exact frame index
      
      trial_target_plus.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + target_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_target_plus.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_target_plus.setAutoDraw(false);
    }
    
    // *trial_target_shape* updates
    if (t >= 0.0 && trial_target_shape.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_target_shape.tStart = t;  // (not accounting for frame time here)
      trial_target_shape.frameNStart = frameN;  // exact frame index
      
      trial_target_shape.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + target_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_target_shape.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_target_shape.setAutoDraw(false);
    }
    
    // *trial_resp* updates
    if (t >= 0.0 && trial_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_resp.tStart = t;  // (not accounting for frame time here)
      trial_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { trial_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { trial_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { trial_resp.clearEvents(); });
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_resp.status = PsychoJS.Status.FINISHED;
        }
      
    if (trial_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = trial_resp.getKeys({keyList: ['m', 'n'], waitRelease: false});
      _trial_resp_allKeys = _trial_resp_allKeys.concat(theseKeys);
      if (_trial_resp_allKeys.length > 0) {
        trial_resp.keys = _trial_resp_allKeys[_trial_resp_allKeys.length - 1].name;  // just the last key pressed
        trial_resp.rt = _trial_resp_allKeys[_trial_resp_allKeys.length - 1].rt;
        trial_resp.duration = _trial_resp_allKeys[_trial_resp_allKeys.length - 1].duration;
        // was this correct?
        if (trial_resp.keys == corrAns) {
            trial_resp.corr = 1;
        } else {
            trial_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *trial_target_label_valence* updates
    if (t >= 0.0 && trial_target_label_valence.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_target_label_valence.tStart = t;  // (not accounting for frame time here)
      trial_target_label_valence.frameNStart = frameN;  // exact frame index
      
      trial_target_label_valence.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + target_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_target_label_valence.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_target_label_valence.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial_targetComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial_targetRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_target' ---
    trial_targetComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial_target.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (trial_resp.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         trial_resp.corr = 1;  // correct non-response
      } else {
         trial_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(trial_resp.corr, level);
    }
    psychoJS.experiment.addData('trial_resp.keys', trial_resp.keys);
    psychoJS.experiment.addData('trial_resp.corr', trial_resp.corr);
    if (typeof trial_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('trial_resp.rt', trial_resp.rt);
        psychoJS.experiment.addData('trial_resp.duration', trial_resp.duration);
        routineTimer.reset();
        }
    
    trial_resp.stop();
    // the Routine "trial_target" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trial_ITIComponents;
function trial_ITIRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_ITI' ---
    t = 0;
    trial_ITIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial_ITI.started', globalClock.getTime());
    // keep track of which components have finished
    trial_ITIComponents = [];
    trial_ITIComponents.push(self_trial_ITI_text);
    
    trial_ITIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trial_ITIRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_ITI' ---
    // get current time
    t = trial_ITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *self_trial_ITI_text* updates
    if (t >= 0.0 && self_trial_ITI_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      self_trial_ITI_text.tStart = t;  // (not accounting for frame time here)
      self_trial_ITI_text.frameNStart = frameN;  // exact frame index
      
      self_trial_ITI_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + ITI_dur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (self_trial_ITI_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      self_trial_ITI_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial_ITIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial_ITIRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_ITI' ---
    trial_ITIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial_ITI.stopped', globalClock.getTime());
    // the Routine "trial_ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trial_feedbackComponents;
function trial_feedbackRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_feedback' ---
    t = 0;
    trial_feedbackClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.250000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial_feedback.started', globalClock.getTime());
    self_trial_feedback_text.setColor(new util.Color(trial_feedback_colour));
    self_trial_feedback_text.setText(trial_feedback_msg);
    // keep track of which components have finished
    trial_feedbackComponents = [];
    trial_feedbackComponents.push(self_trial_feedback_text);
    
    trial_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trial_feedbackRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_feedback' ---
    // get current time
    t = trial_feedbackClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *self_trial_feedback_text* updates
    if (t >= 0.0 && self_trial_feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      self_trial_feedback_text.tStart = t;  // (not accounting for frame time here)
      self_trial_feedback_text.frameNStart = frameN;  // exact frame index
      
      self_trial_feedback_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (self_trial_feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      self_trial_feedback_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial_feedbackComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial_feedbackRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_feedback' ---
    trial_feedbackComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial_feedback.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _pj;
var trial_accuracy;
var trial_breakComponents;
function trial_breakRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_break' ---
    t = 0;
    trial_breakClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('trial_break.started', globalClock.getTime());
    // Run 'Begin Routine' code from trial_break_code
    var _pj;
    function _pj_snippets(container) {
        function in_es6(left, right) {
            if (((right instanceof Array) || ((typeof right) === "string"))) {
                return (right.indexOf(left) > (- 1));
            } else {
                if (((right instanceof Map) || (right instanceof Set) || (right instanceof WeakMap) || (right instanceof WeakSet))) {
                    return right.has(left);
                } else {
                    return (left in right);
                }
            }
        }
        container["in_es6"] = in_es6;
        return container;
    }
    _pj = {};
    _pj_snippets(_pj);
    if ((! _pj.in_es6(trials.thisN, [72, 144, 216, 288, 360]))) {
        continueRoutine = false;
    }
    trial_accuracy = Number.parseInt((trials.data["trial_resp.corr"].mean() * 100));
    
    trial_break_text.setText('');
    // keep track of which components have finished
    trial_breakComponents = [];
    trial_breakComponents.push(trial_break_text);
    trial_breakComponents.push(image);
    
    trial_breakComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trial_breakRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_break' ---
    // get current time
    t = trial_breakClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trial_break_text* updates
    if (t >= 0.0 && trial_break_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_break_text.tStart = t;  // (not accounting for frame time here)
      trial_break_text.frameNStart = frameN;  // exact frame index
      
      trial_break_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_break_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_break_text.setAutoDraw(false);
    }
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial_breakComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trial_breakRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_break' ---
    trial_breakComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial_break.stopped', globalClock.getTime());
    // the Routine "trial_break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _trials_end_resp_allKeys;
var trials_endComponents;
function trials_endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trials_end' ---
    t = 0;
    trials_endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    psychoJS.experiment.addData('trials_end.started', globalClock.getTime());
    trials_end_resp.keys = undefined;
    trials_end_resp.rt = undefined;
    _trials_end_resp_allKeys = [];
    // keep track of which components have finished
    trials_endComponents = [];
    trials_endComponents.push(trials_end_text);
    trials_endComponents.push(trials_end_resp);
    
    trials_endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trials_endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trials_end' ---
    // get current time
    t = trials_endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trials_end_text* updates
    if (t >= 0.0 && trials_end_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trials_end_text.tStart = t;  // (not accounting for frame time here)
      trials_end_text.frameNStart = frameN;  // exact frame index
      
      trials_end_text.setAutoDraw(true);
    }
    
    
    // *trials_end_resp* updates
    if (t >= 0.0 && trials_end_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trials_end_resp.tStart = t;  // (not accounting for frame time here)
      trials_end_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { trials_end_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { trials_end_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { trials_end_resp.clearEvents(); });
    }
    
    if (trials_end_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = trials_end_resp.getKeys({keyList: [], waitRelease: false});
      _trials_end_resp_allKeys = _trials_end_resp_allKeys.concat(theseKeys);
      if (_trials_end_resp_allKeys.length > 0) {
        trials_end_resp.keys = _trials_end_resp_allKeys[_trials_end_resp_allKeys.length - 1].name;  // just the last key pressed
        trials_end_resp.rt = _trials_end_resp_allKeys[_trials_end_resp_allKeys.length - 1].rt;
        trials_end_resp.duration = _trials_end_resp_allKeys[_trials_end_resp_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trials_endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trials_endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trials_end' ---
    trials_endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trials_end.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(trials_end_resp.corr, level);
    }
    psychoJS.experiment.addData('trials_end_resp.keys', trials_end_resp.keys);
    if (typeof trials_end_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('trials_end_resp.rt', trials_end_resp.rt);
        psychoJS.experiment.addData('trials_end_resp.duration', trials_end_resp.duration);
        routineTimer.reset();
        }
    
    trials_end_resp.stop();
    // the Routine "trials_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var endComponents;
function endRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'end' ---
    t = 0;
    endClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    psychoJS.experiment.addData('end.started', globalClock.getTime());
    // keep track of which components have finished
    endComponents = [];
    endComponents.push(text);
    
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function endRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'end' ---
    // get current time
    t = endClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    endComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function endRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'end' ---
    endComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('end.stopped', globalClock.getTime());
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
