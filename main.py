import tkinter as tk
from tkinter import ttk
from detection_parameters import *
from PIL import Image, ImageTk
from get_frames import get_images, release_video_capture


default_detection_parameters = get_default_values()
current_detection_parameters = default_detection_parameters.copy()
print(default_detection_parameters)

run_opencv_id = None





window = tk.Tk()
window.geometry('1600x1000')

# Create a custom style for the Notebook tabs
style = ttk.Style()
style.configure('Custom.TNotebook.Tab', padding=[20, 10], font=('Helvetica', 8))

notebook = ttk.Notebook(window, style='Custom.TNotebook')  # create the notebook


def update_the_default_parameters():
    # update the current values
    current_detection_parameters['lower_h'] = low_h_int.get()
    current_detection_parameters['upper_h'] = high_h_int.get()
    current_detection_parameters['lower_s'] = low_s_int.get()
    current_detection_parameters['upper_s'] = high_s_int.get()
    current_detection_parameters['lower_v'] = low_v_int.get()
    current_detection_parameters['upper_v'] = high_v_int.get()
    current_detection_parameters['kernel'] = ker_s_int.get()
    current_detection_parameters['blur'] = blur_int.get()
    current_detection_parameters['radius'] = radius_int.get()
    #print("Array Updated")


# function that runs when the tabs are changed by the user

def run_function():

    current_tab_index = notebook.index(notebook.select())  # Get the index of the currently selected tab
    if current_tab_index == 1:  # Tab 1 is active
        #tab1.after(200,run_function)
        print("tab1")


def stop_opencv():
    opencv_button.configure(state='active')
    opencv_button_stop.configure(state='disabled')
    global run_opencv_id
    if run_opencv_id:
        right_pic_label.after_cancel(run_opencv_id)

    release_video_capture()





def run_opencv():
    global run_opencv_id

    opencv_button.configure(state='disabled')
    opencv_button_stop.configure(state='active')



    l_pic, r_pic = get_images(current_detection_parameters)
    left_pic_label.photo_image = l_pic

    # Configure image in the label
    left_pic_label.configure(image=l_pic)


    right_pic_label.photo_image = r_pic

    # Configure image in the label
    right_pic_label.configure(image=r_pic)

    run_opencv_id = right_pic_label.after(5,run_opencv)




# To detect when the tabs are changed
notebook.bind("<<NotebookTabChanged>>", lambda event: run_function())


# create different frames for the notebook
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# add the two frames for the notebook
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

# add the notebook to the main window
notebook.pack(expand=True, fill='both')  # make the widget fill when the main window is resized

tk.Label(tab1, text="hello, this is tab 1", width=50, height=25).pack()


# frame to hold the horizontal scales
scale_frame = ttk.Frame(tab2, width=300, height=300)



# frame for the web cam
web_cam_frame = ttk.Frame(tab2, width=800, height=800)




# add the rows and columns to the scale_frame
scale_frame.columnconfigure(0, weight=1)
scale_frame.columnconfigure(1, weight=1)
scale_frame.columnconfigure(2, weight=1)

scale_frame.columnconfigure(3, weight=1)
scale_frame.columnconfigure(4, weight=1)
scale_frame.columnconfigure(5, weight=1)

# For H values
scale_frame.rowconfigure(0, weight=1)

# For S values
scale_frame.rowconfigure(1, weight=1)

# For V values
scale_frame.rowconfigure(2, weight=1)

# for Ker and Blur
scale_frame.rowconfigure(3, weight=1)

# for Radius and Reset andSave Buttons
scale_frame.rowconfigure(4, weight=1)

# To Show Live Detections
scale_frame.rowconfigure(5, weight=1)






# H values
# Add the 1st scale to row 0
# Variable to have the data
low_h_int = tk.IntVar(value=default_detection_parameters['lower_h'])

low_h_scale_label = ttk.Label(scale_frame, text='LOW H')
low_h_scale = ttk.Scale(scale_frame, from_=0, to=255, orient='horizontal',length=300, variable=low_h_int, command=lambda value: ((low_h_scale_value_label.configure(text=low_h_int.get())), update_the_default_parameters()))
low_h_scale_value_label = ttk.Label(scale_frame, text=low_h_int.get())

low_h_scale_label.grid(row=0, column=0, padx=10)
low_h_scale.grid(row=0, column=1, padx=10)
low_h_scale_value_label.grid(row=0, column=2, padx=100)


high_h_int = tk.IntVar(value=default_detection_parameters['upper_h'])

high_h_scale_label = ttk.Label(scale_frame,text='HIGH H')
high_h_scale = ttk.Scale(scale_frame, from_=0, to=255, orient='horizontal',length=300, variable=high_h_int, command=lambda value: ((high_h_scale_value_label.configure(text=high_h_int.get())), update_the_default_parameters()))
high_h_scale_value_label = ttk.Label(scale_frame, text=high_h_int.get())

high_h_scale_label.grid(row=0, column=3, padx=10, pady=10)
high_h_scale.grid(row=0, column=4, padx=10, pady=10)
high_h_scale_value_label.grid(row=0, column=5, padx=100, pady=10)

