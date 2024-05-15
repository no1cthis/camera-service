from camera_service.modules.modules_list import modules
import concurrent.futures

# Define a thread pool with a maximum number of worker threads
pool = concurrent.futures.ThreadPoolExecutor(max_workers=10)

# Dictionary to hold futures for each module
module_futures = {}

def start_processing(frame, frame_number):

	# Submit each module processing task to the thread pool
	for module in modules:
		previous_module_future = module_futures.get(module.get("proccessing"))
		skip_frames = None
		if module and module.get("options"):
			skip_frames = module.get("options").get("processing_frame")

		print("Processing frame number", frame_number, skip_frames)
		# Check if the previous module is done processing
		if previous_module_future is None or (skip_frames is None and previous_module_future.running() is False) or (skip_frames is not None and frame_number % skip_frames == 0):
			# Submit module processing task to the thread pool and store the future

			future = pool.submit(module.get("proccessing"), frame, frame_number)	
			module_futures[module.get("proccessing")] = future
		