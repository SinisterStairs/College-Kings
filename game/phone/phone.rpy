init python:

    class Application:
        def __init__(self, name, img, homeScreen, notification=False, locked=False):
            self.name = name
            self.img = "images/phone/{}".format(img)
            self.homeScreen = homeScreen
            self.notification = notification
            self.locked = locked
            if notification:
                self.newNotification()

            applications.append(self)

        def newNotification(self):
            self.notification = True
            if not os.path.splitext(self.img)[0].endswith("Notification"):
                self.img = os.path.splitext(self.img)[0] + "Notification" + os.path.splitext(self.img)[1]

        def seenNotification(self):
            self.notification = False
            if os.path.splitext(self.img)[0].endswith("Notification"):
                self.img = os.path.splitext(self.img)[0][:-3] + os.path.splitext(self.img)[1]

        def unlock(self):
            self.locked = False

init offset = -1
default applications = []

screen phoneIcon():
    zorder 100

    imagebutton:
        if any([application.notification for application in applications]):
            idle "images/phone/phoneIconNotification.webp"
        else:
            idle "images/phone/phoneIcon.webp"
        
        if freeRoam:
            action Show("phone")
        else:
            action Call("enterPhone")
        align (0.999, 0.05)

label enterPhone:
    call screen phone


screen phoneTemplate():
    modal True

    add "images/phonescreen.webp"

    if renpy.get_screen("phone"):
        button:
            if freeRoam:
                action [Hide("tutorial"), Hide("phone")]
            else:
                action [Hide("tutorial"), Return()]

        textbutton "Exit Phone":
            style "phonebutton"
            if freeRoam:
                action [Hide("tutorial"), Hide("phone")]
            else:
                action [Hide("tutorial"), Return()]

    button:
        align (0.5, 0.5)
        xysize (400, 800)
        action NullAction()

    transclude

    if not renpy.get_screen("phone") and not renpy.get_screen("reply"):
        button:
            xysize(407, 61)
            xalign 0.5
            ypos 906
            style "phonehome"
            action Show("phone")


screen phone():
    tag phoneTag
    modal True

    use phoneTemplate:

        vpgrid:
            cols 3
            ypos 180
            xpos 787
            spacing 20

            for app in applications:
                if not app.locked:
                    vbox:
                        imagebutton:
                            idle Transform(app.img, size=(100, 100))
                            if app.name == "Kiwii" and kiwii_firstTime:
                                action Jump("kiwii_firstTime")
                            else:
                                action [Function(renpy.retain_after_load), Show(app.homeScreen)]
                                
                        text app.name style "applabels"