# S values
# Add the 1st scale to row 1
# Variable to have the data
low_s_int = tk.IntVar(value=default_detection_parameters['lower_s'])

low_s_scale_label = ttk.Label(scale_frame,text='LOW S')
low_s_scale = ttk.Scale(scale_frame, from_=0, to=255, orient='horizontal',length=300, variable=low_s_int, command=lambda value: ((low_s_scale_value_label.configure(text=low_s_int.get())), update_the_default_parameters()))
low_s_scale_value_label = ttk.Label(scale_frame, text=low_s_int.get())

low_s_scale_label.grid(row=1, column=0, padx=10, pady=10)
low_s_scale.grid(row=1, column=1, padx=10, pady=10)
low_s_scale_value_label.grid(row=1, column=2, padx=100, pady=10)


high_s_int = tk.IntVar(value=default_detection_parameters['upper_s'])

high_s_scale_label = ttk.Label(scale_frame,text='HIGH S')
high_s_scale = ttk.Scale(scale_frame, from_=0, to=255, orient='horizontal',length=300, variable=high_s_int, command=lambda value: ((high_s_scale_value_label.configure(text=high_s_int.get())), update_the_default_parameters()))
high_s_scale_value_label = ttk.Label(scale_frame, text=high_s_int.get())

high_s_scale_label.grid(row=1, column=3, padx=10, pady=10)
high_s_scale.grid(row=1, column=4, padx=10, pady=10)
high_s_scale_value_label.grid(row=1, column=5, padx=100, pady=10)

# V values
# Add the 1st scale to row 2
# Variable to have the data
low_v_int = tk.IntVar(value=default_detection_parameters['lower_v'])

low_v_scale_label = ttk.Label(scale_frame,text='LOW V')
low_v_scale = ttk.Scale(scale_frame, from_=0, to=255, orient='horizontal',length=300, variable=low_v_int, command=lambda value: ((low_v_scale_value_label.configure(text=low_v_int.get())), update_the_default_parameters()))
low_v_scale_value_label = ttk.Label(scale_frame, text=low_v_int.get())

low_v_scale_label.grid(row=2, column=0, padx=10, pady=10)
low_v_scale.grid(row=2, column=1, padx=10, pady=10)
low_v_scale_value_label.grid(row=2, column=2, padx=100, pady=10)


high_v_int = tk.IntVar(value=default_detection_parameters['upper_v'])

high_v_scale_label = ttk.Label(scale_frame,text='HIGH V')
high_v_scale = ttk.Scale(scale_frame, from_=0, to=255, orient='horizontal',length=300, variable=high_v_int, command=lambda value: ((high_v_scale_value_label.configure(text=high_v_int.get())), update_the_default_parameters()))
high_v_scale_value_label = ttk.Label(scale_frame, text=high_s_int.get())

high_v_scale_label.grid(row=2, column=3, padx=10, pady=10)
high_v_scale.grid(row=2, column=4, padx=10, pady=10)
high_v_scale_value_label.grid(row=2, column=5, padx=100, pady=10)


# Kernel Size values
# Add the 1st scale to row 3
# Variable to have the data
ker_s_int = tk.IntVar(value=default_detection_parameters['kernel'])

ker_s_scale_label = ttk.Label(scale_frame, text='KER SIZE')
ker_s_scale = ttk.Scale(scale_frame, from_=0, to=255, orient='horizontal',length=300, variable=ker_s_int, command=lambda value: ((ker_s_scale_value_label.configure(text=ker_s_int.get())), update_the_default_parameters()))
ker_s_scale_value_label = ttk.Label(scale_frame, text=ker_s_int.get())

ker_s_scale_label.grid(row=3, column=0, padx=10, pady=10)
ker_s_scale.grid(row=3, column=1, padx=10, pady=10)
ker_s_scale_value_label.grid(row=3, column=2, padx=100, pady=10)

# Blur
blur_int = tk.IntVar(value=default_detection_parameters['blur'])

blur_scale_label = ttk.Label(scale_frame,text='BLUR')
blur_scale = ttk.Scale(scale_frame, from_=0, to=10, orient='horizontal',length=300, variable=blur_int, command=lambda value: ((blur_scale_value_label.configure(text=blur_int.get())), update_the_default_parameters()))
blur_scale_value_label = ttk.Label(scale_frame, text=blur_int.get())

blur_scale_label.grid(row=3, column=3, padx=10, pady=10)
blur_scale.grid(row=3, column=4, padx=10, pady=10)
blur_scale_value_label.grid(row=3, column=5, padx=100, pady=10)

# Row 4
# Filter Radius
radius_int = tk.IntVar(value=default_detection_parameters['radius'])

radius_scale_label = ttk.Label(scale_frame,text='RADIUS')
radius_scale = ttk.Scale(scale_frame, from_=0, to=100, orient='horizontal',length=300, variable=radius_int, command=lambda value: ((radius_scale_value_label.configure(text=radius_int.get())), update_the_default_parameters()))
radius_scale_value_label = ttk.Label(scale_frame, text=radius_int.get())

