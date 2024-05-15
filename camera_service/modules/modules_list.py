

def test(frame, frame_number):
    print("Test module processing frame number", frame_number)

def test2(frame, frame_number):
    print("Test2 module processing frame number", frame_number) 

modules = [
    {'proccessing': test, "options": {"processing_frame": 10}},
    {'proccessing': test2, "options": {"processing_frame": 20}},
    ]