"""Implementation of statechart model.
Generated by itemis CREATE code generator.
"""

import queue
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

class Model:
	"""Implementation of the state machine Model.
	"""

	class State:
		""" State Enum
		"""
		(
			main_region_stopped,
			main_region_move_forward,
			null_state
		) = range(3)
	
	
	class UserVar:
		"""Implementation of scope UserVar.
		"""
		
		def __init__(self, statemachine):
			self.base_speed = None
			self.base_rotation = None
			self.startprocedure = None
			
			self.statemachine = statemachine
		
	
	class BaseValues:
		"""Implementation of scope BaseValues.
		"""
		
		def __init__(self, statemachine):
			self.max_speed = None
			self.max_rotation = None
			self.degrees_front = None
			self.degrees_right = None
			self.degrees_back = None
			self.degrees_left = None
			
			self.statemachine = statemachine
		
	
	class Output:
		"""Implementation of scope Output.
		"""
		
		def __init__(self, statemachine):
			self.speed = None
			self.rotation = None
			self.obstacles = None
			self.gems = None
			self.finish = None
			
			self.statemachine = statemachine
		
	
	class Grid:
		"""Implementation of scope Grid.
		"""
		
		def __init__(self, statemachine):
			self.update = None
			self.receive = None
			self.column = None
			self.row = None
			self.orientation = None
			self.visited = None
			self.wall_front = None
			self.wall_right = None
			self.wall_back = None
			self.wall_left = None
			self.grid_size = None
			self.max_col = None
			self.max_row = None
			
			self.statemachine = statemachine
		
	
	class StartPos:
		"""Implementation of scope StartPos.
		"""
		
		def __init__(self, statemachine):
			self.set_zero = None
			self.zero_x = None
			self.zero_y = None
			self.zero_south_degree = None
			self.laser_deg_offset = None
			
			self.statemachine = statemachine
		
	
	class Computer:
		"""Implementation of scope Computer.
		"""
		
		def __init__(self, statemachine):
			self.m_press = None
			self.w_press = None
			self.a_press = None
			self.s_press = None
			self.d_press = None
			self.x_press = None
			
			self.statemachine = statemachine
		
		def raise_m_press(self):
			"""Raise method for event m_press.
			"""
			self.statemachine.in_event_queue.put(self.__raise_m_press_call)
			self.statemachine.run_cycle()
		
		def __raise_m_press_call(self):
			"""Raise callback for event m_press.
			"""
			self.m_press = True
		
		def raise_w_press(self):
			"""Raise method for event w_press.
			"""
			self.statemachine.in_event_queue.put(self.__raise_w_press_call)
			self.statemachine.run_cycle()
		
		def __raise_w_press_call(self):
			"""Raise callback for event w_press.
			"""
			self.w_press = True
		
		def raise_a_press(self):
			"""Raise method for event a_press.
			"""
			self.statemachine.in_event_queue.put(self.__raise_a_press_call)
			self.statemachine.run_cycle()
		
		def __raise_a_press_call(self):
			"""Raise callback for event a_press.
			"""
			self.a_press = True
		
		def raise_s_press(self):
			"""Raise method for event s_press.
			"""
			self.statemachine.in_event_queue.put(self.__raise_s_press_call)
			self.statemachine.run_cycle()
		
		def __raise_s_press_call(self):
			"""Raise callback for event s_press.
			"""
			self.s_press = True
		
		def raise_d_press(self):
			"""Raise method for event d_press.
			"""
			self.statemachine.in_event_queue.put(self.__raise_d_press_call)
			self.statemachine.run_cycle()
		
		def __raise_d_press_call(self):
			"""Raise callback for event d_press.
			"""
			self.d_press = True
		
		def raise_x_press(self):
			"""Raise method for event x_press.
			"""
			self.statemachine.in_event_queue.put(self.__raise_x_press_call)
			self.statemachine.run_cycle()
		
		def __raise_x_press_call(self):
			"""Raise callback for event x_press.
			"""
			self.x_press = True
		
	
	class Imu:
		"""Implementation of scope Imu.
		"""
		
		def __init__(self, statemachine):
			self.pitch = None
			self.roll = None
			self.yaw = None
			
			self.statemachine = statemachine
		
	
	class Odom:
		"""Implementation of scope Odom.
		"""
		
		def __init__(self, statemachine):
			self.x = None
			self.y = None
			self.z = None
			
			self.statemachine = statemachine
		
	
	class LaserDistance:
		"""Implementation of scope LaserDistance.
		"""
		
		def __init__(self, statemachine):
			self.d0 = None
			self.d90 = None
			self.d180 = None
			self.dm90 = None
			self.dmin = None
			self.min_deg = None
			self.dmax = None
			self.max_deg = None
			self.dmean = None
			self.dfront_min = None
			self.min_deg_f = None
			self.dfront_max = None
			self.max_deg_f = None
			self.dfront_mean = None
			self.dright_min = None
			self.min_deg_r = None
			self.dright_max = None
			self.max_deg_r = None
			self.dright_mean = None
			self.dback_min = None
			self.min_deg_b = None
			self.dback_max = None
			self.max_deg_b = None
			self.dback_mean = None
			self.dleft_min = None
			self.min_deg_l = None
			self.dleft_max = None
			self.max_deg_l = None
			self.dleft_mean = None
			
			self.statemachine = statemachine
		
	
	class LaserIntensity:
		"""Implementation of scope LaserIntensity.
		"""
		
		def __init__(self, statemachine):
			self.i0 = None
			self.i90 = None
			self.i180 = None
			self.im90 = None
			self.ifront_min = None
			self.ifront_max = None
			self.ifront_mean = None
			self.iright_min = None
			self.iright_max = None
			self.iright_mean = None
			self.iback_min = None
			self.iback_max = None
			self.iback_mean = None
			self.ileft_min = None
			self.ileft_max = None
			self.ileft_mean = None
			
			self.statemachine = statemachine
		
	
	def __init__(self):
		""" Declares all necessary variables including list of states, histories etc. 
		"""
		self.user_var = Model.UserVar(self)
		self.base_values = Model.BaseValues(self)
		self.output = Model.Output(self)
		self.grid = Model.Grid(self)
		self.start_pos = Model.StartPos(self)
		self.computer = Model.Computer(self)
		self.imu = Model.Imu(self)
		self.odom = Model.Odom(self)
		self.laser_distance = Model.LaserDistance(self)
		self.laser_intensity = Model.LaserIntensity(self)
		
		self.in_event_queue = queue.Queue()
		# enumeration of all states:
		self.__State = Model.State
		self.__state_conf_vector_changed = None
		self.__state_vector = [None] * 1
		for __state_index in range(1):
			self.__state_vector[__state_index] = self.State.null_state
		
		# for timed statechart:
		self.timer_service = None
		self.__time_events = [None] * 1
		
		# initializations:
		#Default init sequence for statechart model
		self.user_var.base_speed = 0.05
		self.user_var.base_rotation = 0.2
		self.user_var.startprocedure = True
		self.base_values.max_speed = 0.22
		self.base_values.max_rotation = 2.84
		self.base_values.degrees_front = 10
		self.base_values.degrees_right = 10
		self.base_values.degrees_back = 10
		self.base_values.degrees_left = 10
		self.output.speed = 0.0
		self.output.rotation = 0.0
		self.output.obstacles = 0
		self.output.gems = 0
		self.output.finish = 0
		self.grid.update = False
		self.grid.receive = False
		self.grid.column = 0
		self.grid.row = 0
		self.grid.orientation = 0
		self.grid.visited = False
		self.grid.wall_front = 0
		self.grid.wall_right = 0
		self.grid.wall_back = 0
		self.grid.wall_left = 0
		self.grid.grid_size = 0.48
		self.grid.max_col = 3
		self.grid.max_row = 3
		self.start_pos.set_zero = False
		self.start_pos.zero_x = 0.0
		self.start_pos.zero_y = 0.0
		self.start_pos.zero_south_degree = 0.0
		self.start_pos.laser_deg_offset = 0
		self.imu.pitch = 0.0
		self.imu.roll = 0.0
		self.imu.yaw = 0.0
		self.odom.x = 0.0
		self.odom.y = 0.0
		self.odom.z = 0.0
		self.laser_distance.d0 = 0.0
		self.laser_distance.d90 = 0.0
		self.laser_distance.d180 = 0.0
		self.laser_distance.dm90 = 0.0
		self.laser_distance.dmin = 0.0
		self.laser_distance.min_deg = 0
		self.laser_distance.dmax = 0.0
		self.laser_distance.max_deg = 0
		self.laser_distance.dmean = 0.0
		self.laser_distance.dfront_min = 0.0
		self.laser_distance.min_deg_f = 0
		self.laser_distance.dfront_max = 0.0
		self.laser_distance.max_deg_f = 0
		self.laser_distance.dfront_mean = 0.0
		self.laser_distance.dright_min = 0.0
		self.laser_distance.min_deg_r = 0
		self.laser_distance.dright_max = 0.0
		self.laser_distance.max_deg_r = 0
		self.laser_distance.dright_mean = 0.0
		self.laser_distance.dback_min = 0.0
		self.laser_distance.min_deg_b = 0
		self.laser_distance.dback_max = 0.0
		self.laser_distance.max_deg_b = 0
		self.laser_distance.dback_mean = 0.0
		self.laser_distance.dleft_min = 0.0
		self.laser_distance.min_deg_l = 0
		self.laser_distance.dleft_max = 0.0
		self.laser_distance.max_deg_l = 0
		self.laser_distance.dleft_mean = 0.0
		self.laser_intensity.i0 = 0.0
		self.laser_intensity.i90 = 0.0
		self.laser_intensity.i180 = 0.0
		self.laser_intensity.im90 = 0.0
		self.laser_intensity.ifront_min = 0.0
		self.laser_intensity.ifront_max = 0.0
		self.laser_intensity.ifront_mean = 0.0
		self.laser_intensity.iright_min = 0.0
		self.laser_intensity.iright_max = 0.0
		self.laser_intensity.iright_mean = 0.0
		self.laser_intensity.iback_min = 0.0
		self.laser_intensity.iback_max = 0.0
		self.laser_intensity.iback_mean = 0.0
		self.laser_intensity.ileft_min = 0.0
		self.laser_intensity.ileft_max = 0.0
		self.laser_intensity.ileft_mean = 0.0
		self.__is_executing = False
	
	def is_active(self):
		"""Checks if the state machine is active.
		"""
		return self.__state_vector[0] is not self.__State.null_state
	
	def is_final(self):
		"""Checks if the statemachine is final.
		Always returns 'false' since this state machine can never become final.
		"""
		return False
			
	def is_state_active(self, state):
		"""Checks if the state is currently active.
		"""
		s = state
		if s == self.__State.main_region_stopped:
			return self.__state_vector[0] == self.__State.main_region_stopped
		if s == self.__State.main_region_move_forward:
			return self.__state_vector[0] == self.__State.main_region_move_forward
		return False
		
	def time_elapsed(self, event_id):
		"""Add time events to in event queue
		"""
		if event_id in range(1):
			self.in_event_queue.put(lambda: self.raise_time_event(event_id))
			self.run_cycle()
	
	def raise_time_event(self, event_id):
		"""Raise timed events using the event_id.
		"""
		self.__time_events[event_id] = True
	
	def __execute_queued_event(self, func):
		func()
	
	def __get_next_event(self):
		if not self.in_event_queue.empty():
			return self.in_event_queue.get()
		return None
	
	def __entry_action_main_region_stopped(self):
		"""Entry action for state 'stopped'..
		"""
		#Entry action for state 'stopped'.
		self.output.speed = 0.0
		
	def __entry_action_main_region_move_forward(self):
		"""Entry action for state 'Move Forward'..
		"""
		#Entry action for state 'Move Forward'.
		self.timer_service.set_timer(self, 0, (15 * 1000), False)
		self.output.speed = self.user_var.base_speed
		
	def __exit_action_main_region_move_forward(self):
		"""Exit action for state 'Move Forward'..
		"""
		#Exit action for state 'Move Forward'.
		self.timer_service.unset_timer(self, 0)
		
	def __enter_sequence_main_region_stopped_default(self):
		"""'default' enter sequence for state stopped.
		"""
		#'default' enter sequence for state stopped
		self.__entry_action_main_region_stopped()
		self.__state_vector[0] = self.State.main_region_stopped
		self.__state_conf_vector_changed = True
		
	def __enter_sequence_main_region_move_forward_default(self):
		"""'default' enter sequence for state Move Forward.
		"""
		#'default' enter sequence for state Move Forward
		self.__entry_action_main_region_move_forward()
		self.__state_vector[0] = self.State.main_region_move_forward
		self.__state_conf_vector_changed = True
		
	def __enter_sequence_main_region_default(self):
		"""'default' enter sequence for region main region.
		"""
		#'default' enter sequence for region main region
		self.__react_main_region__entry_default()
		
	def __exit_sequence_main_region_stopped(self):
		"""Default exit sequence for state stopped.
		"""
		#Default exit sequence for state stopped
		self.__state_vector[0] = self.State.null_state
		
	def __exit_sequence_main_region_move_forward(self):
		"""Default exit sequence for state Move Forward.
		"""
		#Default exit sequence for state Move Forward
		self.__state_vector[0] = self.State.null_state
		self.__exit_action_main_region_move_forward()
		
	def __exit_sequence_main_region(self):
		"""Default exit sequence for region main region.
		"""
		#Default exit sequence for region main region
		state = self.__state_vector[0]
		if state == self.State.main_region_stopped:
			self.__exit_sequence_main_region_stopped()
		elif state == self.State.main_region_move_forward:
			self.__exit_sequence_main_region_move_forward()
		
	def __react_main_region__entry_default(self):
		"""Default react sequence for initial entry .
		"""
		#Default react sequence for initial entry 
		self.__enter_sequence_main_region_stopped_default()
		
	def __react(self, transitioned_before):
		"""Implementation of __react function.
		"""
		#State machine reactions.
		return transitioned_before
	
	
	def __main_region_stopped_react(self, transitioned_before):
		"""Implementation of __main_region_stopped_react function.
		"""
		#The reactions of state stopped.
		transitioned_after = transitioned_before
		if transitioned_after < 0:
			if self.computer.w_press:
				self.__exit_sequence_main_region_stopped()
				self.__enter_sequence_main_region_move_forward_default()
				self.__react(0)
				transitioned_after = 0
		#If no transition was taken
		if transitioned_after == transitioned_before:
			#then execute local reactions.
			transitioned_after = self.__react(transitioned_before)
		return transitioned_after
	
	
	def __main_region_move_forward_react(self, transitioned_before):
		"""Implementation of __main_region_move_forward_react function.
		"""
		#The reactions of state Move Forward.
		transitioned_after = transitioned_before
		if transitioned_after < 0:
			if self.__time_events[0]:
				self.__exit_sequence_main_region_move_forward()
				self.__time_events[0] = False
				self.__enter_sequence_main_region_stopped_default()
				self.__react(0)
				transitioned_after = 0
		#If no transition was taken
		if transitioned_after == transitioned_before:
			#then execute local reactions.
			transitioned_after = self.__react(transitioned_before)
		return transitioned_after
	
	
	def __clear_in_events(self):
		"""Implementation of __clear_in_events function.
		"""
		self.computer.m_press = False
		self.computer.w_press = False
		self.computer.a_press = False
		self.computer.s_press = False
		self.computer.d_press = False
		self.computer.x_press = False
		self.__time_events[0] = False
	
	
	def __micro_step(self):
		"""Implementation of __micro_step function.
		"""
		state = self.__state_vector[0]
		if state == self.State.main_region_stopped:
			self.__main_region_stopped_react(-1)
		elif state == self.State.main_region_move_forward:
			self.__main_region_move_forward_react(-1)
	
	
	def run_cycle(self):
		"""Implementation of run_cycle function.
		"""
		#Performs a 'run to completion' step.
		if self.timer_service is None:
			raise ValueError('Timer service must be set.')
		
		if self.__is_executing:
			return
		self.__is_executing = True
		next_event = self.__get_next_event()
		if next_event is not None:
			self.__execute_queued_event(next_event)
		condition_0 = True
		while condition_0:
			self.__micro_step()
			self.__clear_in_events()
			condition_0 = False
			next_event = self.__get_next_event()
			if next_event is not None:
				self.__execute_queued_event(next_event)
				condition_0 = True
		self.__is_executing = False
	
	
	def enter(self):
		"""Implementation of enter function.
		"""
		#Activates the state machine.
		if self.timer_service is None:
			raise ValueError('Timer service must be set.')
		
		if self.__is_executing:
			return
		self.__is_executing = True
		#Default enter sequence for statechart model
		self.__enter_sequence_main_region_default()
		self.__is_executing = False
	
	
	def exit(self):
		"""Implementation of exit function.
		"""
		#Deactivates the state machine.
		if self.__is_executing:
			return
		self.__is_executing = True
		#Default exit sequence for statechart model
		self.__exit_sequence_main_region()
		self.__state_vector[0] = self.State.null_state
		self.__is_executing = False
	
	
	def trigger_without_event(self):
		"""Implementation of triggerWithoutEvent function.
		"""
		self.run_cycle()
	