radius_scale_label.grid(row=4, column=0, padx=10, pady=10)
radius_scale.grid(row=4, column=1, padx=10, pady=10)
radius_scale_value_label.grid(row=4, column=2, padx=100, pady=10)

def reset_scales():
    print(default_detection_parameters)
    low_h_int.set(default_detection_parameters['lower_h'])
    high_h_int.set(default_detection_parameters['upper_h'])
    low_s_int.set(default_detection_parameters['lower_s'])
    high_s_int.set(default_detection_parameters['upper_s'])
    low_v_int.set(default_detection_parameters['lower_v'])
    high_v_int.set(default_detection_parameters['upper_v'])
    ker_s_int.set(default_detection_parameters['kernel'])
    blur_int.set(default_detection_parameters['blur'])
    radius_int.set(default_detection_parameters['radius'])

    low_h_scale_value_label.configure(text=low_h_int.get())
    high_h_scale_value_label.configure(text=high_h_int.get())
    low_s_scale_value_label.configure(text=low_s_int.get())
    high_s_scale_value_label.configure(text=high_s_int.get())
    low_v_scale_value_label.configure(text=low_v_int.get())
    high_v_scale_value_label.configure(text=high_v_int.get())

    ker_s_scale_value_label.configure(text=ker_s_int.get())
    blur_scale_value_label.configure(text=blur_int.get())
    radius_scale_value_label.configure(text=radius_int.get())
    update_the_default_parameters()


def save_configuration_file():

    current_detection_parameters['lower_h'] = low_h_int.get()
    current_detection_parameters['upper_h'] = high_h_int.get()
    current_detection_parameters['lower_s'] = low_s_int.get()
    current_detection_parameters['upper_s'] = high_s_int.get()
    current_detection_parameters['lower_v'] = low_v_int.get()
    current_detection_parameters['upper_v'] = high_v_int.get()
    current_detection_parameters['kernel'] = ker_s_int.get()
    current_detection_parameters['blur'] = blur_int.get()
    current_detection_parameters['radius'] = radius_int.get()
    write_default_values(current_detection_parameters)


reset_button = ttk.Button(scale_frame, text="Reset", command= reset_scales)
reset_button.grid(row=4, column=3, padx=10, pady=10)

save_button = ttk.Button(scale_frame, text="Save Detection Profile", command=save_configuration_file)
save_button.grid(row=4, column=4, padx=10, pady=10)


def load_configuration_file():
    loaded_file = get_default_from_file()

    if loaded_file and isinstance(loaded_file,dict):
        print(loaded_file)
        #print(len(loaded_file))

        if len(loaded_file) == 9:
            print("data verified")

            low_h_int.set(loaded_file['lower_h'])
            high_h_int.set(loaded_file['upper_h'])
            low_s_int.set(loaded_file['lower_s'])
            high_s_int.set(loaded_file['upper_s'])
            low_v_int.set(loaded_file['lower_v'])
            high_v_int.set(loaded_file['upper_v'])
            ker_s_int.set(loaded_file['kernel'])
            blur_int.set(loaded_file['blur'])
            radius_int.set(loaded_file['radius'])

            low_h_scale_value_label.configure(text=low_h_int.get())
            high_h_scale_value_label.configure(text=high_h_int.get())
            low_s_scale_value_label.configure(text=low_s_int.get())
            high_s_scale_value_label.configure(text=high_s_int.get())
            low_v_scale_value_label.configure(text=low_v_int.get())
            high_v_scale_value_label.configure(text=high_v_int.get())

            ker_s_scale_value_label.configure(text=ker_s_int.get())
            blur_scale_value_label.configure(text=blur_int.get())
            radius_scale_value_label.configure(text=radius_int.get())
            update_the_default_parameters()



load_button = ttk.Button(scale_frame, text="Load Detection Profile", command=load_configuration_file)
load_button.grid(row=4, column=5, padx=10, pady=10)

#row 5

opencv_button_press = tk.BooleanVar(value=False)
opencv_button_text_var = tk.StringVar(value="Make Live Detection")
opencv_button = ttk.Button(scale_frame, textvariable=opencv_button_text_var, command=run_opencv)
opencv_button.grid(row=5, column=0, padx=10, pady=10)

opencv_button_stop = ttk.Button(scale_frame,text='Stop Live Detections', command= stop_opencv)
opencv_button_stop.grid(row=5, column=1, padx=10, pady=10)

scale_frame.pack(anchor='nw')

camera_frame = ttk.Frame(tab2)
camera_frame.pack(anchor='nw', fill='both', expand=True)

left_pic_label = ttk.Label(camera_frame, text="left pic" )
right_pic_label = ttk.Label(camera_frame, text="left pic")

left_pic_label.pack(side='left', expand=True, fill='both',padx=10)
right_pic_label.pack(side='left', expand=True, fill='both',padx=10)



window.mainloop()
