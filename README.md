# MentalMathsPythonFlask


Python Flask program that helps youngsters get better at mental maths

Can be configured to test addition, subtraction, multiplication and division

Can be configured to have maximum and minimum number range for both numbers in the sum

Can be configured to have varying amount of questions

Will keep asking user same question until he/she gets it right

Results and times stored in json

Pic taken on completion and used on leaderboard (disabled by default)

#Installation and Run

Clone from git hub into your preferred working directory

Go to directory in cmd prompt and from there type    runMMPF

Open a browser and go to http://localhost:5000/login

Type in your name to start

#Admin and Leaderboard Access

to make maths easier or harder and chnage number of questions....type in admin when prompted to login at http://localhost:5000/login
    
to access leaderboard....type in leaderboard when prompted to login at http://localhost:5000/login

to enable camera.....edit hello.py

at line 220 to 226 remove comments by removing #

    # pygame.camera.init()
    # pygame.camera.list_cameras()
    # cam = pygame.camera.Camera("/dev/video0", (640, 480))
    # cam.start()
    # img = cam.get_image()
    # pygame.image.save(img, "static/" + user + date + ".jpg")
    # cam.stop()

also at line 7 remove comments by removing #
    
    # import pygame.camera